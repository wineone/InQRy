import os
import re
import subprocess

VERSION_PY = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def version_getter():
    try:
        pattern = re.compile(r'(v\d+\.\d+\.?\d?).*', re.UNICODE)
        tag = subprocess.check_output(["git", "describe", "--tags"]).rstrip().decode("utf-8")
        return re.findall(pattern, tag)[0]
    except:
        with open(VERSION_PY, 'r') as f:
            return f.read().strip().split('=')[-1].replace('"', '')


def version_writer():
    message = "#  Do not edit this file. Pipeline versioning is governed by git tags."
    with open(VERSION_PY, 'w') as f:
        f.write(message + os.linesep + "__version__ = '{ver}'".format(ver=version_getter()) + '\n')


def main():
    return version_writer()


main()

setup(name='InQRy',
      version="{ver}".format(ver=version_getter()),
      license='MIT',
      description='Gets machine specs and generates a QR code containing them',
      author=['OXO Hub Lab', 'Eric Hanko', 'Jacob Zaval'],
      author_email='apxlab@microsoft.com',
      url="https://office.visualstudio.com/APEX/Lab-Projects/_git/lab_inventory",
      packages=['inqry', "inqry.system_specs"],
      long_description=open('README.md').read(),
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
