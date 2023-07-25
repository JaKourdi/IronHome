FROM python:3.10-alpine3.15
RUN pip install --upgrade pip

RUN adduser -D appuser
USER appuser
WORKDIR /app

ENV PATH="/app/.local/bin:${PATH}"
ENV FLASK_APP=app

COPY --chown=appuser:appuser . .
RUN pip install --user -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]