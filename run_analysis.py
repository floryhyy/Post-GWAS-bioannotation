import re
import sys
def spredxcan(current_path,filename,snp,beta,z,p,a1,a2):
    data_folder = current_path+'/data'
    smulti_output = current_path+'/results/SMultiXcan_Brain_v8_'+re.sub('(?<=\.).+','',filename)+'csv'

    command = './MetaXcan.py --model_db_path data/Models/en_Brain_Amygdala.db --covariance data/Models/en_Brain_Amygdala.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Amygdala.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Anterior_cingulate_cortex_BA24.db --covariance data/Models/en_Brain_Anterior_cingulate_cortex_BA24.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Anterior_cingulate_cortex_BA24.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Caudate_basal_ganglia.db --covariance data/Models/en_Brain_Caudate_basal_ganglia.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Caudate_basal_ganglia.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Cerebellar_Hemisphere.db --covariance data/Models/en_Brain_Cerebellar_Hemisphere.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Cerebellar_Hemisphere.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Hypothalamus.db --covariance data/Models/en_Brain_Hypothalamus.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Hypothalamus.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Cerebellum.db --covariance data/Models/en_Brain_Cerebellum.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Cerebellum.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Cortex.db --covariance data/Models/en_Brain_Cortex.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Cortex.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Frontal_Cortex_BA9.db --covariance data/Models/en_Brain_Frontal_Cortex_BA9.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Frontal_Cortex_BA9.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Hippocampus.db --covariance data/Models/en_Brain_Hippocampus.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Hippocampus.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Nucleus_accumbens_basal_ganglia.db --covariance data/Models/en_Brain_Nucleus_accumbens_basal_ganglia.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Nucleus_accumbens_basal_ganglia.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Putamen_basal_ganglia.db --covariance data/Models/en_Brain_Putamen_basal_ganglia.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Putamen_basal_ganglia.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Spinal_cord_cervical_c-1.db --covariance data/Models/en_Brain_Spinal_cord_cervical_c-1.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Spinal_cord_cervical_c-1.csv && ./MetaXcan.py --model_db_path data/Models/en_Brain_Substantia_nigra.db --covariance data/Models/en_Brain_Substantia_nigra.txt.gz --gwas_file ".*gz" --snp_column snpid --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column pvalue --output_file results/en_Brain_Substantia_nigra.csv'
    code = 'python3 SMulTiXcan.py --models_folder data/Models --models_name_filter en_Brain_.*db --models_name_pattern "en_Brain_(.*).db" --snp_covariance data/gtex_v8_expression_elastic_net_snp_smultixcan_covariance.txt.gz --metaxcan_folder results --metaxcan_filter ".*csv" --metaxcan_file_name_parse_pattern "en_Brain_(.*).csv" --gwas_file ".*gz" --snp_column SNP --non_effect_allele_column A2 --effect_allele_column A1 --beta_column beta --pvalue_column P --cutoff_condition_number 30 --verbosity 1 --throw --output '
    code=code + smulti_output
    command =command +' && '+code
    command = re.sub('snpid',snp,command)
    if beta =='':
        command = re.sub('--beta_column beta','--zscore_column '+z,command)
    else:
        command = re.sub('(?<=--beta_column )beta',beta,command) 
        
    command = command.replace(' ".*gz" ',' '+data_folder+'/'+filename+' ')
    command = re.sub(' SNP ',' '+snp+' ',command)
    command = re.sub(' pvalue ',' '+p+' ',command)
    command = re.sub(' P ',' '+p+' ',command)
    command = re.sub(' A1 ',' '+a1+' ',command)
    command = re.sub(' A2 ',' '+a2+' ',command)
    command = re.sub('./MetaXcan.py','python3 SPrediXcan.py',command)
    command = re.sub('(?<=--output_file ).+?(?=en)',current_path+'/results/spredxcan/',command)
    command = re.sub('(?<=--metaxcan_folder ).+?(?= --metaxcan_filter)',current_path+'/results/spredxcan',command)

    print(command)
    return smulti_output
def hmagma(current_path,filename,snp,p,ncol,n):
    hmagma = 'magma_v1.08_win/magma --bfile g1000_eur --pval data/EXTERNALIZING_MA_Problematic_drinking_2019_08_29.tbl.TRUNCATED.txt use=SNP,P ncol=Weight --gene-annot ../Input_Files/neuro.genes.annot --out '
    output_file = current_path+'/results/HMAGMA_neuro_'+re.sub('(?<=\.).+','',filename).replace('.','')
    hmagma+=output_file
    hmagma=re.sub('(?<=--pval ).+(?= use)',current_path+'/data/'+filename,hmagma)
    if ncol !=999:
        use = snp+','+p+' ncol='+ncol
    if n !='':
        use = snp+','+p+' N='+n
    hmagma=re.sub('(?<=use\=).+(?= --gene-annot)',use,hmagma)
    ls  = ['Astro','Fetal_brain','Adult_brain','neuro']
    result = [re.sub('(?<=results/HMAGMA_).+?(?=_)',i,re.sub('(?<=Files/).+?(?=.genes)',i,hmagma)) for i in ls]
    print(' && '.join(result))
    return [re.sub('.+(?=/results/)','',n).replace('/result/','') for n in result]
def ldsc(current_path,filename,n,ignore,p,a1,a2):        
    munge = './munge_sumstats.py --out sumstats/23andMe_EverPrescriptionPain_27805_104308_132113_ldsc.txt --merge-alleles w_hm3.snplist --sumstats data/23andMe_Intimate_Loneliness.dat.gz_129635_MAF_filtered.txt.gz'
    ld = './ldsc.py --h2 sumstats/23andMe_EverPrescriptionPain_27805_104308_132113_ldsc.txt.sumstats.gz --ref-ld-chr eur_w_ld_chr/ --w-ld-chr eur_w_ld_chr --out result/23andMe_EverPrescriptionPain_27805_104308_132113_ldsc.txt'
    if type(filename)!=list:
        munge = re.sub('(?<=--out ).+(?= --merge)',current_path+'/results/ldsc_sumstats/'+filename,munge)
        munge = re.sub('(?<=--sumstats ).+',current_path+'/data/'+filename,munge)
        ld = re.sub('(?<=--h2 ).+?(?= --ref-ld-chr)',current_path+'/results/ldsc_sumstats/'+filename+'.sumstats.gz',ld)
        ld = re.sub('(?<=--out ).+',current_path+'/results/ldsc/'+filename,ld)
    if n!='':
        munge+=' --N '+n
    if ignore !=999:
        munge+=' --ignore '+ignore
    munge+=' --a1 '+a1
    munge+=' --a2 '+a2
    munge+=' --p '+p

    print(munge+' && '+ld)
if __name__ == '__main__':
    current_path = sys.argv[1]
    filename = sys.argv[2]
    analysis = sys.argv[3]

    snp=sys.argv[4]
    beta=sys.argv[5]
    z=sys.argv[6]
    p=sys.argv[7]
    a1=sys.argv[8]
    a2=sys.argv[9]
    ncol=sys.argv[10]
    n=sys.argv[11]
    ignore=sys.argv[12]

    if analysis=='spred':
        spred = spredxcan(current_path,filename,snp,beta,z,p,a1,a2)
    elif analysis=='hmagma':
        h = hmagma(current_path,filename,snp,p,ncol,n)
    elif analysis=='ldsc':
        ldsc(current_path,filename,n,ignore,p,a1,a2)
    