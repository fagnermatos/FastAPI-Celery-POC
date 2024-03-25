from fastapi import FastAPI

from app.celery_worker import send_msg

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/send")
async def say_hello(name: str):
    task = send_msg.delay(5, 5)
    return {"message": f"Hello {task.id}"}
