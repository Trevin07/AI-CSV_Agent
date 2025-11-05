# 📊 AI CSV Agent — Gemini-Powered CSV Data Explorer

### 🧠 About This Project
AI CSV Agent is a **Flask-based web app** that lets you **upload a CSV file** and then **chat with your data** in plain English.  
The app uses **Google’s Gemini API** to generate valid **Pandas expressions** that answer your questions — no coding needed.

Example:  
> Q: What is the average age of employees?  
> A: The AI writes and executes the code `df["age"].mean()` and shows the result instantly.

---

### ⚙️ Features
- 🔹 Upload your own CSV file securely  
- 🔹 Ask natural language questions  
- 🔹 Auto-generates and runs Pandas code  
- 🔹 Displays the AI’s executed code and result  
- 🔹 Built with Flask, Pandas, and Gemini API  

---

### 🛠️ How to Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/Trevin07/AI-CSV_Agent.git
   cd AI-CSV_Agent
