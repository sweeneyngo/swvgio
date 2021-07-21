#!/bin/sh
echo '> Executing task: docker-build <'
echo '> docker build --rm --pull -f "/home/misu/.code/swvgio/Dockerfile" --label "com.microsoft.created-by=visual-studio-code" -t "swvgio:latest" "/home/misu/.code/swvgio" <'
docker build --rm --pull -f "/home/misu/.code/swvgio/Dockerfile" --label "com.microsoft.created-by=visual-studio-code" -t "swvgio:latest" "/home/misu/.code/swvgio/"
