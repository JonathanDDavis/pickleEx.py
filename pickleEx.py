#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      jd0919889
#
# Created:     31/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import Pickle
import pickle

#Get name
#name = input (What is your name?: ")

# Dump name
#pickle.dump(name, open( "save.sav", "wb" ) )

#load file and print name
name = pickle.load( open( "save.sav", "rb" ) )
print name
