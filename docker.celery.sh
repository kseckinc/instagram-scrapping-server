# #!/bin/sh -ex
celery --app=core worker \
            --loglevel=INFO \
            # --uid=nobody --gid=nogroup


# #!/bin/sh -ex
# celery -A core worker --loglevel=info &
# # celery -A core beat --pidfile= -l info -S django &
# tail -f /dev/null

