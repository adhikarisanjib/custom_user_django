import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
app = Celery("project")
app.conf.update(timezone="Asia/Kathmandu")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "delete-unused-rooms": {
        "task": "school.tasks.remove_unwanted_rooms",
        "schedule": crontab(hour=15, minute=0),
        "args": ("Scheduled task done.",),
    }
}

app.autodiscover_tasks()
