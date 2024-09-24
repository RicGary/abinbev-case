resource "google_workflows_workflow" "import-raw-data" {
  project         = var.project
  name            = "import-raw-data"
  region          = var.region
  source_contents = file("../../../workflows/import_raw_data.yaml")
}

resource "google_workflows_workflow" "convert-json-delta" {
  project         = var.project
  name            = "convert-json-delta"
  region          = var.region
  source_contents = file("../../../workflows/convert_json_delta.yaml")
}

resource "google_workflows_workflow" "export-delta-to-bq" {
  project         = var.project
  name            = "export-delta-to-bq"
  region          = var.region
  source_contents = file("../../../workflows/export_to_bq.yaml")
}