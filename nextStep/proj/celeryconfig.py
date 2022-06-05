from xml.etree.ElementInclude import include


broker_url = 'redis://localhost:6379'
result_backend = 'mongodb://localhost:27017/'

include = ['proj.tasks']
task_serialzer = 'json'
result_serialzer = 'json'
accept_content = ['json']
timezone = 'Asia/Tehran'
enable_utc = True