FROM debian

LABEL hub_url="darkbahhh/myapi-backend"

WORKDIR /usr/bin/
COPY --chown=root:root ./api.py ./
COPY --chown=root:root ./data.txt ./

RUN apt-get update -y && apt-get install -y python-requests python-flask
ENV API_DATA_PATH ./data.txt
EXPOSE 8001
CMD api.py
