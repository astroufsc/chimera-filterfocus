from distutils.core import setup

setup(
    name='chimera_filterfocus',
    version='0.0.1',
    packages=['chimera_filterfocus', 'chimera_filterfocus.controllers'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-filterfocus',
    license='GPL v2',
    author='William Schoenell',
    author_email='wschoenell@gmail.com',
    description='Automatically apply focus offsets when filter changes'
)
