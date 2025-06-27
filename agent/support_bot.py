import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def generate_response(user_query, policy_text=None):
    """
    Generate a contextual response using Groq (LLaMA3) and the uploaded insurance document.
    """
    if not API_KEY:
        return "❌ API key not found. Please check your .env file."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Add document text to the system prompt
    SYSTEM_PROMPT = (
        "You are InsureAI, an expert Indian insurance assistant. "
        "Answer questions using only the uploaded document and your insurance knowledge. "
        "Be concise, helpful, and avoid assuming anything not in the document."
    )

    if policy_text:
        SYSTEM_PROMPT += "\n\nPolicy Document:\n" + policy_text[:2000]  # Limit to 2000 chars

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.4
    }

    try:
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        else:
            return f"❌ API error: {res.status_code} - {res.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
