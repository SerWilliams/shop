from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from api import router


app = FastAPI(
    title='Shop',
    version='1.0.0'
)

template = Jinja2Templates(directory="template")
app.mount("/extjs", StaticFiles(directory="e:\\Work\\ext-7.0.0"), name="extjs")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})
