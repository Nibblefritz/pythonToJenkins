FROM python
RUN "apt update && apt install python3"
COPY ./PasswordGenerator.py /kfife/scripts/PasswordGenerator.py
WORKDIR /kfife/scripts
ENTRYPOINT ["python3", "./PasswordGenerator.py"]