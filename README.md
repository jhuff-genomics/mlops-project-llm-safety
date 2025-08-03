## Multiple service cloud deployment
  This repo has multiple parts deployed to different cloud infrastructures or services, requiring accounts and different authentication for each. These each have generous free tiers, or in the case of Databricks, a free trial. However, because they must be set up separately, the process of deployment is separated into multiple parts, which makes it difficult to fully replicate the deployment only from the code. So, I have provided detailed instructions and screenshots for each part in order to show that it works, as well as enable others to follow along if they wish to replicate it.

## Frontend deployment

[![Netlify Status](https://api.netlify.com/api/v1/badges/0185d101-55fb-43ce-b6f9-ce16e5a3779b/deploy-status)](https://app.netlify.com/projects/mlops-project-llm-safety/deploys)

https://mlops-project-llm-safety.netlify.app/


## Technologies 

* **Cloud**: AWS + Databricks
* **Experiment tracking and model registry**: MLflow
* **Workflow orchestration**: Databricks jobs
* **Monitoring**: Pydantic Logfire
* **CI/CD**: GitHub Actions
* **Infrastructure as code (IaC)**: Databricks Asset Bundle (for ml-training)
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
