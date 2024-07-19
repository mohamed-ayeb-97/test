import streamlit as st
from flask import Flask, request, jsonify
from threading import Thread
import requests

# Define Flask app
flask_app = Flask(__name__)

@flask_app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    chat_history = data.get('chat_history', [])
    response = {'class': 'Question', 'response': 'ai_response'}  # Mock response
    return jsonify(response)

def run_flask():
    flask_app.run(host='0.0.0.0', port=5000)

# Run Flask app in a separate thread
thread = Thread(target=run_flask)
thread.daemon = True
thread.start()

# Streamlit UI
st.title("Streamlit and Flask Integration")
st.write("This is a Streamlit app running alongside a Flask app.")

query = st.text_input("Enter your query:")
if st.button("Send"):
    if query:
        response = requests.post('http://localhost:5000/chat', json={'query': query, 'chat_history': []})
        st.write("Response from Flask:", response.json())
    else:
        st.write("Please enter a query.")
