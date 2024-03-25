from fastapi import FastAPI

from app.celery_worker import send_msg

app = FastAPI()


@app.get("/start_task")
async def start_task():
    task = send_msg.delay(5, 5)
    return {"message": f"Task {task.id}"}
