import mlflow
import os
from google import genai

experiment_id = os.environ.get("MLFLOW_EXPERIMENT_ID")
databricks_host = os.environ.get("DATABRICKS_HOST")
mlflow_tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
gemini_api_key = os.environ.get("GEMINI_API_KEY")

if (
    experiment_id is None
    or databricks_host is None
    or mlflow_tracking_uri is None
    or gemini_api_key is None
):
    raise Exception("Environment variables are not configured correctly.")

mlflow.gemini.autolog()
mlflow.set_experiment(experiment_id=experiment_id)

prompt = """
You are an empathetic and supportive storyteller, skilled in creating personal social narratives. Your goal is to generate a story that is tailored to the person's name and a specific issue or event, providing understanding and guidance for coping with the situation.
## Step by Step instructions
1. Read the provided Person Name and Issue Or Event.
2. Write a few sentences of the social story, incorporating the Person Name and addressing the Issue Or Event in an empathetic and guiding manner.
3. After every few sentences, look back over the story written so far. Does it feel complete and offer sufficient understanding and coping strategies for the person? If so, conclude the story; otherwise, go back to step 2 and continue writing, ensuring progress towards a complete and helpful narrative.

## Input
Person Name: Alice
Issue Or Event: feeling anxious about finishing a project
"""

mlflow.set_active_model(name="my-app-v1")
llm = "gemini-2.5-flash"

mlflow.log_model_params(
    {
        "prompt_template": prompt,
        "llm": llm,
    }
)

client = genai.Client(api_key=gemini_api_key)

# Inputs and outputs of the API request will be logged in a trace
data = client.models.generate_content(model=llm, contents=prompt)
