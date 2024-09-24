resource "google_project_service" "services" {
  # Enable the services
  for_each           = toset(var.apis)
  project            = var.project
  service            = each.value
  disable_on_destroy = false
}