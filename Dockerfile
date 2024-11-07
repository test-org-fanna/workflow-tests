# A very simple Dockerfile with secrets to test building and pushing
FROM python:3.11.10-alpine
ARG ARG_1=1
RUN --mount=type=secret,id=first \
    --mount=type=secret,id=second \
    echo $(cat /run/secrets/first) && \
    echo $(cat /run/secrets/second)
ENTRYPOINT ["sh", "-c"]
CMD ["trap 'exit' TERM; while true; do sleep ${ARG_1}; done"]