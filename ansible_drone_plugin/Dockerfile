FROM python:3.6
RUN pip install --upgrade pip
RUN pip install ansible
COPY entrypoint.sh /tmp/
WORKDIR /drone/
ENTRYPOINT [ "bash", "/tmp/entrypoint.sh" ]
