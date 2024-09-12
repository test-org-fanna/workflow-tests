FROM python:3.11.10-alpine
RUN --mount=type=secret,id=first \
    --mount=type=secret,id=second \

RUN cat /run/secrets/first | echo
RUN cat /run/secrets/second | echo

CMD sh -c 'trap "exit" TERM; while true; do sleep 1; done'