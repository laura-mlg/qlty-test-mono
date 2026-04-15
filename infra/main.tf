terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

resource "aws_s3_bucket" "frontend_assets" {
  bucket = "my-app-frontend-assets"

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
