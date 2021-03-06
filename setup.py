from setuptools import setup , find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable' ,
    'Intended Audience :: Science/Research' ,
    'Operating System :: Microsoft :: Windows :: Windows 10' ,
    'License :: OSI Approved :: MIT License' ,
    'Programming Language :: Python :: 3'
]

setup (
    name='PySIC' ,
    version='1.1.1' ,
    description='A package for satellite image classification using machine learning models' ,
    long_description=open ( 'README.md' ).read ( ) + '\n\n' + open ( 'CHANGELOG.txt' ).read ( ) ,
    url='https://github.com/Hejarshahabi' ,
    author='Hejar Shahabi' ,
    author_email='hejarshahabi@gmail.com' ,
    license='MIT' ,
    classifiers=classifiers ,
    keywords='Machine Learning, Remote Sensing ' ,
    long_description_content_type='text/markdown',
    packages=find_packages ( ) ,
    install_requires=['']
)
