# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup
import subprocess


# -----------------------------------------------------------------------------
def main():
    """main setup method"""
    setup(
        name="{{cookiecutter.company}}-{{cookiecutter.namespace}}-{{cookiecutter.project}}",
        version=(subprocess.check_output(['git', 'describe', '--tag'])
                 .strip().decode('ascii').replace('-', '_')),
        packages=find_packages(),
        zip_safe=False)


# =============================================================================
if __name__ == '__main__':
    main()
