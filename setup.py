from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='gisweb.anagraficautenti',
      version=version,
      description="Aggiunge campi anagrafici per i cittadini italiani. Basato su collective.examples.userdata",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read() + "\n"
                       + open(os.path.join("docs", "TODO.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Silvio Tomatis',
      author_email='silviot@gmail.com',
      url='http://github.com/silviot/gisweb.anagraficautenti',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gisweb',],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.users >= 1.0b7',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
