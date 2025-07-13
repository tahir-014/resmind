# resume_parser.py

import re
from pdfminer.high_level import extract_text

def extract_resume_text(file_path):
    try:
        return extract_text(file_path)
    except Exception as e:
        return f"Error reading file: {e}"

def extract_sections(resume_text):
    sections = {
        "education": "",
        "experience": "",
        "skills": "",
        "projects": "",
        "contact": "",
    }
    
    # Normalize
    lines = resume_text.lower().splitlines()

    current_section = None
    for line in lines:
        line = line.strip()

        # Detect section headers
        if "education" in line:
            current_section = "education"
        elif any(x in line for x in ["experience", "employment", "work"]):
            current_section = "experience"
        elif "project" in line:
            current_section = "projects"
        elif "skill" in line:
            current_section = "skills"
        elif any(x in line for x in ["phone", "email", "contact"]):
            current_section = "contact"

        # Append to current section
        if current_section and line:
            sections[current_section] += line + "\n"

    return sections
