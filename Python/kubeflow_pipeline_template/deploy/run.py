"""
On-demand kubeflow pipeline trigger.
"""

import uuid
import logging

import kfp

import config


def run(
    client: kfp.Client,
    base_config: config.BaseConfig,
    runtime_config: config.RuntimeConfig,
    logger: logging.Logger,
) -> None:
    """
    Submits a pipeline run request to KFP.

    Parameters
    -------
    client: Initialized KFP client.
    base_config: Base configuration.
    runtime_config: Runtime configuration.
    logger: Logger.

    Returns
    -------
    None.
    """
    client.create_experiment(base_config.experiment_name)
    experiment = client.get_experiment(experiment_name=base_config.experiment_name)
    logger.info(f"Running pipeline under experiment: {base_config.experiment_name}")

    # Get the id of the latest pipeline version
    pipeline_id = client.get_pipeline_id(base_config.pipeline_name)
    run_id = uuid.uuid4().hex[0:6]
    job_name = f"{base_config.pipeline_name}-run-{run_id}"
    parameters = {
        "variable_name": runtime_config.variable_name
    }
    logger.info(parameters)
    client.run_pipeline(
        experiment.id,
        job_name=job_name,
        pipeline_id=pipeline_id,
        params=parameters,
    )

    logger.info(f"Run successfully submitted with job_name: {job_name}")


def main():
    """
    Parses config, initializes the client, and makes a Run request to KFP.

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
        base_config, runtime_config = config.get()  # Omitting scheduling config
        client = kfp.Client(host=base_config.kubeflow_pipelines_host)
        run(
            client,
            base_config,
            runtime_config,
            logger,
        )
    except Exception as e:  # pylint: disable=broad-except
        logger.exception("Failed to submit a pipeline run request")
        raise e


if __name__ == "__main__":
    main()
