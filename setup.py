from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
    
setup(
    name="RegressionProject",
    version='0.0.1',
    author='Deepak kumar',
    author_email='kumardeepak11042@gmail.com',
    install_reuires=get_requirements('requirments.txt'),
    packages=find_packages(),
    
)