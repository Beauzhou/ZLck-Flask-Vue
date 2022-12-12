FROM python:3.8

RUN mkdir -p /home/flask/app
WORKDIR /home/flask/app

ADD ./requirements.txt /home/flask/app/requirements.txt

RUN pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

ADD . /home/flask/app
CMD python app.py runserver -h 0.0.0.0

EXPOSE 5000
