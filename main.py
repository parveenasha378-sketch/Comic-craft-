from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI(title="ComicCraft - AI Comic Story Creator")

os.makedirs("app/static/panels", exist_ok=True)
os.makedirs("app/static/exports", exist_ok=True)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}