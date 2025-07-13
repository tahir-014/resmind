from flask import Flask, render_template, request
import os
from resume_parser import extract_resume_text, extract_sections
from analyzer import analyze_resume_vs_jd
from feedback_generator import section_feedback
from mnc_predictor import predict_company_and_salary


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        jobrole = request.form["jobrole"]

        if resume_file and resume_file.filename.endswith(".pdf"):
            resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(resume_path)
            resume_text = extract_resume_text(resume_path)
    
            jd_path = f"job_descriptions/{jobrole}.txt"
            try:
                with open(jd_path, 'r', encoding='utf-8') as f:
                    jd_text = f.read()
            except FileNotFoundError:
                return "Job description not found."

            result = analyze_resume_vs_jd(resume_text, jd_text)
            sections = extract_sections(resume_text)
            section_tip = section_feedback(sections)

            company, salary = predict_company_and_salary(resume_text, jobrole)

            return render_template("index.html",
                                   **result,
                                   sections=sections,
                                   section_tip=section_tip,
                                   job_role=jobrole.replace("_", " ").title(),
                                   company=company,
                                   salary=salary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
