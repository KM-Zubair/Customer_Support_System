from flask import Flask, request, jsonify
from loaders import load_documents
from splitter import split_documents
from vectorstore import create_vectorstore
from conversation_chain import setup_conversation_chain

app = Flask(__name__)

# Load, split, and store documents
documents = load_documents()
chunks = split_documents(documents)
vectorstore = create_vectorstore(chunks)

# Set up the conversation chain
conversation_chain, memory = setup_conversation_chain(vectorstore)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = conversation_chain.run(user_input, memory=memory)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
