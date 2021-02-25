ARG BASE_CONTAINER=ubuntu:20.04
FROM $BASE_CONTAINER

RUN apt -y update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt -y install python3-pip

RUN apt -y install python2
RUN add-apt-repository universe
RUN apt -y install curl
RUN curl https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py
RUN python2 get-pip.py

RUN apt-get -y  install python-dev   
RUN apt-get -y install python3-dev

RUN apt -y install git

RUN python2 -V
RUN python3 -V
RUN pip3 --version
RUN pip2 --version

RUN pip3 install --no-cache-dir Cython
RUN pip3 install --no-cache-dir numpy
RUN pip3 install --no-cache-dir scipy
RUN pip3 install --no-cache-dir pandas
RUN pip3 install --no-cache-dir sqlalchemy 
RUN pip3 install --no-cache-dir statsmodels
RUN pip3 install --no-cache-dir h5py

RUN pip2 install --no-cache-dir bitarray
RUN pip2 install --no-cache-dir nose
RUN pip2 install --no-cache-dir pybedtools
RUN pip2 install --no-cache-dir scipy
RUN pip2 install --no-cache-dir pandas
RUN pip2 install --no-cache-dir numpy

