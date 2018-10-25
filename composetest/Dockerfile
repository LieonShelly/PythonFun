FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
# CMD ["python3", "app.py"]