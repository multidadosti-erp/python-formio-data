from setuptools import setup, find_packages

setup(
    name='formio-data',
    version='2.1.0',
    description='Form.io JSON-data API',
    url='https://github.com/novacode-nl/python-formio-data',
    author='Bob Leers',
    author_email='bob@novacode.nl',
    license='MIT',
    packages=find_packages(include=['formiodata']),
    package_dir={'formiodata': 'formiodata'},
    extras_require={
        # Optional dependencies
        'json_logic': ['json-logic-qubit'],
    },
 )
