FROM python:3

ENV HTTP_PROXY="http://www-proxy.statoil.no:80"
ENV HTTPS_PROXY=$HTTP_PROXY
ENV NO_PROXY="localhost,127.0.0.1,puppet.sdp.statoil.no"
COPY ./src /app

RUN pip install -r /app/requirements.txt

CMD python3 /app/app.py
