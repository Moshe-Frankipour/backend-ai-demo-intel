from openai import OpenAI as OpenAIClient
import os
from dotenv import load_dotenv
import httpx

load_dotenv(override=True, verbose=True)
client = OpenAIClient(api_key=os.environ.get("OPENAI_API_KEY"))
