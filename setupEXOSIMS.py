"""setupEXOSIMS.py is designed to setup the EXOSIMS module for operation

Must be run from top file of EXOSIMS
Written by: Dean Keithly
Written on: 9/9/2018
"""
import os
import shutil
#import pip
from setuptools.command.easy_install import main as install

# def install(package):
#     #Checks to see if the package can be imported. If not, then use pip to install the package... (might not work)
#     try:
#         __import__(package)
#     except ImportError:    
#         if hasattr(pip, 'main'):
#             pip.main(['install', package])
#         else:
#             pip._internal.main(['install', package])


if __name__ == '__main__':
    #Check to ensure files exist in the correct places
    files = ['makeSimilar.json','makeSimilar2.json','makeSimilarScripts.py','deleteMe100.json']
    for file in files:
        assert os.path.isfile('./EXOSIMS/Scripts/' + file)
    for folder in ['Scripts','run']:
        assert os.path.isdir('./EXOSIMS/' + folder)

    #### Part 1 makeSimilarScripts.py ##########################
    if not os.path.isdir('../Scripts'):#Check if the folder exists otherwise make it
        os.mkdir('../Scripts')
    for file in files:#Copy makeSimilarScripts to top level Scripts
        shutil.copy2('./EXOSIMS/Scripts/' + file,'../Scripts/' + file)


    #### If packages not installed, install them
    #pip.main(['install','-r','./requirements.txt'])
    with open('./requirements.txt') as g:
        reqs = g.readlines()
    for line in reqs:
        install(line.split())



    #Download HLC fit files from IPAC WFIRST website
    #Download de432.bsp file fromJPL