from fastapi import FastAPI, Form, UploadFile, File, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, StreamingResponse, RedirectResponse

from .core.model import compute
from .core.document import WordDocument

app = FastAPI()

# Mount static html files
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def website():
    """redirect to the main page on base url"""
    return RedirectResponse('/static/index.html', status_code=status.HTTP_302_FOUND)


@app.post("/modify")
async def modify(prompt: str = Form(...), file: UploadFile = File(...)):
    doc = WordDocument(file.file)

    # make openai request
    modified_content = compute(
        f'Modifica il seguente preventivo secondo queste istruzioni:\n{prompt}\nPreventivo:\n{doc.text}'
    )

    # build document for output
    buffer = doc.docx(modified_content)

    return StreamingResponse(
        buffer,
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        headers={'Content-Disposition': f'attachment; filename="modified_document.docx"'}
    )


@app.post("/create")
async def create(premessa: str = Form(...), costo: str = Form(...), dettaglio_tecnico: str = Form(...),
                 accordo_confidenziali: str = Form(...), contatti: str = Form(...)):

    # make openai request
    modified_content = compute(
        f'Crea un preventivo con queste sezioni:\n'
        f'Premessa: {premessa}\n'
        f'Dettagli Tecnici: {dettaglio_tecnico}\n'
        f'Sezione Costi: {costo}\n'
        f'Accordi Confidenziali: {accordo_confidenziali}\n'
        f'Contatti: {contatti}\n'
    )

    # build document for output
    buffer = WordDocument.docx(modified_content)

    return StreamingResponse(
        buffer,
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        headers={'Content-Disposition': f'attachment; filename="new_document.docx"'}
    )
