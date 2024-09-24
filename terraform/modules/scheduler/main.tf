resource "google_cloud_scheduler_job" "import-raw-data" {
  name             = "trigger-import-raw-data"
  description      = "Trigger for import-raw-data process"
  project          = var.project
  region           = var.region
  schedule         = var.schedule_import_raw_data
  time_zone        = "UTC"
  paused           = true

  retry_config {
    retry_count          = 1
    min_backoff_duration = "60s"
  }

  http_target {
    http_method = "POST"
    uri         = "https://workflowexecutions.googleapis.com/v1/projects/${var.project}/locations/${var.region}/workflows/import-raw-data/executions"
    body        = ""

    oauth_token {
      service_account_email = var.service_account_email
    }
  }
}
