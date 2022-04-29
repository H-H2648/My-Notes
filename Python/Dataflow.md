Recommended pipenv install

```
pipenv install apache-beam[gcp]==2.38.0
```

## Basic

Consists of:

* `Pipeline`: encapsulates your entire data processing task, from start to finish. This includes reading input data, transforming that data, and writing output data.
* `PCollection`: represents a distributed data set that the Beam pipeline operates on. The data set can comes from a fixed source like a file, or a continuously updating source via a subscription or other mechanism. Typically pipelines create initial PCollections by reading data from an external data source.
* `PTransform`: represents a data processing operation, or a step, in your pipeline. Every PTransform takes one or more PCollection objects as input, performs a processing function and produces zero or more output PCollection objects.

## Create pipeline
```
import apache_beam as beam

pipeline = beam.Pipeline()
```

## Configure pipeline option
We can configure the option of pipeline (where to run the pipeline, gcp project id and so on)

```
from apache_beam.options.pipeline_options import PipelineOptions

beam_options = PipelineOptions()
```

configures values from the commandline.

To create a custom option, do the following:

```
from apache_beam.options.pipeline_options import PipelineOptions

class MyOptions(PipelineOptions):
  @classmethod
  def _add_argparse_args(cls, parser):
    parser.add_argument('--input-file')
    parser.add_argument('--output-path')
```

## Creating PCollection

To read data (can be in the cloud or local)

```
create_collections = pipeline | "Reading" >> beam.create(
    "location of data")
```

## Applying transformaion

In general it follows (from create to transformations):

```
pipeline = beam.Pipeline()
(pipeline | beam.create(
    "location of data") | some_transformation | some_transformation 
)
```

The transformation can be done in `beam.Map(function, other_variables)` which applies each value of the data to the function (one-to-one) and outputs a new collection of outputs

The transformation can also be `ParDo` as in the example below:

```
class ComputeWordLengthFn(beam.DoFn):
  def process(self, element):
    return [len(element)]

word_lengths = pipeline | beam.ParDo(ComputeWordLengthFn())
```

Finally an template dataflow pipeline is found [here](./dataflow_pipeline_template)