import os
from setuptools import setup, find_packages

here = os.path.realpath(os.path.dirname(__file__))
scripts = [ os.path.join(here, 'src', 'qiimeToMaaslin.py') ]
setup(
    name='qiimetomaaslin',
    version='1.1.0',
    description='''Data munging script to change text Qiime OTU tables to
    pcl-formatted, maaslin-compatible text files''',
    packages=[],
    zip_safe=False,
    install_requires=[ ],
    classifiers=[
        "Development Status :: 4 - Beta"
    ],
    scripts=scripts
)
