import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_response(user_query):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    SYSTEM_PROMPT = (
        "You are InsureAI — an intelligent insurance advisor for Indian customers. "
        "Always respond with fresh, accurate answers based on the user's question. "
        "If the user asks about policy benefits, claims, types, or Indian insurance companies, reply accordingly. "
        "Avoid repeating previous answers."
    )

    payload = {
        "model": "llama3-70b-8192",  # ✅ Better model than 8b
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.6
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error:", response.status_code, response.text)
        return "❌ Sorry, unable to answer right now."
