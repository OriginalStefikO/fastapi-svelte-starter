import uvicorn
import sys

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

@app.get("/favicon.png", response_class=FileResponse)
async def favicon_png():
    return FileResponse("public/favicon.png")

@app.get("/favicon.ico", response_class=FileResponse)
async def favicon_ico():
    return FileResponse("public/favicon.png")


app.mount('/', StaticFiles(directory='public', html=True))

if __name__ == "__main__" and len(sys.argv) > 1:
    match sys.argv[1]:
        case 'dev' | "--dev" | "-d":
            print("dev")
            uvicorn.run("main:app", port=8002, reload=True)
        case _:
            uvicorn.run("main:app", port=8002)