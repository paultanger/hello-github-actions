FROM python:3

ADD action-c/entrypoint.sh entrypoint.sh
ADD test_example.py test_example.py
RUN chmod +x entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]