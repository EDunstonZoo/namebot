FROM python:3.8.12-slim
RUN pip install --upgrade pip==20.2
RUN pip install rasa
RUN pip install sanic==21.9.3
RUN python -m  pip install spacy
RUN python -m spacy download en_core_web_md
WORKDIR /app
COPY . .

RUN rasa train nlu

# Set user
USER 1001

# Set entrypoint for interactive shells
ENTRYPOINT ["rasa"]

# command to run when container is called
CMD ["run", "--enable-api", "--port", "8080"]


