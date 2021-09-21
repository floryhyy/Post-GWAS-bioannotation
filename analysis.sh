#!/bin/bash
spred_path='/home/MetaXcan/software'
hmagma_path='/home/H-MAGMA/Codes'
ldsc_path='/home/GitHub/ldsc'
current=$PWD

# bash analysis.sh SNP BETA 999 P A1 A2 999 387649 999 chr1.assoc.dosage.gz
snp=$1
beta=$2
z=$3
p=$4
a1=$5
a2=$6
ncol=$7
n=$8
ignore=$9
filename=${10}

echo ${filename/.gz/}

#run Metaxcan
# spredxcan=`python run_analysis.py $current $filename spred $snp $beta $z $p $a1 $a2 $ncol $n $ignore`
# cd $spred_path
# echo $spredxcan
# eval $spredxcan

#run hmagma
cd $hmagma_path
hmagma=`python run_analysis.py $current $filename hmagma $snp $beta $z $p $a1 $a2 $ncol $n $ignore `
cd $hmagma_path
echo $hmagma
eval $hmagma

# run ldsc
# cd $current
# ldsc=`python run_analysis.py $current $filename ldsc $snp $beta $z $p $a1 $a2 $ncol $n $ignore`

# #if you are currently in enviorment with python3, switch enviorment below
# eval "$(conda shell.bash hook)"
# conda activate python27

# cd $ldsc_path
# echo $ldsc
# eval $ldsc


