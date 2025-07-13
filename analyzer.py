# analyzer.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB", "ADJ"] and not token.is_stop]

def analyze_resume_vs_jd(resume_text, jd_text):
    resume_keywords = set(extract_keywords(resume_text))
    jd_keywords = set(extract_keywords(jd_text))

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords.difference(resume_keywords)

    match_score = int((len(matched) / len(jd_keywords)) * 100)

    from feedback_generator import generate_feedback
    feedback = generate_feedback(match_score, matched, missing)

    return {
        "score": match_score,
        "matched": sorted(matched),
        "missing": sorted(missing),
        "total": len(jd_keywords),
        "feedback": feedback
    }
