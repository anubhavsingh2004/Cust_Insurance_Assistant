import os
import requests
from dotenv import load_dotenv

# Load environment variables (e.g., GROQ_API_KEY)
load_dotenv()

# ✅ Set your Groq or OpenAI API key here
API_KEY = os.getenv("GROQ_API_KEY")  # Change to OPENAI_API_KEY if using OpenAI

def generate_response(user_query, policy_text=None):
    if not API_KEY:
        return "❌ API key not found."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # ✅ System prompt with instructions to format responses in clean HTML
    SYSTEM_PROMPT = (
        "You are InsureAI, an intelligent insurance assistant. "
        "Always reply using well-formatted HTML. "
        "Use <strong> for headings, <ul><li> for bullet points, <br> for line breaks, "
        "and emoji bullets like ✅, ❌, 📌 where appropriate. "
        "Keep answers clean, structured, and readable in a chat interface. "
        "Always reference the policy text when available to answer user queries accurately."
    )

    # ✅ Append the uploaded policy document to the prompt (if present)
    if policy_text:
        SYSTEM_PROMPT += (
            "\n\nHere is the insurance policy document uploaded by the user. "
            "Use this as your reference:\n"
            + policy_text[:2000]  # only send first 2000 characters for safety
        )

    payload = {
        "model": "llama3-70b-8192",  # or "gpt-4" if you're using OpenAI instead of Groq
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.4
    }

    try:
        # ✅ Send request to the Groq API (or OpenAI if configured)
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

        # Return the model's response if successful
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        else:
            return f"❌ API error: {res.status_code} - {res.text}"
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"
