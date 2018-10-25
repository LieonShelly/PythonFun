# Use an official Python runtime as a parent image
FROM python:3.6
ADD . /Blog
WORKDIR /Blog
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
# CMD [ "gunicorn", "-c", "gunicorn.conf", "run:app"]
# CMD [ "python3", "run.py" ]