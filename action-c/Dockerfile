FROM python:3

ADD entrypoint.sh /entrypoint.sh
COPY . .
# RUN python test_example.py
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]