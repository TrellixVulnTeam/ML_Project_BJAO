from setuptools import setup,find_packages
from typing import List

#Declaring varialbles for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Salman"
DESCRIPTION = "This is a first fsds Nov batch Machine Learning Project"

REQUIREMENTS_FILE_NAME = "requirements.txt"



def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in requirements.txt file

    return: This function is going to return a list which contain name of libraries mention in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirements_file.readlines().remove("-e .")



setup(
name = PROJECT_NAME,
version = VERSION,
author=AUTHOR,
packages=find_packages(),
install_requires = get_requirements_list()
)



