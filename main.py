from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Load your CSV file
df = pd.read_csv("catalog_data.csv")  # make sure the CSV is in the same folder

# FastAPI app
app = FastAPI()

# Input model
class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
def recommend_assessments(input: QueryInput):
    text = input.query.lower()

    # Very simple tag-matching logic
    matched = df[df["Tags"].str.contains("|".join(text.split()), case=False, na=False)]

    # If nothing matched, return a helpful message
    if matched.empty:
        return {"message": "No matching assessments found for your query."}

    return matched.to_dict(orient="records")
