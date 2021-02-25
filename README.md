# Post-GWAS-bioannotation

# prerequisite 
- MetaXcan: https://github.com/hakyimlab/MetaXcan/blob/master/software/MulTiXcan.py
- H-MAGMA: https://github.com/thewonlab/H-MAGMA
- ldsc: https://github.com/bulik/ldsc 
  If you do not already have the above package setup and function well on your computer, first stpes is to set up two environment with python3 and python2 (Since ldsc is written in python2 while metaxcan is in python3). Normally, you can install python3 directly and create a new enviorment that has python2 in. 
  Recommended install Anaconda for creating new enviorment and install packages. https://docs.anaconda.com/anaconda/install/. 
  # Instruction for using Anaconda:
    download Anaconda for python3 (Anaconda3) first, and set the base enviorment with python3 to be your default enviorment as promoted
    Then create a new python2 enviorment with anaconda and install python2 in it. 
      - a good way to test if python2 and python3 is properly installed is by typing python (or python3 or python2,depends on how you set the name) in command line, and see if it open a python code terminal and allow you to type python code directly like :

      $python
      Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
      Type "help", "copyright", "credits" or "license" for more information.
      >>>1+1
      2
      >>>
  
  - Once you got the enviorments set up, clone github repository for MetaXcan and  H-MAGMA and ldsc locally(recommend using Github desktop if you are not familiar with commandline), and install all required package of MetaXcan in python3 enviorment, and all required packege for ldsc in python2 enviorment. 
  - for H-MAGMA, download MAGMA v1.08 https://ctg.cncr.nl/software/magma, and put into "Codes" folder of H-MAGMA

# install docker container
  $ docker pull floryhyy/postgwas
  $ docker run -dt --name my_postgwas floryhyy/postgwas
    b6a04200ad91000a93300c22c92a949c1297c15136da99551362b3d7fb747e98
  $ docker ps -a
    CONTAINER ID   IMAGE                  COMMAND       CREATED         STATUS                      PORTS                    NAMES
    b6a04200ad91   floryhyy/postgwas      "/bin/bash"   8 seconds ago   Up 7 seconds                                         my_postgwas
  #now you can execute command on the container
  $ docker exec -it my_postgwas bash
  root@b6a04200ad91:/#
  #Inside docker
  root@b6a04200ad91:/# cd ldsc

# LDSC sample data download:
  #Inside docker
  root@b6a04200ad91:/# cd ldsc
  
  #download data
  root@b6a04200ad91:/ldsc# wget https://data.broadinstitute.org/alkesgroup/LDSCORE/eur_w_ld_chr.tar.bz2
  root@b6a04200ad91:/ldsc# wget https://data.broadinstitute.org/alkesgroup/LDSCORE/w_hm3.snplist.bz2
  root@b6a04200ad91:/ldsc# tar -jxvf eur_w_ld_chr.tar.bz2
  root@b6a04200ad91:/ldsc# bunzip2 w_hm3.snplist.bz2
  root@b6a04200ad91:/ldsc# mkdir data
  #download gwas file
  
  The pgc file no longer allow direct download so you need to go to their website and fill a form to download manually OR you can use your own gwas file, but the below munge command will need modification
  https://www.med.unc.edu/pgc/download-results
  Alternative link to directly download sample pgc file: https://4119f3fb-a-f9436c1e-s-sites.googlegroups.com/a/broadinstitute.org/pgc-summer-school-2015/lecture-materials/pgc.cross.scz.zip

  Once gwas data is ready, open a new terminal on your computer and copy your gwas file into the docker container with command
  docker cp [filepath_to_your_gwas_file] [your docker container id, mine was my_postgwas]:ldsc/data
  Example: $ docker cp pgc.cross.SCZ17.2013-05.txt my_postgwas:lsdc   
  
#munge data
  go back to docker container and inside ldsc folder
  root@131c7182addc:/ldsc# mkdir sumstats
  root@131c7182addc:/ldsc# mkdir result
  root@131c7182addc:/ldsc# python2 munge_sumstats.py --sumstats data/pgc.cross.SCZ17.2013-05.txt --N 17115 --out sumstats/scz --merge-alleles w_hm3.snplist
  root@131c7182addc:/ldsc#   python2   ldsc.py --h2 sumstats/scz.sumstats.gz --ref-ld-chr eur_w_ld_chr/ --w-ld-chr eur_w_ld_chr/ --out result/scz_bip


  
