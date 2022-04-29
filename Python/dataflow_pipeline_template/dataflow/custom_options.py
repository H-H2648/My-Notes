from apache_beam.options import pipeline_options


class CustomOptions(pipeline_options.PipelineOptions):
    "Extra parameters for the pipeline."

    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument("--some-value", required=True)