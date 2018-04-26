variable "aws_region" {
  description = "The chosen region for the application."
  default = "us-east-1"
}

variable "app_name" {
  description = "The name of the S3 bucket that the firehose dumps to."
  default = "example"
}

variable "cluster_name" {
  description = "The name of the cluster you're deploying to."
  default = "koralamode"
}
