FROM python:2.7.8

RUN apt-get install libevent-dev
RUN pip install --upgrade cython setuptools pyzmq greenlet
RUN pip install locustio

EXPOSE 5557 5558 8089

ADD locust-tasks /locust-tasks
RUN chmod 755 /locust-tasks/run.sh

ENTRYPOINT ["/locust-tasks/run.sh"]
