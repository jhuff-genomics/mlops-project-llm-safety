## Multiple service cloud deployment
  This repo has multiple parts deployed to different cloud infrastructures and services, requiring accounts and different authentication for each. These each have generous free tiers, or in the case of Databricks, a free trial. However, because they must be set up separately, the process of deployment is separated into multiple parts, which makes it unclear how to fully replicate from a single invocation, such as `make all`. So, I have provided detailed instructions and screenshots for each part in order to demonstrate that it works, as well to enable others in following along if they wish to replicate it.


## Training

The `mlflow` server is run locally with a local SQLite backend, defaulting to `http://127.0.0.1:5000`:
```
cd ml-train
uv run mlflow server --backend-store-uri sqlite:///mydb.sqlite
```


## Serverless web service deployment to Modal

Test the API response:
`curl -X POST -H 'Content-Type: application/json' --data-binary '{["qty": 5]}' https://jhuff-genomics--modal-fastapi-endpoint-py-stream-me-dev.modal.run`

OpenAPI (aka Swagger) docs at:
`https://jhuff-genomics--modal-fastapi-endpoint-py-stream-me-dev.modal.run/docs/`


## Frontend Astro Netlify app

[![Netlify Status](https://api.netlify.com/api/v1/badges/0185d101-55fb-43ce-b6f9-ce16e5a3779b/deploy-status)](https://app.netlify.com/projects/mlops-project-llm-safety/deploys)

https://mlops-project-llm-safety.netlify.app/


## Technologies 

* **Cloud**: AWS + Databricks, Modal.com serverless containers (for `ml-deploy/`)
* **Experiment tracking and model registry**: Databricks MLflow
* **Workflow orchestration**: Databricks Jobs
* **Monitoring**: Pydantic Logfire
* **CI/CD**: GitHub Actions
* **Infrastructure as code (IaC)**: Databricks Asset Bundle (for `ml-train/`)
* **Best Practices**:
  * uv package management
  * pytest for testing
  * ruff linting and code formatting


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
