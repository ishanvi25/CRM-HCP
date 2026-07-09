import os

from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL_NAME")

print("API KEY FOUND:", bool(api_key))
print("API KEY PREFIX:", api_key[:8] if api_key else "None")
print("MODEL:", model)

# Test the key directly using the official Groq SDK
try:
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Say hello"
            }
        ]
    )

    print("✅ GROQ KEY IS VALID")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ GROQ TEST FAILED")
    print(e)

llm = ChatGroq(
    api_key=api_key,
    model=model,
    temperature=0,
)