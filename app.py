from flask import Flask, request, jsonify, render_template
from agent.support_bot import generate_response
from agent.doc_parser import extract_text_from_pdf
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for upload folder
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query')   # ✅ Get dynamic query
    print("User asked:", user_query)         # ✅ Log to console
    if not user_query:
        return jsonify({'response': "No question received."}), 400

    response = generate_response(user_query)
    return jsonify({'response': response})

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'Empty filename'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    pdf_text = extract_text_from_pdf(filepath)
    return jsonify({'status': 'success', 'message': f'{filename} uploaded and text extracted.', 'text': pdf_text[:300]})

if __name__ == '__main__':
    app.run(debug=True)
