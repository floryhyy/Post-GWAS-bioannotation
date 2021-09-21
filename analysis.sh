#!/bin/bash
spred_path='/c/Users/flori.LAPTOP-SAJS3KG7/Documents/GitHub/sanchez-roige-lab/MetaXcan/software'
hmagma_path='/c/Users/flori.LAPTOP-SAJS3KG7/Documents/GitHub/H-MAGMA/Codes'
ldsc_path='/c/Users/flori.LAPTOP-SAJS3KG7/Documents/GitHub/ldsc'
filename='chronic_pain-bgen.stats'
current=$PWD
echo ${filename/.gz/}

#run Metaxcan
spredxcan=`python test.py $current $filename spred`
cd $spred_path
echo $spredxcan
eval $spredxcan

#run hmagma
cd $current
cd $current
hmagma=`python test.py $current $filename hmagma`
cd $hmagma_path
echo $hmagma
eval $hmagma

# run ldsc
# cd $current
# ldsc=`python test.py $current $filename ldsc`

# #if you are currently in enviorment with python3, switch enviorment below
# eval "$(conda shell.bash hook)"
# conda activate python27

# cd $ldsc_path
# echo $ldsc
# eval $ldsc


