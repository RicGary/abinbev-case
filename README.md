# Open Brewery DB Data Pipeline

This project is designed to fetch data from the [Open Brewery DB API](https://api.openbrewerydb.org/breweries), transform it, and store it in a data lake following the medallion architecture (Bronze, Silver, and Gold layers). The infrastructure for this project is built on Google Cloud Platform (GCP) using Terraform, with the orchestration and containerization aspects handled via a modularized approach.

## Project Structure

- **Bronze Layer**: Raw data is fetched from the API and stored in its native format (JSON).
- **Silver Layer**: Data is transformed into a columnar format (e.g., Parquet or Delta) and partitioned by brewery location.
- **Gold Layer**: Aggregated data is stored, providing insights such as the number of breweries per type and location.

## Prerequisites

- Google Cloud Platform account
- Terraform installed on your local machine
- Service account with appropriate permissions for Terraform
- Billing account set up for the GCP project
- Docker installed (for containerization)

## Infrastructure Setup

### 1. Create a Google Cloud Project

- Log in to your GCP account and create a new project.
- Make sure billing is enabled for the project.

### 2. Set Up Service Account for Terraform

- Create a service account for Terraform with the **Owner** role.
- Download the JSON key for the service account.
- Update `terraform.tfvars` with the service account key by following the format in `terraform.tfvars.example`.

### 3. Deploy Docker Images to Artifact Registry

- Navigate to the `./openbrewerydb/batches` directory and follow the instructions to deploy Docker images for each pipeline code to Google Cloud Artifact Registry.
  - **Note**: For this version, each workflow requires a separate image deployment. (This could be optimized in the future.)

### 4. Configure Workflow Image URIs

- After deploying the Docker images, update the `imageUri` fields in `./terraform/environments/dev/variables.tf` with the corresponding URIs for each workflow.

### 5. Build the Infrastructure Using Terraform

- Run the following commands to initialize and apply Terraform configurations:

  ```bash
  terraform init
  terraform plan
  ```

- If the plan looks correct, apply the changes:

  ```bash
  terraform apply
  ```

### 6. Start the Scheduler

After applying the Terraform plan, manually unpause the scheduler in the GCP Console.

## Data Pipeline Instructions

### API Data Fetching

- The project consumes data from the Open Brewery DB API using the following endpoint:
    `https://api.openbrewerydb.org/breweries`
    The data is ingested into the Bronze Layer as raw JSON format.

### Data Transformation

- The pipeline transforms the raw data into a Delta format for the Silver Layer.
- The data is partitioned by brewery location (country and state).

### Aggregation for Gold Layer

- The Gold Layer contains aggregated insights on the number of breweries per type and location.
- This layer enables analytical queries on brewery data that can be accessed using BigQuery.

