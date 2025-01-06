from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    try:
        requirement_list = []
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            for req  in requirements:
                requirement = req.strip()
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_list

setup(
    name='IMdb',
    version='0.0.1',
    author='Samarth Garg',
    author_email='samarthgarg8099@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)