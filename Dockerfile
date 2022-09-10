FROM ubuntu
RUN apt update -y && apt dist-upgrade -y;apt install python3 python3-pip -y
RUN pip3 install flask
COPY prog_lang_app.py /app/prog_lang_app.py
ENV  FLASK_APP=/app/prog_lang_app.py
EXPOSE 3000
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0", "-p", "3000"]
