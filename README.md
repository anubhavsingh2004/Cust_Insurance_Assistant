# Cust_Insurance_Assistant
This is a customer insurance assistant agent that helps customers know more about BSIF

**InsureAI** is a GenAI-powered Flask web application that acts as an intelligent insurance assistant. It allows users to ask questions about insurance policies and upload documents (e.g., PDFs), from which the AI can extract and answer context-specific queries.



## Features

- Chat interface for insurance-related queries  
- Upload support for PDFs and text files  
- AI-powered answers using Groq + LLaMA3 (or any compatible LLM)  
- Context-aware responses based on uploaded content  
- Sleek and responsive frontend UI with modern gradient    

## Project Structure
.
├── app.py # Flask backend entry point
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
├── agent/
│ ├── support_bot.py # Query handler and Groq API logic
│ └── doc_parser.py # PDF parser for uploaded content
├── templates/
│ └── index.html # Frontend UI
├── data/ # Uploaded documents
└── static/ (optional) # Any static CSS/images (not currently used)


## Getting Started (Local Development)

### Prerequisites

- Python 3.8+
- Pip (Python package manager)
- A [Groq API key](https://console.groq.com/keys)


### Installation

# 1. Clone the repo
git clone https://github.com/yourusername/insureai.git
cd insureai

# 2. Set up virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key (Groq or OpenAI)
export GROQ_API_KEY=your_api_key_here  # On Windows: set GROQ_API_KEY=your_key
Run the App
python app.py
Open your browser and visit http://127.0.0.1:5000

# How It Works
1. User uploads a PDF policy document (e.g., health, home, car).
2. The file is parsed using doc_parser.py to extract text.
3. User asks a natural-language question.
4. The chatbot combines document content and user query using Groq's API.
5. A well-formatted AI-generated answer is returned in real-time.

# Example Use Case:
Ask: "What does Clause 11 mean in this policy?"
Upload: "sample_insurance_policy.pdf"
Get: "Clause 11: Accidental damage to garden equipment..."
