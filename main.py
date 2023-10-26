from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    name = "Thomas Hermanu"
    skillsList = ["HTML","CSS","JavaScript"]
    return templates.TemplateResponse("index.html", {"request": request, "name": name, "skillsList": skillsList})

@app.get("/contact", response_class=HTMLResponse)
async def get_form(request: Request): 
    return templates.TemplateResponse("contact.html", {"request": request })

@app.post("/contact", response_class=HTMLResponse)
async def post_data(request: Request): 
    return templates.TemplateResponse("response.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)