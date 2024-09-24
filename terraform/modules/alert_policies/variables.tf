variable "region" {
  default = "southamerica-east1"
}

variable "project" {
  default = "abinbev-case-eric"
}

variable "environment" {}

variable "email_to_alert" {
  type        = string
  description = "Email to send notifications to."
}