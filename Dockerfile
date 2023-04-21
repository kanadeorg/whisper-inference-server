FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04
LABEL maintainer="me@kanade.org"

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    ffmpeg
WORKDIR /app
COPY requirements.txt requirements.txt
COPY model.pt model.pt
COPY tiktoken-cache tiktoken-cache
RUN pip install -r requirements.txt
COPY main.py main.py
CMD ["python3","./main.py"]
EXPOSE 5000
