variable "project" {
  type        = string
  description = "Project ID"
}

variable "service_account_email" {
  type        = string
  description = "Service account being used by the terraform."
}

variable "schedule_import_raw_data" {
  default = "0 3 * * 1"
}

variable "region" {
  default = "southamerica-east1"
}

variable "email_to_alert" {
  type        = string
  description = "Email to send notifications to."
}

variable "environment" {}