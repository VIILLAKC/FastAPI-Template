from celery import Celery, Task

celery_app = Celery("worker")

celery_app.conf.update(
    broker_url="redis://redis:6379/0",
    task_routes={
        "app.tasks.*": "main-queue",
    },
)