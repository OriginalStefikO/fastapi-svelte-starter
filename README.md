# ProjectGallery

## How to setup **[FasAPI](https://fastapi.tiangolo.com)** with **[Svelte](https://svelte.dev)** or [React](https://react.dev) using **Vite**

#### This repo is just me trying to setup Fastapi with Svelte and doing small project with one of them, I'm no expert and I just started, I just did't find any updated tutorial for this so I made my own.

### <ins> Setting up Fastapi </ins>

1. Create Python Virtual Enviroment (further just venv)
    - this will make our life easier
    - when you restart your workspace you will need to activate it again, just run the second line

> first we create venv from our python installation
```
~\AppData\Local\Programs\Python\Python311\python -m venv venv

venv\Scripts\activate
```
> after that we activate it

2. Create main.py
```py
from typing import Union
from fastapi import FastAPI

# we need these to get files from server
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()

# Here we mount our index.html that will be our build in dist forlder to /front
app.mount("/front", StaticFiles(directory="./dist", html=True), name="front")
# And here all the other files like css and js that is in assets folder
app.mount("/build", StaticFiles(directory="./dist/assets"), name="build")

# When you land in root it will redirect you to index.html
@app.get('/')
async def front():
   return RedirectResponse(url='front', status_code=302)
```

3. Download dependencies
    - Make sure your venv is activate, if not activate it
    - it may ask you to install autopep8, type yes

```
pip install fastapi
pip install "uvicorn[standard]"
```

4. Run the Fastapi server (not now, it won't work, we are missing frontend)
```cmd
uvicorn main:app --reload
```

### <ins> Setting up Svelte or React with Vite </ins>

1. We start with initializing Vite
    - choose the things in comments, if you want React, just choose React

```cmd
npm init vite;
# (Package name)     frontend
# (install packages) yes
# (Template)         Svelte
# (Typescript)       you can choose TS or JS, it depends on your preferences
cd frontend;
npm install
```

2. Now it still won't work, we need to edit config first
    - find vite.config.js (or ts)

```js
export default defineConfig({
  plugins: [react()],
  base: './',
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
})
```
> When we build our app now, it will build it to dist folder in root and by changing **base: './'** the files in index.html won't be static but relative

<br>

> When you want to run or build svelte, just run one of those in ./frontend
```cmd
npm run dev
npm run build
```

> and as I said before, to run fastapi, run
```cmd
uvicorn main:app --reload
```

### If you have any suggestion for change or notice a mistake, just notify me or something, I hope this will help you when starting with svelte or React