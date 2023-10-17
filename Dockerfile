FROM python:3.10.13
ENV PYTHONUNBUFFERED=1
RUN git clone https://github.com/Paillat-dev/Voiceping.git
RUN pip install -r /Voiceping/requirements.txt
WORKDIR /Voiceping
RUN adduser -u 4587 --disabled-password --gecos "" appuser && chown -R appuser /Voiceping
USER appuser
CMD ["python", "main.py"]