terraform {
  backend "s3" {
    bucket = "terraform-taxim-bucket"
    key    = "global/s3/terraform.tfstate"
    region = "eu-central-1"

    dynamodb_table = "terraform-taxim-db"
    encrypt        = true
  }
}
