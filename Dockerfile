# syntax=docker/dockerfile:1
FROM alpine
RUN --mount=type=secret,id=first,env=FIRST_ENV \
    --mount=type=secret,id=second,env=SECOND_ENV
ENTRYPOINT ["sh", "-c"]
CMD ["trap 'exit' TERM; while true; do sleep 1; done"]