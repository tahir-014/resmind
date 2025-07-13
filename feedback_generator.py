# feedback_generator.py

def generate_feedback(score, matched, missing):
    feedback = f"✅ Your resume matches **{score}%** of the job description.\n\n"
    
    if score >= 75:
        feedback += "🎯 Great alignment! Your resume is highly relevant to the job.\n\n"
    elif score >= 50:
        feedback += "⚠️ Decent match. Consider improving alignment with job keywords.\n\n"
    else:
        feedback += "❌ Low match. You may need to tailor your resume better for this role.\n\n"

    feedback += "🟢 **Skills Present:**\n" + ", ".join(matched or ["None"]) + "\n\n"
    feedback += "🔴 **Skills Missing:**\n" + ", ".join(missing or ["None"]) + "\n\n"

    return feedback

def section_feedback(sections):
    comments = ""
    if not sections["projects"].strip():
        comments += "⚠️ Add a 'Projects' section to showcase hands-on experience.\n"
    if not sections["skills"].strip():
        comments += "⚠️ Missing 'Skills' section. Include a clear list of technical proficiencies.\n"
    if not sections["experience"].strip():
        comments += "⚠️ Add 'Experience' to highlight work/internships.\n"
    if not sections["education"].strip():
        comments += "⚠️ 'Education' section is missing or unclear.\n"

    return comments or "✅ All key resume sections are present and well-organized!"
