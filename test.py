import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Read API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set.")
    exit()

try:
    # Create OpenAI client
    client = OpenAI(api_key=api_key)

    # Make a simple API request
    response = client.responses.create(
        model="gpt-4o",
        input="Say hello in one short sentence."
    )

    print("✅ OpenAI API Key is working!")
    print("Response:")
    print(response.output_text)

except Exception as e:
    print("❌ OpenAI API request failed.")
    print(f"Error: {e}")