FROM python:3
WORKDIR /home/demo

COPY main.py .

RUN chmod +x main.py && python3 ./main.py unzip

EXPOSE 8080

# CMD ["python3", "main.py"]
CMD ["python3", "main.py","web"]

USER 10001
