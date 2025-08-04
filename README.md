## Multiple service cloud deployment
  This repo has multiple parts deployed to different cloud infrastructures and services, requiring accounts and different authentication for each. These each have generous free tiers, or in the case of Databricks, a free trial. However, because they must be set up separately, the process of deployment is separated into multiple parts, which makes it unclear how to fully replicate from a single invocation, such as `make all`. So, I have provided detailed instructions and screenshots for each part in order to demonstrate that it works, as well to enable others in following along if they wish to replicate it.


## Training

The `mlflow` server is run on Databricks on AWS.
![mlflow artifacts on Databricks](png/Databricks_mlfow_model_artifacts.png)


## Serverless web service deployment to Modal

To create environment secrets `Databricks-MLflow` to securely interact with Databricks and its managed MLflow, run the following using the modified `.env` file:
```
$ cd ml-deploy
$ uv run modal secret create Databricks-MLflow --from-dotenv .env
```

## Using the API

Test the API response:
```
$ curl -X POST -H 'Content-Type: application/json' --data-binary '{["qty": 5]}' https://jhuff-genomics--modal-fastapi-endpoint-py-stream-me-dev.modal.run
```

OpenAPI (aka Swagger) docs for how to use the API are at:
```
https://jhuff-genomics--modal-fastapi-endpoint-py-stream-me-dev.modal.run/docs/
```

## Technologies 

* **Cloud**: AWS + Databricks (for `ml-train/`), Modal.com serverless containers (for `ml-deploy/`)
* **Experiment tracking and model registry**: Databricks MLflow
* **Monitoring**: Databricks MLflow Tracing
* **Best Practices**:
  * `uv` package management
  * `ruff` linting and code formatting
  * `pre-commit` hooks


## Accounts

* **Databricks**: 
   * A free trial of Databricks on AWS is available: [Databricks free trial](https://docs.databricks.com/aws/en/getting-started/free-trial)
   * Alternatively, Databricks can be used on Azure, GCP or SAP clouds, and on the trial page, the appropriate cloud can be selected at top right
   * Authentication to Databricks is required, and the method assumed in this repo is: [Databricks configuration profiles](https://docs.databricks.com/aws/en/dev-tools/auth/config-profiles)
   * An authentication profile is configured most easily with the Databricks CLI tools: `databricks configure`, CLI installation instructions at [Databricks CLI tutorial](https://docs.databricks.com/aws/en/dev-tools/cli/tutorial)

* **Modal.com**: 
   * A free tier of Modal.com is available: [Modal.com pricing](https://modal.com/pricing)
   * Authentication to Modal from a dev computer is easiest from `uv`, which will open a browser to authorize access and set up a token locally:
   ```
   cd ml-deploy
   uv run python3 -m modal setup
   ```
