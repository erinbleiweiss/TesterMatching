from setuptools import find_packages, setup

setup(name='TesterMatching',
      version='1.0',
      description='Tester Matching Demo App',
      url='http://github.com/erinbleiweiss/TesterMatching',
      author='Erin Bleiweiss',
      author_email='erinbleiweiss@gmail.com',
      packages=find_packages(),
      install_requires=[
            'tornado',
            'flask',
            'flask-cors'
      ])