variable "region" {
  default = "southamerica-east1"
}

variable "project" {
  default = "abinbev-case-eric"
}

variable "apis" {
  type        = list(string)
  description = "APIs to be enabled."
}