# Main entry point for the Holiday Management Agent application
# This script orchestrates the multi-agent team to help users plan holidays

from autogen_agentchat.messages import TextMessage
from holiday_management.teams.holiday_team import team
import asyncio


async def main():
    # Create a task message from the user requesting holiday planning assistance
    # This message will be processed by the holiday management team of agents
    task = TextMessage(
        content="I want to plan trip to Dubai for 5 days. Please help me with that",
        source="user"
    )

    # Execute the team with the user's task
    # The team of agents (planner, researcher, etc.) will collaborate to provide recommendations
    response = await team.run(task=task)

    # Iterate through all messages in the response and display them
    # Messages include responses from different agents and the final recommendations
    for message in response.messages:
        print(f"{message.source}: {message.content}")


# Entry point - ensures the async main function runs when script is executed directly
if __name__ == "__main__":
    asyncio.run(main())