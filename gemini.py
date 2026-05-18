from google import genai
from dotenv import load_dotenv
load_dotenv()
client=genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="What is 2+2*0"
)
print(response.text)