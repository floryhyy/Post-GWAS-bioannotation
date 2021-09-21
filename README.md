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

# Download supplemental data:
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
        
  - dowload data for HMAGMA
        
        root@153a8260ec95:/home/H-MAGMA# cd Codes/ 
        root@153a8260ec95:/home/H-MAGMA/Codes# wget https://ctg.cncr.nl/software/MAGMA/prog/magma_v1.09a.zip  
        root@153a8260ec95:/home/H-MAGMA/Codes# unzip magma_v1.09a.zip   
        root@153a8260ec95:/home/H-MAGMA/Codes# wget https://ctg.cncr.nl/software/MAGMA/ref_data/g1000_eur.zip 
        root@153a8260ec95:/home/H-MAGMA/Codes# unzip g1000_eur.zip    
  
  - download gwas file on your computer
 
    I am using sample data (chr1.assoc.dosage)from MEtaXcan's readme : https://s3.amazonaws.com/imlab-open/Data/MetaXcan/sample_data/GWAS.tar.gz . But any gwas file would work.
    
  - Once gwas data is ready, open a new terminal on your computer and copy your gwas file into the docker container with command
  
        $ docker cp [filepath_to_your_gwas_file] [your docker container id, mine was my_postgwas]:ldsc/data
  
  Example: $ docker cp chr1.assoc.dosage postgwas:lsdc   
  
# Clone this repostiory and run analysis:
  - In the docker container's /home folder, clone this repository:
  
      root@153a8260ec95:/home# git clone https://github.com/floryhyy/Post-GWAS-bioannotation.git
      root@153a8260ec95:/home# cd Post-GWAS-bioannotation
      root@153a8260ec95:/home/Post-GWAS-bioannotation# cd results/                                                            
      root@153a8260ec95:/home/Post-GWAS-bioannotation/results# mkdir hmagma
      root@153a8260ec95:/home/Post-GWAS-bioannotation/results# cd ..
      
  - To run analysis, use command: 'bash analysis.sh [snp col name] [beta col name] [z col name] [p value col name] [effect allele col name][ non-effect allele col name] [ncol name] [n] [column to be ignore] [gwas file name], for value that your file do not have, put 999. (Only z_col,ncol, and ignore col can be 999).
      Example:
      
      root@153a8260ec95:/home/Post-GWAS-bioannotation# bash analysis.sh SNP BETA 999 P A1 A2 999 387649 999 chr1.assoc.dosage 
      
  - To update analysis code:
      
      root@153a8260ec95:/home/Post-GWAS-bioannotation# git pull
      
  
  
# munge data and get heritability score
  - go back to docker container and inside ldsc folder

        root@131c7182addc:/ldsc# mkdir sumstats
        root@131c7182addc:/ldsc# mkdir result
        root@131c7182addc:/ldsc# python2 munge_sumstats.py --sumstats data/pgc.cross.SCZ17.2013-05.txt --N 17115 --out sumstats/scz --merge-alleles w_hm3.snplist
        root@131c7182addc:/ldsc#   python2   ldsc.py --h2 sumstats/scz.sumstats.gz --ref-ld-chr eur_w_ld_chr/ --w-ld-chr eur_w_ld_chr/ --out result/scz_bip


  
