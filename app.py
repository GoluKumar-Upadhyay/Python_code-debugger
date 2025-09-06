


from flask import Flask, render_template, request
from langchain.prompts import PromptTemplate
from pathlib import Path
from dotenv import load_dotenv
import os
import google.generativeai as genai   

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEN_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# ---------------- Gemini Wrapper ----------------
class GeminiLLM:
    def __init__(self, model="gemini-1.5-flash"):
        self.model = model

    def invoke(self, prompt: str) -> str:
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        return response.text

gemini_llm = GeminiLLM()

# ---------------- Flask App ----------------
app = Flask(__name__)

# Load prompt template from file or fallback
STUDENT_PROMPT = Path("prompt.txt").read_text(encoding="utf-8") if Path("prompt.txt").exists() else """
You are an experienced Python debugging assistant. Help the student debug code without giving the fixed solution.
Include: Summary, Likely root cause(s), Hints, Debug steps, Questions. Be friendly and encouraging.
"""

# LangChain PromptTemplate
template = PromptTemplate(
    input_variables=["bug_report", "student_level", "mode", "system_instructions"],
    template=(
        "{system_instructions}\n\n"
        "Bug report (raw):\n"
        "'''\n"
        "{bug_report}\n"
        "'''\n\n"
        "Context: student_level={student_level}\n\n"
        "Mode: {mode}\n\n"
        "Now produce the student-facing output as instructed in the system_instructions."
    )
)

# ---------------- Routes ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        buggy_code = request.form.get("buggy_code")
        student_level = request.form.get("student_level")

        formatted_prompt = template.format(
            system_instructions=STUDENT_PROMPT,
            bug_report=buggy_code,
            student_level=student_level,
            mode="debugging"
        )

        # Call Gemini
        response = gemini_llm.invoke(formatted_prompt)

        return render_template("result.html", code=buggy_code, level=student_level, response=response)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
