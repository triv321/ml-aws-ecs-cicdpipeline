terraform {
  backend "s3" {
    bucket         = "ml-pipeline-bucket" 
    key            = "prod/capstone/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-locks" 
  }
}