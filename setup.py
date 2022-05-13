from setuptools import setup

PACKAGE_NAME = 'rulefinder'

REQUIREMENTS = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        REQUIREMENTS.append(line)

setup(
   name=PACKAGE_NAME,
   version='0.1.0',
   description='A project for WSI course at MiNI faculty at WUT',
   packages=[PACKAGE_NAME],  
   install_requires= REQUIREMENTS
)
