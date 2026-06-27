from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("=" * 50)
print("Multimodal Image Prompt Generator")
print("=" * 50)

prompt = input("Enter image description: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": f"Create a detailed AI image generation prompt for: {prompt}"
        }
    ]
)

print("\nGenerated Prompt:\n")
print(response.choices[0].message.content)