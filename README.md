# muti_gentic_secondary_analysis

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
  
