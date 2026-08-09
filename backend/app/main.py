from fastapi import FastAPI

app = FastAPI(title = "Group Calendar API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

