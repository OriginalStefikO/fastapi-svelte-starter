from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

@app.get("/", response_class=FileResponse)
async def main():
    return "public/index.html"


@app.get("/example", response_class=FileResponse)
async def main():
    return "public/pages/example.html"
 