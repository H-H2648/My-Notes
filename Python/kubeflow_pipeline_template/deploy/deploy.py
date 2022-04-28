"""
Kubeflow pipeline deployment taking into account pipeline versioning.
"""

import uuid
import logging
import tempfile
from pathlib import Path
from typing import Callable

import kfp

import config
import pipeline


def compile_pipeline(
    pipeline_function: Callable, package_path: str, logger: logging.Logger
) -> None:
    """
    Compiles a pipeline function into a package that will located in package_path

    Parameters
    -------
    pipeline_function: KFP function wrapped in @kfp.dsl.pipeline decorator.
    package_path: Path to write compiled pipeline to.
    logger: Logger.

    Returns
    -------
    None.
    """
    kfp.compiler.Compiler().compile(pipeline_function, package_path)
    logger.info(f"Pipeline successfully compiled to {package_path}")


def remove_existing_recurring_runs(
    client: kfp.Client, pipeline_name: str, logger: logging.Logger
) -> None:
    """
    Removes any existing scheduled recurring runs.
    Parameters
    -------
    client: Initialized KFP client.
    pipeline_name: Pipeline name.
    logger: Logger.

    Returns
    -------
    None.
    """

    recurring_runs = client.list_recurring_runs()
    if recurring_runs.jobs is not None:
        logger.info("Deleting existing scheduled runs")
        for job in recurring_runs.jobs:
            if pipeline_name in job.name:
                logger.info(f"Deleting scheduled run: {job.id}")
                client._job_api.delete_job(job.id)  # pylint: disable=protected-access


def upload_pipeline(
    client: kfp.Client, pipeline_name: str, package_path: str, logger: logging.Logger
) -> str:
    """
    Uploads a pipeline - if it already exists, creates a pipeline version.
    Parameters
    -------
    client: Initialized KFP client.
    pipeline_name: Pipeline name.
    package_path: Location of compiled pipeline.
    logger: Logger.

    Returns
    -------
    pipeline version id.
    """
    if client.get_pipeline_id(pipeline_name):
        pipeline_version_name = uuid.uuid4().hex[0:6]
        pipeline_version = client.upload_pipeline_version(
            package_path, pipeline_version_name, pipeline_name=pipeline_name
        )
        logger.info(
            f"Pipeline version updated -- new version name: {pipeline_version_name}"
        )
    else:
        pipeline_version = client.upload_pipeline(package_path, pipeline_name)
        logger.info(f"New pipeline deployed -- version name: {pipeline_version.name}")
    return pipeline_version.id


# pylint: disable=too-many-arguments
def deploy(
    client: kfp.Client,
    pipeline_function: Callable,
    base_config: config.BaseConfig,
    logger: logging.Logger,
) -> None:
    """
    Compiles and deploys a pipeline.

    Parameters
    -------
    client: Initialized KFP client.
    pipeline_function: KFP function wrapped in @kfp.dsl.pipeline decorator.
    base_config: Base configuration.
    logger: Logger.

    Returns
    -------
    None.
    """
    with tempfile.TemporaryDirectory() as tempdir:
        package_path = str(Path(tempdir, f"{base_config.pipeline_name}.zip"))
        compile_pipeline(pipeline_function, package_path, logger)

        remove_existing_recurring_runs(client, base_config.pipeline_name, logger)

        _ = upload_pipeline(client, base_config.pipeline_name, package_path, logger)


def main():
    """
    Parses config, initializes the client, and deploys the pipeline.
    Parameters
    -------
    None.

    Returns
    -------
    None.
    """
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    try:
        base_config, _ = config.get()
        client = kfp.Client(host=base_config.kubeflow_pipelines_host)
        deploy(
            client,
            pipeline.definition,
            base_config,
            logger,
        )
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Failed to deploy pipeline")
        raise e


if __name__ == "__main__":
    main()
