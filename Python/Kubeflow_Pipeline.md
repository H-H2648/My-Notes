```
pipenv install kfp==1.4.0
```


# What is Kubeflow Pipeline?
* It essentially allows us to run the complicated process of machine learning (from data extraction, model training, to deployment) in an organized and clear way. 
* It shows us a simple UI of exactly which component of the pipeline succeeded/failed

# Setting up component

Components can be created in the following ways:

## Docker

See [template](./kubeflow_pipeline_components_template/docker)

* run `make build`, `make push` and change the image under container under implementation to the appropriate image location after building and pushing

## No docker

See [template](./kubeflow_pipeline_components_template/no_docker)
* run `pipenv run python main.py` which will create component.yaml

# Setting up pipeline

## Simple pipeline run

See [template](./kubeflow_pipeline_template/simple)

* Set up environment variable with `source env.example`
* To run `pipenv run sh ./run_pipeline.sh`
* By running `chmod +x run_pipeline.sh` once, we can just use `pipenv run ./run_pipeline.sh` (no need for `sh`) from now on

## Deploying pipeline run

See [template](./kubeflow_pipeline_template/deploy)

* Deploy  `pipenv run python deploy.py`
* Set up environment variable with `source env.example`
* Run `pipenv run python run.py`





