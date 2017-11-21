from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pycr',
      version='0.0.0.9000',
      description='Analyzing Real-Time Quantitative PCR Data',
      url='https://github.com/MahShaaban/pycr',
      author='Mahmoud Ahmed',
      author_email='mahmoud.s.fahmy@students.kasralainy.edu.eg',
      license='GPL-3',
      packages=['pycr'],
      install_requires=[
        'markdown',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
