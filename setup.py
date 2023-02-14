

# from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="rclonerizer",
  url="git@github.com:ComfortableSoftware/rclonerizer.git",
  version="0.0.1",
  package_dir={"rclonerizer": "rclonerizer"},
  package_data={
      "rclonerizer": [
          "../doc/*",
      ]
  },
  packages=["rclonerizer"],
  install_requires=[
      "CF",
  ],
  extras_require={
  },
  scripts=["scripts/rclonerizer"],
#  entry_points = """
#      [console_scripts]
#      runawayClock=__main__:cli
#  """,
)
