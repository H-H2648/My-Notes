import sys
import logging
import argparse
from typing import List, Tuple
import datetime


def parse_arguments(arguments: List) -> Tuple(argparse.Namespace, List):
    """
    Processes pipeline arguments.
    """
    parser = argparse.ArgumentParser(
        description="parser"
    )

    parser.add_argument(
        "--value",
        required=True,
        help="Some value",
    )

    # ASSUMES THERE IS SOME ENV, don't need this (as well as config.py if there is only one environment)
    parser.add_argument(
        "--env",
        default=constants.ENV_DEV,
        choices=[constants.ENV_DEV, constants.ENV_STAGE, constants.ENV_PROD],
    )

    parser.add_argument("--local-test", action="store_true")

    parser.add_argument("--region", default=constants.DEFAULT_REGION)
    parser.add_argument(
        "--num-workers", type=int, default=constants.DEFAULT_NUM_WORKERS
    )
    parser.add_argument(
        "--max-num-workers",
        type=int,
        default=constants.DEFAULT_MAX_NUM_WORKERS,
    )
    parser.add_argument(
        "--worker-machine-type",
        default=constants.DEFAULT_WORKER_MACHINE_TYPE,
    )
    parser.add_argument("--runner", default=constants.DEFAULT_RUNNER)
    parser.add_argument("--setup-file", default=constants.DEFAULT_SETUP_FILE)
    parser.add_argument("--job-name", default=constants.DEFAULT_JOB_NAME)

    return parser.parse_known_args(arguments)


def get_dataflow_args(
    known_args: argparse.Namespace, resource: config.Resources
) -> List[str]:
    """Return the required arguments to run the pipeline on dataflow"""
    job_name = (
        f"{known_args.job_name}-{datetime.datetime.utcnow().strftime('%Y-%m-%d')}"
    )

    label = known_args.spectrogram_gcs_folder[-1]

    if known_args.local_test:
        return [
            f"--value={known_args.value}",
            f"--project={resource.project_id}",
            f"--num-shards={known_args.num_shards}",
            f"--env={resource.env}",
            f"--bucket={resource.bucket}",
            f"--staging_location={resource.process_staging_bucket_name}",
            f"--temp_location={resource.process_temporary_bucket_name}",
            f"--runner={known_args.runner}",
            f"--job-name={job_name}",
        ]
    return [
        f"--value={known_args.value}",
        f"--project={resource.project_id}",
        f"--env={resource.env}",
        f"--bucket={resource.bucket}",
        f"--staging_location={resource.process_staging_bucket_name}",
        f"--temp_location={resource.process_temporary_bucket_name}",
        f"--runner={known_args.runner}",
        f"--machine_type={known_args.worker_machine_type}",
        f"--num_workers={known_args.num_workers}",
        f"--max_num_workers={known_args.max_num_workers}",
        f"--setup_file={known_args.setup_file}",
        f"--service_account_email={resource.service_account}",
        f"--region={known_args.region}",
        f"--job_name={job_name}",
    ]


def main():
    """Run the audio data transform pipeline."""
    args, _ = parse_arguments(sys.argv)
    resources = config.RESOURCES[args.env]
    dataflow_args = get_dataflow_args(args, resources)

    pipeline.run(dataflow_args)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
