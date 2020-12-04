# This Dockerfile is edited based on docker file in this repo: https://github.com/cclauss/Python2-and-Python3-in-Docker
# Starts with python:3.7.1-alpine and then installs most of python:2.7.15-alpine on top
# to allows us to choose Python versions at runtime via: python2, python3, pip2, pip3, etc.
ARG BASE_CONTAINER=sculpto/python2-and-3:latest
FROM $BASE_CONTAINER

#RUN pip install --no-cache-dir --upgrade pip
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

