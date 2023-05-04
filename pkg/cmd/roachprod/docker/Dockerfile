FROM golang:1.19.8
WORKDIR /build
COPY . .
RUN ["/build/build.sh"]
ENTRYPOINT ["/build/entrypoint.sh"]
