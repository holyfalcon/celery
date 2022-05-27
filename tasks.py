from celery import Celery

app = Celery('tasks')

# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'json'
#
# app.conf.update(
#     task_serialzer = 'json',
#     result_serialzer = 'json',
#     accept_content = ['json'],
#     timezone = 'Asia/Tehran',
#     enable_utc = True
# )

app.config_from_object('celeryconfig')

@app.task
def add(x,y):
    return x + y

@app.task
def divide(x, y):
    return x / y