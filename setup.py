from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e . '
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return list of requirement
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','') for req in requirement]

        if Hyphen_e_dot in requirement:
            requirement.remove(Hyphen_e_dot)
    return requirement


setup(
name='mlproject',
version='0.0.1',
author='Ankush',
packages=find_packages(),
install_requires = get_requirement('requirements.txt')
)