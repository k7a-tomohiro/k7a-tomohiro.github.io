FROM debian:stable-slim AS downloader
RUN apt update \
    && apt install -y curl \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
RUN curl -L https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.$(uname -m) -o /tmp/ttyd


FROM debian:stable-slim
COPY --from=downloader --chmod=0755 /tmp/ttyd /usr/local/bin/ttyd
EXPOSE 7681
ENTRYPOINT ["/usr/local/bin/ttyd"]
CMD ["--writable", "bash"]
