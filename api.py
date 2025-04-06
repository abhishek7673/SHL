from fastapi import FastAPI, Request
from recommender import SHLRecommender
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
recommender = SHLRecommender()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommend")
async def get_recommendations(request: Request):
    body = await request.json()
    query = body.get("query")
    results = recommender.recommend(query)
    return results.to_dict(orient="records")

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
