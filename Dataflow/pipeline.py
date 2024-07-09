
#### pipeline.py

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions

def run_dataflow_pipeline():
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = 'YOUR_PROJECT_ID'
    google_cloud_options.job_name = 'wordcount-pipeline'
    google_cloud_options.temp_location = 'gs://YOUR_BUCKET/temp'
    options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DataflowRunner'

    with beam.Pipeline(options=options) as p:
        (p
         | 'Read' >> beam.io.ReadFromText('gs://dataflow-samples/shakespeare/kinglear.txt')
         | 'CountWords' >> beam.FlatMap(lambda x: x.split())
         | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
         | 'GroupAndSum' >> beam.CombinePerKey(sum)
         | 'Write' >> beam.io.WriteToText('gs://YOUR_BUCKET/output'))

if __name__ == '__main__':
    run_dataflow_pipeline()
