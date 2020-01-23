variable "acmcertificatearn" { }
variable "route53-zone-id" { }
variable "host" { }
variable "subdomain" { }
variable "api-id" { }
variable "region" { }
variable "stage" { }

provider "aws" {
  profile    = "default"
  region     = var.region
}

resource "aws_api_gateway_domain_name" "custom-subdomain" {
  certificate_arn = var.acmcertificatearn
  domain_name     = "${var.subdomain}.${var.host}"
}

resource "aws_api_gateway_base_path_mapping" "path-mapping" {
  api_id      = var.api-id
  stage_name  = var.stage
  domain_name = aws_api_gateway_domain_name.custom-subdomain.domain_name
}

resource "aws_route53_record" "custom-route53-record" {
  zone_id = var.route53-zone-id
  name    = aws_api_gateway_domain_name.custom-subdomain.domain_name
  type    = "A"
  alias {
    name                   = aws_api_gateway_domain_name.custom-subdomain.cloudfront_domain_name
    zone_id                = aws_api_gateway_domain_name.custom-subdomain.cloudfront_zone_id
    evaluate_target_health = true
  }
}
