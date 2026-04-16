from fastapi import FastAPI
import json
from rapidfuzz import fuzz

app = FastAPI()

with open("kb.json", encoding="utf-8") as f:
    KB = json.load(f)

# 🔍 SMART SEARCH
def search_kb(query):
    query = query.lower()
    best_match = None
    best_score = 0

    for item in KB:
        score = fuzz.partial_ratio(query, item["question"])
        if score > best_score:
            best_score = score
            best_match = item

    if best_score > 60:
        return best_match["answer"]
    else:
        return "Sorry, no relevant answer found. Please contact support."

# 🚀 MAIN API
@app.get("/ask")
def ask(query: str):
    answer = search_kb(query)
    return {"answer": answer}
