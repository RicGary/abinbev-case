resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "brewery_data"
  location                    = var.region
  description                 = "Dataset for storing delta tables data"
  default_table_expiration_ms = 259200000 # 3 days
  project                     = var.project

  access {
    role          = "OWNER"
    special_group = "projectOwners"
  }
}