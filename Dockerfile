FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

WORKDIR /app

RUN mkdir outputs

COPY . .

RUN apt update

RUN apt install -y python3 python3-pip python3-opencv

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download ko_core_news_sm

RUN apt install -y libgl1-mesa-glx ffmpeg unzip

ADD https://huggingface.co/datasets/ij5/ace/resolve/main/assets.zip .

RUN mkdir assets

RUN unzip assets/assets.zip -d assets/

CMD ["python3", "app.py"]

