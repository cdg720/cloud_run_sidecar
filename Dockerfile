FROM python:3.11-slim

RUN pip3 install Flask
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
