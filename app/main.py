from fastapi import FastAPI, status,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from Models import Posts
from random import randrange
import json
import uuid


def https_url_for(request:Request, name:str, **path_params:any)->str:
    http_url = request.url_for(name, **path_params)
    https_url =str(http_url).replace("http", "https", 1)
    return https_url#request.url_for(name, **path_params)


# def https_url_for(request:Request, name:str, **path_params:any)->str:
#     http_url = request.url_for(name, **path_params)
#     https_url =str(http_url).replace("http", "https", 1)
#     return request.url_for(name, **path_params)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.globals["https_url_for"] = https_url_for
with open('db.json') as file:
    posts = json.load(file)

posts = posts["posts"]



@app.get("/", response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse("index.html",{"request":request, "posts":posts} )


@app.post("/post",status_code=status.HTTP_201_CREATED)
async def create_post(post:Posts,request:Request):
    post = post.dict()
    post_id = uuid.uuid4().hex
    post["id"] = post_id
    posts.append(post)

    with open('db.json', "w") as file:
        json.dump(posts, file)


    return {"post":post}

@app.get("/post", response_class=HTMLResponse)
async def post(request:Request):

    return templates.TemplateResponse("post.html", {"request":request, "posts":posts})


@app.get("/post/{id}",response_class=HTMLResponse)
async def single(id:str, request:Request):
    post = next((p for p in posts if p["id"]==id),None)

    if post: 
        return templates.TemplateResponse("single.html", {"request":request, "post":post})
    
    else:
        return templates.TemplateResponse("404.html",{"request":request})
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} was not found")


@app.get("/about", response_class=HTMLResponse)

async def about(request:Request):
    return templates.TemplateResponse("about.html", {"request":request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request:Request):
    return templates.TemplateResponse("contact.html", {"request":request})


@app.get("/tutorial",response_class=HTMLResponse)
async def tutorial(request:Request):
    return templates.TemplateResponse("tutorial.html",{"request":request})

@app.get("/maintuto",response_class=HTMLResponse)
async def tutorial(request:Request):
    return templates.TemplateResponse("side_bar.html",{"request":request})

@app.get("/myCV")
async def cv(request:Request):
    return templates.TemplateResponse("cv.html",{"request":request})


@app.get("/filmReview", response_class=HTMLResponse)
async def filmReview(request:Request):
    return templates.TemplateResponse("french_film_reviews.html", {"request":request})
    


