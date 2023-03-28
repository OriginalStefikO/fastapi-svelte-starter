#region Here you can automatically build the frontend when the backend is started
# import os
# os.chdir("./frontend")
# os.system("npm run build")
# os.chdir("../")
#endregion

from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import uvicorn

import random

app = FastAPI()

app.mount("/front", StaticFiles(directory="./dist", html=True), name="front")
app.mount("/build", StaticFiles(directory="./dist/assets"), name="build")

@app.get('/')
async def front():
   return RedirectResponse(url='front', status_code=302)