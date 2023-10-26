from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Thomas Hermanu"
    skill1 = "HTML"
    skill2 = "CSS"
    skill3 = "JavaScript"
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skill1": skill1, "skill2":skill2, "skill3": skill3})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)