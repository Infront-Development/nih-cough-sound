FROM python:3.8-alpine

USER root
RUN apk add python3 python3-dev g++ unixodbc-dev
RUN apk --no-cache add \
    build-base \
    python3-dev \
    python3-tkinter \
    # wget dependency
    openssl \
    # dev dependencies
    bash \
    git \
    meson \
    sudo \
    # Pillow dependencies
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    libimagequant-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

RUN python3 -m ensurepip
RUN pip3 install --user pyodbc

WORKDIR /code
COPY requirements.txt  /code
RUN pip install -r requirements.txt
COPY . /code
EXPOSE 8000
CMD [ "/bin/sh", "entrypoint_dev.sh" ]
