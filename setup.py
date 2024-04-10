from setuptools import find_packages,setup # type: ignore
from typing import List

HYPHEN='-e .'

def get_requirements(file_path):
    req=[]
    with open("requirements.txt") as f:
        req=f.readline()
        for i in range(len(req)):
            if req[i]=='\n':
                req[i].replace("\n","")
    if HYPHEN in req:
        req=req.remove(HYPHEN)
    return req

setup(
    name="mlproject",
    author_email='vtanwar@usc.edu',
    author='Vishwas Tanwar',
    version='0.0.1',
    install_requires=get_requirements('requirements.txt')

)