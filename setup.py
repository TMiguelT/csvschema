from distutils.core import setup


setup(
    name='CsvSchema',
    version='1.1.0',
    author='Piotr Olejarz',
    author_email='vadwook@hotmail.com',
    url='http://bitbucket.org/vadwook/csvschema/',
    packages=['csv_schema', 'csv_schema.columns', 'csv_schema.structure'],
    license='LICENSE.txt',
    description='Tool for describing CSV data structure.',
    long_description=open('README.rst').read(),
)
