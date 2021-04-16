# Post-GWAS-bioannotation

# install docker container
  - download and install docker desktop
  
    https://www.docker.com/get-started
    
    (after installation it may ask you to register a docker account, I am not sure if this step is necessary, you can try skip it)
    
    There will be some tutorial after installation, you can just ignore those
    
  - open a terminal open you computer and input following command:
    
        $ docker pull floryhyy/postgwas
        $ docker run -dt --name postgwas floryhyy/postgwas
        b6a04200ad91000a93300c22c92a949c1297c15136da99551362b3d7fb747e98
        $ docker ps -a
        CONTAINER ID   IMAGE                  COMMAND       CREATED         STATUS                      PORTS                    NAMES
        b6a04200ad91   floryhyy/postgwas      "/bin/bash"   8 seconds ago   Up 7 seconds                                         my_postgwas
        $ docker exec -it my_postgwas bash
        root@b6a04200ad91:/#
        
  - if you need to update the docker image, delet the old one first, then repeat the above commend
  - command for deleting:
      
        $ docker container rm postgwas  
        $ docker image rm floryhyy/postgwas  

# LDSC sample data download:
  - Inside docker
        
        root@b6a04200ad91:/# cd ldsc
  
  - download data
 
        root@b6a04200ad91:/ldsc# wget https://data.broadinstitute.org/alkesgroup/LDSCORE/eur_w_ld_chr.tar.bz2
        root@b6a04200ad91:/ldsc# wget https://data.broadinstitute.org/alkesgroup/LDSCORE/w_hm3.snplist.bz2
        root@b6a04200ad91:/ldsc# tar -jxvf eur_w_ld_chr.tar.bz2
        root@b6a04200ad91:/ldsc# bunzip2 w_hm3.snplist.bz2
        root@b6a04200ad91:/ldsc# mkdir data
  
  - download gwas file on your computer(not in docker container)
 
  The pgc file no longer allow direct download so you need to go to their website and fill a form to download manually OR you can use your own gwas file, but the below munge command will need modification
  
  https://www.med.unc.edu/pgc/download-results
  
  Alternative link to directly download sample pgc file: https://4119f3fb-a-f9436c1e-s-sites.googlegroups.com/a/broadinstitute.org/pgc-summer-school-2015/lecture-materials/pgc.cross.scz.zip

  - Once gwas data is ready, open a new terminal on your computer and copy your gwas file into the docker container with command
  
        $ docker cp [filepath_to_your_gwas_file] [your docker container id, mine was my_postgwas]:ldsc/data
  
  Example: $ docker cp pgc.cross.SCZ17.2013-05.txt my_postgwas:lsdc   
  
# munge data and get heritability score
  - go back to docker container and inside ldsc folder

        root@131c7182addc:/ldsc# mkdir sumstats
        root@131c7182addc:/ldsc# mkdir result
        root@131c7182addc:/ldsc# python2 munge_sumstats.py --sumstats data/pgc.cross.SCZ17.2013-05.txt --N 17115 --out sumstats/scz --merge-alleles w_hm3.snplist
        root@131c7182addc:/ldsc#   python2   ldsc.py --h2 sumstats/scz.sumstats.gz --ref-ld-chr eur_w_ld_chr/ --w-ld-chr eur_w_ld_chr/ --out result/scz_bip


  
