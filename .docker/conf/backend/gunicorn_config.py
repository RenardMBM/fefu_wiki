name = "fefu_wiki"
command= "/www/bin/gunicorn"
pythonpath = "/www/fefu_wiki"
bind = "0.0.0.0:8000"
workers = 3 # cores * 2 + 1
limit_request_fields = 3000
limit_request_field_size = 10
ram_env = "DJANGO_SETTINGS_MODULE=fefu_wiki.settings"