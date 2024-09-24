####################################
#             Services             #
####################################

module "services" {
  source  = "../../modules/services"
  project = "abinbev-case-eric"
  apis = [
    "monitoring.googleapis.com",           # Cloud Monitoring API
    "pubsub.googleapis.com",               # Cloud Pub/Sub API
    "run.googleapis.com",                  # Cloud Run Admin API
    "secretmanager.googleapis.com",        # Secret Manager API
    "servicemanagement.googleapis.com",    # Service Management API
    "serviceusage.googleapis.com",         # Service Usage API
    "storage-api.googleapis.com",          # Google Cloud Storage JSON API
    "storage-component.googleapis.com",    # Cloud Storage
    "storage.googleapis.com",              # Cloud Storage API
    "workflowexecutions.googleapis.com",   # Workflow Executions API
    "workflows.googleapis.com",            # Workflows API
    "batch.googleapis.com",                # Batch API
    "cloudapis.googleapis.com",            # Google Cloud APIs
    "cloudbuild.googleapis.com",           # Cloud Build API
    "cloudfunctions.googleapis.com",       # Cloud Functions API
    "cloudscheduler.googleapis.com",       # Cloud Scheduler API
    "compute.googleapis.com",              # Compute Engine API
    "dataproc.googleapis.com",             # Cloud Dataproc API
    "datastream.googleapis.com",           # Datastream API
    "eventarc.googleapis.com",             # Eventarc API
    "iam.googleapis.com",                  # Identity and Access Management (IAM) API
    "iamcredentials.googleapis.com",       # IAM Service Account Credentials API
    "logging.googleapis.com",              # Cloud Logging API
    "cloudresourcemanager.googleapis.com"  # Cloud Resource API
  ]
}

####################################
#             BUCKETS              #
####################################

module "abinbev_buckets" {
  source = "../../modules/buckets"
  region = var.region
  project = var.project
}

####################################
#             WORKFLOWS            #
####################################

module "abinbev_workflows" {
  source         = "../../modules/workflows"
  project = var.project
  region = var.region
  # env_vars = {}
}

####################################
#             SCHEDULER            #
####################################

module "tiai_scheduler" {
  source = "../../modules/scheduler"
  project = var.project
  service_account_email = var.service_account_email
  schedule_import_raw_data = var.schedule_import_raw_data
}

####################################
#             BIGQUERY             #
####################################

module "abinbev_big_query" {
  source         = "../../modules/big_query"
  region         = var.region
  project        = var.project
}