import json
from flask import Flask, render_template, request, jsonify, current_app
import google.generativeai as genai
import re

# File path to save chat history
HISTORY_FILE = "chat_history.json"

# Load chat history from file
def load_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save chat history to file
def save_history(chat_data):
    history = load_history()
    history.append(chat_data)
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file)

@current_app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    formatted_response = ""
    history = load_history()  # Load chat history on page load
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if not prompt:
            print("initiate failed" + prompt)
            response_text = "Please enter a valid prompt."
        else:
            print("initiate " + prompt)
            # Configure the Gemini API
            genai.configure(api_key=current_app.config['GEMINI_API_KEY'])
            model = genai.GenerativeModel(model_name='gemini-1.5-flash', tools="code_execution")

            try:
                # Generate content
                result = model.generate_content(prompt)
                response_text = result.text  # Extract generated text

                # Extract code snippet if it exists
                code_matches = re.findall(r"```(.*?)```", response_text, re.DOTALL)
                if code_matches:
                    formatted_response = {
                        "text": re.sub(r"```.*?```", "", response_text, flags=re.DOTALL).strip(),
                        "code": code_matches[0].strip(),
                    }
                else:
                    formatted_response = {"text": response_text, "code": None}

                # Save the generated response to history if 'save' button is pressed
                if 'save' in request.form:
                    chat_name = request.form.get('chat_name')
                    if chat_name:
                        save_history({
                            "name": chat_name,
                            "prompt": prompt,
                            "response_text": response_text,
                            "response_code": formatted_response.get("code", ""),
                        })

                        # Return JSON response indicating success
                        return jsonify({"status": "success", "message": "Chat saved successfully"})

            except Exception as e:
                response_text = f"Error: {str(e)}"
                return jsonify({
                    "status": "error",
                    "message": str(e)
                })

    return render_template('index.html', response=formatted_response, history=history)

if __name__ == "__main__":
    app.run(debug=True)
