from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

package_name = 'monotonic_align'

setup(
  name=package_name,
  version='0.0.3',
  packages=[package_name],
  package_dir={package_name: 'py'},
  ext_modules = cythonize("_core.pyx"),
  include_dirs=[numpy.get_include()],
  install_requires=["Cython", "numpy"],
  long_description=long_description,
  long_description_content_type="text/markdown",
  description="Monotonic Align",
  classifiers=[
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
      "Topic :: Scientific/Engineering :: Artificial Intelligence",
  ],
)
