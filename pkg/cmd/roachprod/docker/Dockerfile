FROM golang:1.18.8
WORKDIR /build
COPY . .
RUN ["/build/build.sh"]
ENTRYPOINT ["/build/entrypoint.sh"]
