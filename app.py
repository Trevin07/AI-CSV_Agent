import os
import pandas as pd
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

# --- Setup ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
app.secret_key = "your_very_secret_key_here"
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# --- Routes ---

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file type"}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'user_data.csv')
    file.save(filepath)
    return jsonify({"success": True, "message": "File uploaded successfully."})


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("prompt")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'user_data.csv')
    if not os.path.exists(filepath):
        return jsonify({"error": "Please upload a CSV first"}), 400

    df = pd.read_csv(filepath)

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    You are a Python data analyst. You are working with a pandas dataframe named df.
    Columns: {', '.join(df.columns)}.
    Write ONE valid pandas expression that directly answers the question:
    "{question}"

    Example:
    Q: how many rows are there?
    A: len(df)

    Output ONLY the code (no explanations, markdown, or quotes).
    """

    try:
        response = model.generate_content(prompt)
        code_snippet = (
            response.text.strip()
            .replace("```python", "")
            .replace("```", "")
            .replace("\n", "")
            .strip()
        )

        # Basic validation
        if not code_snippet or any(keyword in code_snippet.lower() for keyword in ["import", "os", "system"]):
            raise ValueError("Invalid or unsafe code returned.")

        local_vars = {"df": df, "pd": pd}
        result = eval(code_snippet, {}, local_vars)

        if isinstance(result, pd.DataFrame):
            result = result.head(5).to_dict(orient="records")
        elif isinstance(result, pd.Series):
            result = result.tolist()

        return jsonify({
            "response": str(result),
            "code_executed": code_snippet
        })

    except Exception as e:
        q = question.lower()
        if "country" in q:
            col_name = next((col for col in df.columns if "country" in col.lower()), None)
            if col_name:
                countries = df[col_name].dropna().unique().tolist()
                return jsonify({"response": countries, "note": "Fallback used"})
        if "column" in q:
            return jsonify({"response": df.columns.tolist(), "note": "Fallback used"})
        if "row" in q:
            return jsonify({"response": len(df), "note": "Fallback used"})
        return jsonify({"error": f"An error occurred: {e}"}), 500


# --- Run the app ---
if __name__ == "__main__":
    app.run(port=8012, debug=True)
