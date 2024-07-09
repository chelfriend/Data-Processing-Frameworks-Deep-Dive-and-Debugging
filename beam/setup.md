# Apache Beam Setup Guide

## Prerequisites

- Python 3.7+
- Apache Beam Python SDK

## Installation

1. Create a virtual environment:
    ```sh
    python3 -m venv beam_env
    source beam_env/bin/activate
    ```

2. Install Apache Beam:
    ```sh
    pip install apache-beam
    ```

3. Install other dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Pipeline

Run the pipeline locally using the DirectRunner:
```sh
python pipeline.py
