FROM python:3.11-slim

RUN pip3 install Flask
# RUN pip3 install google-cloud-firestore
RUN pip3 install google-cloud-logging
RUN pip3 install langchain
RUN pip3 install requests
RUN pip3 install waitress

ARG FILENAME
ARG PORT

ENV FILENAME ${FILENAME}
ENV PORT ${PORT}

COPY ${FILENAME}.py ./

RUN echo $FILENAME $PORT

CMD sh -c "waitress-serve --listen=0.0.0.0:${PORT} ${FILENAME}:app"

# COPY sidecar.py ./
# ENV PORT=5000
# CMD exec waitress-serve --listen=0.0.0.0:$PORT sidecar:app

# COPY foo.py ./
# ENV PORT=8080
# CMD exec waitress-serve --listen=0.0.0.0:$PORT foo:app