from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2
import os

app = Flask(__name__)
CORS(app)

# 🔥 Skill List
SKILLS = [
    "python", "java", "c", "c++", "javascript",
    "react", "node", "flask", "django",
    "html", "css", "sql", "mysql", "git", "ai"
]

@app.route("/")
def home():
    return "AI Resume Analyzer Backend Running 🚀"

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")

    if not file:
        return jsonify({"error": "No file uploaded"})

    # 📄 Read PDF
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        text = text.lower()

    except Exception as e:
        return jsonify({"error": "Error reading PDF"})

    # 🔍 Find skills
    found_skills = [skill for skill in SKILLS if skill in text]

    # 📊 Score
    score = int((len(found_skills) / len(SKILLS)) * 100)

    # 💼 Job Match
    software_skills = ["python", "java", "react", "sql", "git"]
    data_skills = ["python", "sql", "ai"]

    se_match = int((len([s for s in found_skills if s in software_skills]) / len(software_skills)) * 100)
    ds_match = int((len([s for s in found_skills if s in data_skills]) / len(data_skills)) * 100)

    # ❌ Missing Skills
    missing = [s for s in software_skills if s not in found_skills]

    # 🤖 AI Feedback (basic logic)
    feedback = []

    if score < 50:
        feedback.append("Add more technical skills")

    if "project" not in text:
        feedback.append("Include project details")

    if "github" not in text:
        feedback.append("Add GitHub profile")

    if "internship" not in text:
        feedback.append("Mention internship or experience")

    return jsonify({
        "score": score,
        "skills_found": found_skills,
        "job_match": {
            "software_engineer": se_match,
            "data_scientist": ds_match
        },
        "missing_skills": {
            "software_engineer": missing
        },
        "ai_feedback": feedback
    })


# 🚀 IMPORTANT FOR DEPLOY (RENDER)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))