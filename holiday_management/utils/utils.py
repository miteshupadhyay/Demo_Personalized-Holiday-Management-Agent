from autogen_agentchat.conditions import TextMentionTermination,MaxMessageTermination
from holiday_management.config.settings import TERMINATION_WORD

def get_termination_condition():
    """
    Get the Termination Condition for the agent.
    """
    text_mention_ternination = TextMentionTermination(TERMINATION_WORD)
    max_message_termination = MaxMessageTermination(
        max_messages=5
    )
    return text_mention_ternination | max_message_termination
    
    