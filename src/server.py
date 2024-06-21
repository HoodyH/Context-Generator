from fastapi import FastAPI, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

from core.model import compute

app = FastAPI()

# Mount static html files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())


@app.post("/modify-quote/")
async def modify_quote(prompt: str = Form(...), file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode('utf-8')

    # Modify the text using OpenAI
    modified_content = compute(f'Modifica il seguente preventivo secondo queste istruzioni:\n{prompt}\nPreventivo:\n{content}')

    output_path = "modified_quote.txt"
    with open(output_path, "w") as output_file:
        output_file.write(modified_content)

    # Restituisci il file modificato come risposta
    return FileResponse(output_path, media_type='text/plain', filename='modified_quote.txt')