
# Step 1: Import required libraries

import os
from openai import OpenAI
from dotenv import load_dotenv


# Step 2: Load environment variables from .env

load_dotenv()


# Step 3: Retrieve Groq API key

api_key = os.getenv("GROQ_API_KEY")


# Step 4: Check whether API key exists

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


# Step 5: Initialize Groq client

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


# Step 6: Send prompt to Groq

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Explain AWS in two lines"
)


# Step 7: Print the LLM response

print(response.output_text)
