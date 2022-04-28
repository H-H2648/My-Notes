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