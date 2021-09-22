import re
import sys
import pandas as pd
def no_fuma_format(filename):
    spred_file = 'SMultiXcan_Brain_v8_'+filename+'.csv'
    spred_fp = 'results/'+spred_file

    #please fill in file name for hmagma result seperately 
    annot_ls  = ['iPSC_derived_astro','Fetal_brain','Adult_brain','iPSC_derived_neuro']
    output_file ='results/hmagma/HMAGMA_neuro_'+filename.replace('.','')

    ls = [re.sub('(?<=results/hmagma/HMAGMA_).+?(?=_)',i,output_file)+'.genes.out' for i in annot_ls]

    df = pd.read_csv(spred_fp,sep='\s+')
    #sigSPrediXcan
    size = df.shape[0]
    spred_sig = df[df['pvalue']<(0.05/size)]
    result = 'results/'+re.sub('.csv','_sigResult.csv',spred_file)
    spred_sig.to_csv(result,index=False)

    name_fp = ['Astro_gene_name.csv','Fetal_brain_gene_name.csv','Adult_brain_gene_name.csv','neuro_gene_name.csv']
    cls=['sigHMAGMA_Astro','sigHMAGMA_Fetal_brain','sigHMAGMA_Adult_brain','sigHMAGMA_neuro']

    for i in range(len(ls)):
        h=pd.read_csv(ls[i],sep='\s+')
        name=pd.read_csv(name_fp[i],usecols=['GENE','Gene.name'])
        if 'Gene.name' not in h.columns:
            h = h.merge(name,on='GENE',how='left')
        if h.shape[0] > 300:
            h=h[h['P'] < (0.05/h.shape[0])]

        result = re.sub('.out','_sigResult.csv',ls[i])
        h.to_csv(result,index=False)

if __name__ == '__main__':

    #file name for smultiXcan result
    filename =  sys.argv[1]
    no_fuma_format(filename)