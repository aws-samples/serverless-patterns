FROM python:3.14-slim

ADD script.py /
ADD requirements.txt /
RUN pip install -r requirements.txt

CMD [ "python", "./script.py" ]