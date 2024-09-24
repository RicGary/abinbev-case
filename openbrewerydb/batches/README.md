## Overview

This repository contains a Docker setup for importing raw brewery data from the OpenBrewery API into a Google Cloud Storage bucket. It includes a Dockerfile for building the Docker image and a Python script to handle the data retrieval and storage.

## Prerequisites

- **Google Cloud SDK**: Ensure that you have the Google Cloud SDK installed and configured.
- **Docker**: Install Docker to build and manage the container.
- **Google Cloud Storage Bucket**: You should have a Google Cloud Storage bucket created.

## Building the Docker Image

To build the Docker image, follow these steps:

1. **Authenticate Docker with Google Cloud**:

```bash
gcloud auth configure-docker
```

2. **Build the Docker Image**:

```bash
docker build -t gcr.io/<PROJECT-ID>/<DOCKER-IMAGE-NAME> -f ./batches/Dockerfile .
```

3. **Push the Docker Image to Google Container Registry**:

```bash
docker push gcr.io/<PROJECT-ID>/<DOCKER-IMAGE-NAME>
```

