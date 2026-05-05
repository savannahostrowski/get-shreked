"""Get Shreked — static asset server on FastAPI Cloud."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
