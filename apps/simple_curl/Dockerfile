FROM alpine:latest

WORKDIR /app

COPY . .

RUN chmod +x script.sh

RUN apk --no-cache add curl

ENV TARGET_ENDPOINT_URL="http://localhost/api/v1/hello"

CMD ["./script.sh"]
