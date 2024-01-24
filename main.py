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

if __name__ == "__main__":
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "dev" | "--dev" | "-d" | "development":
                print("Development")
                uvicorn.run("main:app", port=8080, reload=True)
    else:
        print("Production")
        uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=False)