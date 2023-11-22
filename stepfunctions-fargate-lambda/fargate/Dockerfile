FROM python:3.8-slim-buster

ADD script.py /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "python", "./script.py" ]