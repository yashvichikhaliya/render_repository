
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app= FastAPI()

images= "https://tse4.mm.bing.net/th/id/OIP.hXWwNOQw15ZVWKlMs-xv0wAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
@app.get("/")
def home():
    return{
        "Message":"Hello from FastAPI on Render.."
    }

@app.get("/users")
def get_users():
    return[
        {
            "name":"yashvi",
            "role":"Admin",
        },
        {
            "name":"sarthak",
            "role":"employee"
        }
    ]

@app.get("/img", response_class=HTMLResponse)
def get_img():
    return"""

    <h1>Image</h1>
    <img src={images} alt="sunflo0we"/>
    """
