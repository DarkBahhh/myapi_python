FROM debian

LABEL hub_url="darkbahhh/myapi-frontend"

WORKDIR /usr/bin/
COPY --chown=root:root ./api.py ./

ENV API_BACKEND_URL myapi-backend
ENV API_BACKEND_PORT 8001

RUN apt-get update -y && apt-get install -y python-requests python-flask
EXPOSE 8000
CMD ./api.py
