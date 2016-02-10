from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


def get_requires_from_txt(filename):
    requires = []
    with open(os.path.join(here, filename)) as file:
        for line in file:
            if not line.startswith('--'):
                requires.append(line.replace('\n', ''))

    return requires


setup(
    name="TestableObjects",
    version="0.1.0",
    packages=find_packages(),
    tests_require=['mock', 'six'],
    author='Adam Englander',
    author_email='adamenglander@yahoo.com',
    license='MIT',
    test_suite="tests",
)
