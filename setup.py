from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e'
def get_requirment(file_path:str)->List[str]:

    requirment=[]
    with open(file_path) as file_obj:
        requirment=file_obj.readline()

        requirment=[req.replace("'\n","")for req in requirment]


        if HYPEN_E_DOT in requirment:
            requirment.remove(HYPEN_E_DOT)




setup(
name='ML_project',
version='0.0.1',
author='Ayush poddar',
author_email='ayushpoddarbest@gmail.com',
packages=find_packages(),
install_requires=get_requirment('requirment.txt')
)