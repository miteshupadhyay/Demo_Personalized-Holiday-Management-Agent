from autogen_agentchat.conditions import TextMentionTermination
from holiday_management.config.settings import TERMINATION_WORD

def get_termination_condition():
    """
    Get the Termination Condition for the agent.
    """
    text_mention_ternination = TextMentionTermination(TERMINATION_WORD)
    return text_mention_ternination
    
    