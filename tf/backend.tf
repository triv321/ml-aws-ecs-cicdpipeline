terraform {
  backend "s3" {
    bucket         = "triv-bucket-ml" 
    key            = "prod/capstone/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks"
  }
}