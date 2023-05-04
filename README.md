# How to setup Fastapi with Svelte

## Without any additional setup:

<details>
  <summary>Click here to expand</summary>

1. Clone this repository

```git
git clone https://github.com/OriginalStefikO/fastapi-svelte-starter.git .
```

2. Create Python virtual enviroment (further just venv)(optional, but will prevent some unexpected errors)
    - when you restart your workspace you will need to activate it again, just run the second line

> first we create venv from our python installation
```cmd
~\AppData\Local\Programs\Python\Python311\python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt #Here are just
```
> after that we activate it and install needed dependencies

3. Get all svelte packages
```cmd
cd ./frontend
npm install
cd ../
```

4. Build svelte and run fastapi with uvicorn
```cmd
cd ./frontend
npm run build; cd ../
uvicorn main:app --reload
```
5. When developing in Svelte, you can use dev server
```cmd
npm run dev
```
 
</details>

# My way of setting up **Fastapi + Svelte** Hello world (1Q2023)

## How to setup **[FasAPI](https://fastapi.tiangolo.com)** with **[Svelte](https://svelte.dev)** using **Vite**

#### This repo is just me trying to setup Fastapi with Svelte, I'm no expert and I just started, I just did't find any updated tutorials for this, so I made my own.

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
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
 
app = FastAPI()

# Define our static folder, where will be our svelte build later
app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

# Simply the root will return our Svelte build
@app.get("/", response_class=FileResponse)
async def main():
    return "public/index.html"
```

3. Download dependencies
    - Make sure your venv is activate, if not activate it
    - it may ask you to install autopep8, type yes

```
pip install fastapi
pip install "uvicorn[standard]"
```

4. Run the Fastapi with uvicorn (not now, it won't work, we are missing frontend)
```cmd
uvicorn main:app --reload
```

### <ins> Setting up Svelte with Vite </ins>

1. Start by initializing Vite:
   - Choose the following options:
   - Package name: `frontend`
   - Install packages: `yes`
   - Template: `Svelte`
   - Typescript: `TS` I recommend typescript, you won't hate your life later haha

```cmd
npm init vite;
cd frontend;
npm install
```

2. Now it still won't work, we need to edit config first
   - find vite.config.ts
   - I made two scripts, the easy one and the better one, the second will make your life easier I think

```ts
export default defineConfig({
   plugins: [svelte()],
   base: './',
   build: { 
      outDir: '../public',
      assetsDir: 'assets',
      emptyOutDir: true,
   },
})
```

```ts
export default defineConfig({
   plugins: [svelte()],
   base: "./", // This will make paths relative
   build: {
      emptyOutDir: true,
      outDir: '../public', // Where we want to put the build
      assetsDir: 'assets', // This will be folder inside the public
      rollupOptions: {
         input: {
            main: './index.html', // This index.html will be in public folder
            // if you have more pages, just add them bellow like this:
            // example: './pages/example.html',
         },
         output: {
            entryFileNames: 'assets/js/[name]-[hash].js', // Here we put all js files into js folder
            chunkFileNames: 'assets/js/[name]-[hash].js',
            // But after that we need to define which files should go where with regex
            assetFileNames: ({ name }) => {
               if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
                  return 'assets/images/[name].[ext]';
               }

               if (/\.css$/.test(name ?? '')) {
                  return 'assets/css/[name]-[hash].[ext]';
               }

               return 'assets/[name]-[hash].[ext]';
            },
         }
      }     
   }
})
```

> When we build our app now, it will build it to "public" folder and the files should be in their correct subfolders

***

> When you want to run or build svelte, just run one of those in ./frontend
```cmd
npm run dev
npm run build
```

> and as I said before, to run fastapi, run
```cmd
uvicorn main:app --reload
```

### That's it! You should now have a fully functional application with a FastAPI backend and Svelte frontend. Of course, this is just a starting point and you can customize and add to it as needed for your own projects.
