import argparse
import logging
import tempfile
from pathlib import Path

import kfp

PIPELINE_NAME = "PIPELINE_NAME"
EXPERIMENT_NAME = "EXPERIMENT_NAME"
JOB_NAME = "JOB_NAME"


logging.basicConfig(level=logging.INFO)

component_paths = {
    "NAME_OF_COMPONENT": "path to component.yaml of this component",
}

component_op = kfp.components.load_component_from_file(
    component_paths["NAME_OF_COMPONENT"]
)


@kfp.dsl.pipeline(
    name="PIPELINE NAME",
    description="PIPELINE DESCRIPTION",
)
def pipeline(
    values,
):
    # pylint: disable=not-callable
    component_task = component_op(
        value=values
    )

    # For skipping caching
    component_task.execution_options.caching_strategy.max_cache_staleness = (
        "P0D"
    )

    # to extract output of this component to use as input of the next component, use component_task.output as input for next comopnent


if __name__ == "__main__":
    """
    Runs the Feast get_latest_features pipeline.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--value-name", type="some_type")

    args = parser.parse_args()

    with tempfile.TemporaryDirectory() as tempdir:
        client = kfp.Client(host=args.kubeflow_host)

        pipeline_path = Path(tempdir, f"{JOB_NAME}.zip")
        kfp.compiler.Compiler().compile(
            pipeline, str(pipeline_path)
        )

        experiment = client.create_experiment(name=EXPERIMENT_NAME)
        run = client.run_pipeline(
            experiment.id,
            JOB_NAME,
            str(pipeline_path),
            params={
                "value": args.value
            },
        )
