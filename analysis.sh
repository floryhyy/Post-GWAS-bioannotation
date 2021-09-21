#!/bin/bash
spred_path='/home/MetaXcan/software'
hmagma_path='/home/H-MAGMA/Codes'
ldsc_path='/home/GitHub/ldsc'
current=$PWD

filename='chr1.assoc.dosage.gz'
snp='SNP'
beta='BETA'
z=''
p='P'
a1='A1'
a2='A2'
ncol=''
n='387649'
ignore=''

echo ${filename/.gz/}

#run Metaxcan
spredxcan=`python run_analysis.py $current $filename spred $snp $beta $z $p $a1 $a2 $ncol $n $ignore`
cd $spred_path
echo $spredxcan
eval $spredxcan

#run hmagma
# cd $current
# cd $current
# hmagma=`python run_analysis.py $current $filename hmagma $snp $beta $z $p $a1 $a2 $ncol $n $ignore `
# cd $hmagma_path
# echo $hmagma
# eval $hmagma

# run ldsc
# cd $current
# ldsc=`python run_analysis.py $current $filename ldsc $snp $beta $z $p $a1 $a2 $ncol $n $ignore`

# #if you are currently in enviorment with python3, switch enviorment below
# eval "$(conda shell.bash hook)"
# conda activate python27

# cd $ldsc_path
# echo $ldsc
# eval $ldsc


