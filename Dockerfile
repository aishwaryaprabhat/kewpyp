FROM python:3.6
MAINTAINER aish, aishwaryaprabhat@gmail.com
COPY requirements.txt kewpyp/
WORKDIR kewpyp/
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD python src/flask_app.py