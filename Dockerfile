FROM python:3.10-alpine

RUN if [ $(arch) == "aarch64" ]; \
    then export ARCH=arm64; \
    else export ARCH=amd64; \
    fi; wget "https://github.com/linkerd/linkerd-await/releases/download/release%2Fv0.2.4/linkerd-await-v0.2.4-$ARCH" -O linkerd-await; \
    chmod +x linkerd-await && mv linkerd-await /bin

RUN pip install requests falcon

WORKDIR /app
COPY client.py server.py /app/

ENTRYPOINT [ "linkerd-await", "--" ]
CMD [ "python", "server.py" ]
