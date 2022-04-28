"""
Pipeline configuration.
"""

from typing import Tuple

from pydantic import BaseSettings


class BaseConfig(BaseSettings):  # pylint: disable=too-few-public-methods
    """
    Base pipeline configuration.

    Returns
    -------
    BaseConfig object
        - kubeflow_pipelines_host: KFP host address.
        - pipeline_name: Pipeline name.
        - experiment_name: Name of the experiment to run pipeline under.
    """

    kubeflow_pipelines_host: str
    pipeline_name: str
    experiment_name: str


class RuntimeConfig(BaseSettings):  # pylint: disable=too-few-public-methods
    """
    Pipeline runtime configuration.
    Returns
    -------
    RuntimeConfig object
        - variable_name: variable description
    """
    variable_name: some_type


def get() -> Tuple[BaseConfig]:
    """
    Returns initialized configuration objects.

    Parameters
    -------
    None.

    Returns
    -------
    BaseConfig objects.
    """
    base_config = BaseConfig()
    runtime_config = RuntimeConfig()
    return base_config, runtime_config
