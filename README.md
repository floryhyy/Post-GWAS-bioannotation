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
        b6a04200ad91   floryhyy/postgwas      "/bin/bash"   8 seconds ago   Up 7 seconds                                         postgwas
        $ docker exec -it postgwas bash
        root@b6a04200ad91:/#
        
        if encounter this error:
        $ docker exec -it postgwas bash                                                                                        
        Error response from daemon: Container 153a8260ec95c9b52e557d29821144cbeed544be438ebb891956550da6e30e2d is not running   (base) 
        Run $ docker start postgwas
        
  - if you need to update the docker image, delet the old one first, then repeat the above commend
  - command for deleting:
      
        $ docker container rm postgwas  
        $ docker image rm floryhyy/postgwas  

# Extra data for packages download:
  - Inside docker
        
        root@b6a04200ad91:/# cd home
  
  - download data for MetaXcan
  
        root@153a8260ec95:/home# cd MetaXcan/software/data
        root@153a8260ec95:/home/MetaXcan/software/data# wget https://zenodo.org/record/3519321/files/gtex_v8_expression_elastic_net_snp_smultixcan_covariance.txt.gz
        #check if data download successfully:
        root@153a8260ec95:/home/MetaXcan/software/data# ls                                                                      gtex_v8_expression_elastic_net_snp_smultixcan_covariance.txt.gz 
        #download Models
        root@153a8260ec95:/home/MetaXcan/software/data# wget https://zenodo.org/record/3519321/files/elastic_net_eqtl.tar
        root@153a8260ec95:/home/MetaXcan/software/data# tar -xvf elastic_net_eqtl.tar
        root@153a8260ec95:/home/MetaXcan/software/data# mv elastic_net_models/ Models 
        
        #remove extra file, this step is not required.
        root@153a8260ec95:/home/MetaXcan/software/data# rm elastic_net_eqtl.tar  
        root@153a8260ec95:/home/MetaXcan/software/data# cd Models/ 
        # keep only brain tissues
        root@153a8260ec95:/home/MetaXcan/software/data/Models# rm en_[^B]*
        root@153a8260ec95:/home/MetaXcan/software/data/Models# rm en_Brea*       
        
    - dowload data for HMAGMA
    -   
        
        
        
        
        
        
        
        
        
 
  
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


  
