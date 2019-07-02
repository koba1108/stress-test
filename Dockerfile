FROM python:2.7.8

RUN apt-get install libevent-dev
RUN pip install --upgrade cython
RUN pip install --upgrade setuptools
RUN pip install --upgrade pyzmq
RUN pip install --upgrade greenlet
RUN pip install --upgrade locustio

EXPOSE 5557 5558 8089

ADD locust-tasks /locust-tasks
# RUN pip install -r /locust-tasks/requirements.txt
RUN chmod 755 /locust-tasks/run.sh

ENTRYPOINT ["/locust-tasks/run.sh"]
