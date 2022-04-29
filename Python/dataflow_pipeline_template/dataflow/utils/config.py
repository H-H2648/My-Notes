from dataclasses import dataclass

from tfrecord_transform.utils import constants


@dataclass
class Resources:
    env: str
    project_id: str
    service_account: str
    output_bucket: str
    process_staging_bucket_name: str
    process_temporary_bucket_name: str


# Environment specific values are wrapped together as resource objects
# assumes multiple environemnts (dev, stage, prod)
RESOURCES = {
    constants.ENV_DEV: Resources(
        env=constants.ENV_DEV,
        project_id="project_id",
        service_account="service_account",
        output_bucket="some_bucket",
        process_staging_bucket_name="gs://some/path/",
        process_temporary_bucket_name="gs://some/path/",
    ),
    constants.ENV_STAGE: Resources(
        env=constants.ENV_STAGE,
        project_id="project_id",
        service_account="service_account",
        output_bucket="some_bucket",
        process_staging_bucket_name="gs://some/path/",
        process_temporary_bucket_name="gs://some/path/",
    ),
    constants.ENV_PROD: Resources(
        env=constants.ENV_PROD,
        project_id="project_id",
        service_account="service_account",
        output_bucket="some_bucket",
        process_staging_bucket_name="gs://some/path/",
        process_temporary_bucket_name="gs://some/path/",
    ),
}
