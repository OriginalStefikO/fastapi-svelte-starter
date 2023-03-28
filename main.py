# import os
# os.chdir("frontend")
# os.system("npm run build")
# os.chdir("../")

from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import uvicorn

import random

app = FastAPI()

app.mount("/front", StaticFiles(directory="./dist", html=True), name="front")
app.mount("/build", StaticFiles(directory="./dist/assets"), name="build")

@app.get("/rand")
async def rand():
    return random.randint(0, 100)

@app.get('/')
async def front():
   return RedirectResponse(url='front', status_code=302)