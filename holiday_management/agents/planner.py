from autogen_agentchat.agents import AssistantAgent
from holiday_management.models.gpt_model import model_client

planner_agent = AssistantAgent(
    name="Holiday Planner",
    description= " A holiday Planner Agent that helps users plan their trips",
    model_client=model_client,
    system_message="You are a holiday planner agent. Your task is to help users plan their trips " \
    "by providing information about destination, itineraries and travel trips"
)