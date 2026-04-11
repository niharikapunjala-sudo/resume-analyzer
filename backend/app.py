from flask import Flask, request, jsonify
from flask_cors import CORS

# 1. CREATE APP FIRST (MOST IMPORTANT)
app = Flask(__name__)
CORS(app)

# 2. HOME ROUTE
@app.route("/")
def home():
    return "AI Resume Analyzer Running Successfully"

# 3. ANALYZE ROUTE
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")

    print("FILE RECEIVED:", file)

    if not file:
        return jsonify({"error": "No file uploaded"})

    text = file.read().decode("utf-8", errors="ignore")

    print("TEXT LENGTH:", len(text))

    # dummy response (working test)
    return jsonify({
        "score": 41,
        "skills_found": ["python", "react", "sql"],
        "job_match": {
            "software_engineer": 62,
            "data_scientist": 33
        },
        "missing_skills": {
            "software_engineer": ["java", "c++"]
        },
        "ai_feedback": [
            "Improve resume formatting",
            "Add more projects",
            "Mention GitHub profile"
        ]
    })

# 4. RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)