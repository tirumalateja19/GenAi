from google import genai
from dotenv import load_dotenv
load_dotenv()
client=genai.Client()
response = client.models.embed_content(
    model='gemini-embedding-001',
    contents='why is the sky blue?',
)
print(response)