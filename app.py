from flask import Flask, request, jsonify, render_template
from agent.support_bot import generate_response
from agent.doc_parser import extract_text_from_pdf
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# In-memory store for uploaded document text
uploaded_text = ""

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Upload Endpoint
@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_text

    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Empty filename'}), 400

    # Save file to upload folder
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Extract text from the uploaded PDF
    uploaded_text = extract_text_from_pdf(filepath)

    return jsonify({'status': 'success', 'message': f'{filename} uploaded and processed successfully.'})

# Ask Endpoint
@app.route('/ask', methods=['POST'])
def ask():
    global uploaded_text

    user_query = request.json.get('query')
    if not user_query:
        return jsonify({'response': "⚠️ Please enter a valid question."}), 400

    # Send the question and document text to the AI
    response = generate_response(user_query, uploaded_text)
    return jsonify({'response': response})

# Start server
if __name__ == '__main__':
    app.run(debug=True)
