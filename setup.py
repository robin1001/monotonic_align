from setuptools import setup
from Cython.Build import cythonize
import numpy

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
  name = 'monotonic_align',
  version='0.0.1',
  ext_modules = cythonize("core.pyx"),
  include_dirs=[numpy.get_include()],
  setup_requires=["Cython==0.29.21", "numpy==1.18.5"],
  long_description=long_description,
  long_description_content_type="text/markdown",
  description="Monotonic Align",
  classifiers=[
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent",
      "Topic :: Scientific/Engineering :: Artificial Intelligence",
  ],
)
