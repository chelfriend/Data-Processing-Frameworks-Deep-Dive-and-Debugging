# Google DataFlow Setup Guide

## Prerequisites

- Python 3.7+
- Google Cloud Platform account
- Apache Beam Python SDK

## Installation

1. Create a virtual environment:
    ```sh
    python3 -m venv dataflow_env
    source dataflow_env/bin/activate
    ```

2. Install Apache Beam:
    ```sh
    pip install apache-beam[gcp]
    ```

3. Install other dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Google Cloud Setup

1. Set up Google Cloud SDK and authenticate:
    ```sh
    gcloud init
    gcloud auth application-default login
    ```

2. Enable DataFlow API:
    ```sh
    gcloud services enable dataflow.googleapis.com
    ```

## Running the Pipeline

Run the pipeline on Google DataFlow:
```sh
python pipeline.py --runner=DataflowRunner --project=YOUR_PROJECT_ID --temp_location=gs://YOUR_BUCKET/temp
