# SHL Assessment Recommendation Engine

## What It Does
Given a natural language query or job description, this app recommends up to 10 relevant SHL assessments from the SHL product catalog.

## Features
- Natural language understanding via scikit-learn vector
- Streamlit web app for demo
- FastAPI endpoint for programmatic access

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
# OR
uvicorn api:app --reload
```

## Example Query (for API)

```json
{
  "query": "Looking for a software engineer with coding and analytical skills"
}
```
Response includes:
- Coding Skills Assessment
- Cognitive Ability Test (along with links and all different columns)
