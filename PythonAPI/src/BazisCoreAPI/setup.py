from setuptools import setup, find_packages

setup(
    name='BazisCoreAPI',
    packages=find_packages(),
    package_data={
        'BazisCoreAPI': ['lib/*.dll'],
    },
    include_package_data=True,
    install_requires=['pythonnet'],
)