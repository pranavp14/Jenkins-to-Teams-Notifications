terraform {
  backend "s3" {
    bucket = "terraform-remote-bg-s3"
    key    = "dev/terraform.tfstate"
    region = "us-east-2"
  }
}