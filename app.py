from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This part changed to save data to a file
@app.route('/log_click', methods=['POST'])
def log_click():
    data = request.json
    # Get the current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save the click information to a text file
    with open("inquiries.txt", "a") as file:
        file.write(f"Inquiry at {now} - Action: {data.get('action')}\n")
    
    print(f"--- SUCCESS: Inquiry saved to inquiries.txt at {now} ---")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5050)