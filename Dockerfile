FROM ubuntu:22.04

WORKDIR /app

RUN mkdir outputs

COPY . .

RUN apt install -y python3 python3-pip python3-opencv

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download ko_core_news_sm

RUN apt install -y libgl1-mesa-glx ffmpeg unzip

ADD https://huggingface.co/datasets/ij5/ace/resolve/main/assets.zip .

CMD ["python3", "app.py"]

