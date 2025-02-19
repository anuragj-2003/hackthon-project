# /home/lenovo/Videos/hackathon-project/backend/main.py
from fastapi import FastAPI
from api import hm_routes, teacher_routes, student_routes

app = FastAPI()

app.include_router(hm_routes.router)
app.include_router(teacher_routes.router)
app.include_router(student_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Management System"}

@app.on_event("startup")
def show_routes():
    for route in app.routes:
        print(f"Path: {route.path}, Name: {route.name}")
