def predict_company_and_salary(resume_text, jobrole):
    resume_text = resume_text.lower()
    company = "Unknown"
    salary = "Not Estimated"

    # Rule-based prediction
    if "machine learning" in resume_text or "python" in resume_text:
        company = "Google"
    elif "cloud" in resume_text or "aws" in resume_text:
        company = "Amazon"
    elif "java" in resume_text or "spring" in resume_text:
        company = "Infosys"
    elif "data analysis" in resume_text or "sql" in resume_text:
        company = "Accenture"
    elif "web development" in resume_text or "react" in resume_text:
        company = "Microsoft"

    # Salary range based on role
    base_salaries = {
        "data_scientist": "₹8–20 LPA",
        "ai_engineer": "₹10–25 LPA",
        "ml_engineer": "₹7–22 LPA",
        "web_developer": "₹5–15 LPA",
        "software_engineer": "₹6–18 LPA"
    }
    salary = base_salaries.get(jobrole, "₹6–12 LPA")
    return company, salary
