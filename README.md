AI CSV Agent — Gemini-Powered CSV Data Explorer
🧠 About This Project

AI CSV Agent is a Flask-based web app that lets you upload a CSV file and then chat with your data in plain English.
The app uses Google’s Gemini API to generate valid Pandas expressions that answer your questions — no coding needed.

Example:

Q: What is the average age of employees?
A: The AI writes and executes the code df["age"].mean() and shows the result instantly.

⚙️ Features

🔹 Upload your own CSV file securely

🔹 Ask natural language questions

🔹 Auto-generates and runs Pandas code

🔹 Displays the AI’s executed code and result

🔹 Built with Flask, Pandas, and Gemini API

🛠️ How to Run Locally

Clone this repo:

git clone https://github.com/YOUR_USERNAME/AI_CSV_Agent.git
cd AI_CSV_Agent

Install dependencies:

pip install -r requirements.txt

Create a .env file and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here
FLASK_SECRET_KEY=your_secret_key_here

Run the app:

python app.py

Visit in your browser:

http://127.0.0.1:8012
🧩 Project Structure
AI_CSV_Agent/
│
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # Frontend HTML page
├── uploads/             # Temporary upload folder (ignored in Git)
├── .env                 # API key storage (ignored)
├── .gitignore
└── README.md
🔐 Security Notes

Your .env and uploads/ are ignored by Git for privacy.

This app uses eval() for AI-generated code — it’s safe for local use, not public deployment.

🖼️ Screenshot (Add Yours Below)

Add a screenshot of your web UI here once the app is running locally.

![Web UI Screenshot](ss1.png)
![Web UI Screenshot](ss2.png)
![Web UI Screenshot](ss3.png)

🧑‍💻 Built By

Trevin Rodrigo — Data Science Enthusiast & AI Developer
Sri Lanka 🇱🇰
