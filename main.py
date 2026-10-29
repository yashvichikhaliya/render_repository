from fastapi import FastAPI

app= FastAPI()
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