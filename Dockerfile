FROM amd64/ubuntu
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
      telnet \
      tcpdump \
	libopencv-dev \
        python3-pip \
	python3-opencv && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps && \
    pip3 install opencv-python && \
    pip3 install imutils && \
    python3 -m pip install Django

RUN mkdir /it6272
COPY finalproject /it6272 
WORKDIR /it6272 
RUN cd /it6272 
EXPOSE 8080
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

