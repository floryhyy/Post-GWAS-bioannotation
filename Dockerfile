ARG BASE_CONTAINER=ubuntu:20.04
FROM $BASE_CONTAINER

RUN apt -y update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt -y install python3-pip

RUN apt -y install python2
RUN add-apt-repository universe
RUN apt -y install curl
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
RUN python2 get-pip.py

RUN apt-get -y  install python-dev   
RUN apt-get -y install python3-dev
RUN apt-get -y install wget

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
RUN cd home
RUN git clone https://github.com/bulik/ldsc.git
RUN cd ldsc
RUN wget https://data.broadinstitute.org/alkesgroup/LDSCORE/eur_w_ld_chr.tar.bz2
RUN wget https://data.broadinstitute.org/alkesgroup/LDSCORE/w_hm3.snplist.bz2
RUN tar -jxvf eur_w_ld_chr.tar.bz2
RUN bunzip2 w_hm3.snplist.bz2
RUN mkdir data
RUN cd ..
RUN git clone https://github.com/hakyimlab/MetaXcan
RUN cd MetaXcan/software
RUN mkdir data
RUN cd data
RUN wget https://zenodo.org/record/3519321/files/gtex_v8_expression_elastic_net_snp_smultixcan_covariance.txt.gz?download=1
RUN wget https://zenodo.org/record/3519321/files/elastic_net_eqtl.tar?download=1

