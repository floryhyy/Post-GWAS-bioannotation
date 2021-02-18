ARG BASE_CONTAINER=ubuntu:20.04
FROM $BASE_CONTAINER

RUN apt -y update
RUN apt -y install python2
RUN apt -y install python2-pip

RUN pip2 install --no-cache-dir bitarray

RUN pip install --no-cache-dir --upgrade pip
#RUN pip3 install --no-cache-dir Cython
RUN pip install --no-cache-dir numpy
RUN pip install --no-cache-dir scipy
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir sqlalchemy 
RUN pip install --no-cache-dir statsmodels
RUN pip install --no-cache-dir h5py

RUN pip2 install --no-cache-dir bitarray
RUN pip2 install --no-cache-dir nose
RUN pip2 install --no-cache-dir pybedtools
RUN pip2 install --no-cache-dir scipy
RUN pip2 install --no-cache-dir pandas
RUN pip2 install --no-cache-dir numpy

