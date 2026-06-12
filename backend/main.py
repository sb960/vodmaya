from fastapi import FastAPI

app = FastAPI(title="Vodmaya", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Vodmaya is running!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}