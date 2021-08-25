FROM python:3
COPY ./PasswordGenerator.py /kfife/scripts/PasswordGenerator.py
WORKDIR /kfife/scripts
ENTRYPOINT ["python3", "./PasswordGenerator.py"]