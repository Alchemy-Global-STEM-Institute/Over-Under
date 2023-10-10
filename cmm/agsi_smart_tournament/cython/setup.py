from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize (
        'test_cython.py',
        compiler_directives={'language_level' : '3'}
    )
)