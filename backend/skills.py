import re

SKILL_SET = [
    "python", "java", "c", "c++", "javascript", "react",
    "node", "flask", "django", "html", "css", "sql",
    "mongodb", "mysql", "git", "github",
    "machine learning", "data science", "ai"
]

def extract_skills(text):
    text = text.lower()

    # STEP 1: force clean spacing (VERY IMPORTANT FIX)
    text = re.sub(r"[^a-zA-Z+.# ]", " ", text)
    text = re.sub(r"\s+", " ", text)

    found = set()

    # STEP 2: strict matching
    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found.add(skill)

    return list(found)