resource "google_monitoring_notification_channel" "alert_channel" {
  project      = var.project
  display_name = "alert-channel-${var.environment}"
  type         = "email"
  labels = {
    email_address = var.email_to_alert
  }
  force_delete = false
}