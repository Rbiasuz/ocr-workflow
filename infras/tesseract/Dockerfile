FROM ubuntu:20.04

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive


RUN apt-get update \
  && apt-get -y install tesseract-ocr \
  && apt-get install -y python3.9 python3-distutils python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN pip3 install pytesseract
RUN pip3 install numpy
RUN pip3 install flask
RUN pip3 install nltk
RUN pip3 install scikit-learn


EXPOSE 80

EXPOSE 5000