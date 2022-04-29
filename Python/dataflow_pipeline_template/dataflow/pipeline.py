import logging
from typing import List

import apache_beam as beam
from apache_beam.options import pipeline_options

from dataflow.custom_options import CustomOption
from dataflow.custom_function import some_function


def run(argv: List):

    logging.info(f"Running with args: {argv}")

    options = pipeline_options.PipelineOptions(argv)
    options = options.view_as(pipeline_options.GoogleCloudOptions)
    options = options.view_as(CustomOptions)
    pipeline = beam.Pipeline(options=options)

    (
        pipeline
        | "Creates PCollections" >> beam.Create(some_files)
        | "Some PTransform"
        >> beam.ParDo(
            some_function
        )
    )
    pipeline.run()
