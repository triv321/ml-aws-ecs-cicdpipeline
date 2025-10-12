variable "aws_region" {
  description = "The AWS region for our ml-pipeline"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "The name of our project, used for tagging resources."
  type        = string
  default     = "ml-api-capstone"
}

variable "vpc_cidr" {
  description = "The main CIDR block for our VPC."
  type        = string
  default     = "10.0.0.0/16"
}