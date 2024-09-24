resource "google_storage_bucket" "abinbev-database-raw" {
  project                     = var.project
  name                        = "abinbev-database-raw"
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket" "abinbev-database-delta-lake" {
  project                     = var.project
  name                        = "abinbev-database-delta-lake"
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket" "abinbev-scripts-case" {
  project                     = var.project
  name                        = "abinbev-scripts-case"
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_storage_bucket" "abinbev-temp" {
  project                     = var.project
  name                        = "abinbev-temp"
  location                    = var.region
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}