from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='bibliotekaWDI',
    version='1.0.0',
    description='Biblioteka zawierajca przydatne funkcje na WDI',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    url='',
    author='Davsooonowy, HadesXBloodFire',
    author_email='muldaw@student.agh.edu.pl',
    license='MIT',
    classifiers=classifiers,
    keywords='AGH WDI',
    packages=find_packages(),
    install_requires=['']
)