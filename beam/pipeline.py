
#### pipeline.py

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_beam_pipeline():
    options = PipelineOptions()
    with beam.Pipeline(options=options) as p:
        (p
         | 'Read' >> beam.io.ReadFromText('sample_data.txt')
         | 'CountWords' >> beam.FlatMap(lambda x: x.split())
         | 'PairWithOne' >> beam.Map(lambda x: (x, 1))
         | 'GroupAndSum' >> beam.CombinePerKey(sum)
         | 'Write' >> beam.io.WriteToText('output.txt'))

if __name__ == '__main__':
    run_beam_pipeline()
