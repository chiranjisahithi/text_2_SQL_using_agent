import os
import pandas as pd
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # wrapper for external models
from src.instructions import INSTRUCTIONS
from src.tools.query_runner_tool import create_sql_tool

#  Grok API Key for Google ADK
os.environ["XAI_API_KEY"] = "---your grok api key here----"

#  Load Superstore dataset
df = pd.read_excel("src/data/SampleSuperstore.xls", sheet_name="Orders")

# Create SQL tool with the loaded dataset
run_sql_tool = create_sql_tool(df)

# Set up the wrapper
model_wrapper = LiteLlm(model="xai/grok-3-mini", api_key_env="XAI_API_KEY")

#  Define the root agent — same as 2-tool-agent format
root_agent = Agent(
    name="superstore_agent",
    model=model_wrapper,
    description="An agent that analyzes the Superstore dataset using Grok 3 Mini.",
    instruction=INSTRUCTIONS,
    tools=[run_sql_tool],
)
