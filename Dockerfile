FROM python:alpine3.7

RUN pip install flask


COPY . /app
WORKDIR /app

EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [  "./MainScores.py" ]