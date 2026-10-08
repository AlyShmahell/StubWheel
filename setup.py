import os
from setuptools import setup, find_packages

setup(
    name='stubwheel',
    version='2.0.0',
    url='https://github.com/AlyShmahell/stubwheel',
    author='Aly Shmahell',
    author_email='',
    description='a script that reserves a project name on PyPi',
	long_description=(open('README.md', encoding='utf-8').read() if os.path.exists('README.md')
                        else ''),
    long_description_content_type='text/markdown',
    packages=['stubwheel'],    
    install_requires=['twine >= 7.0.0', 'wheel >= 0.48.0', 'setuptools >= 84.0.0', 'questionary >= 2.1.0'],
    entry_points = {
        "console_scripts": [
            "stubwheel = stubwheel.__main__:main",
        ]
    }
)