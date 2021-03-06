import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# Allow setup.py to be run from any path.
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="pyqtnavutils",
    version="0.1.0",
    packages=["pyqtnavutils"],
    author="dhzdhd",
    # author_email='yencardonaal@unal.edu.co',
    maintainer="dhzdhd",
    # maintainer_email='yencardonaal@unal.edu.co',
    download_url="https://github.com/dhzdhd/pyqt_nav_utils",
    # install_requires=["PyQt6"],
    python_requires=">=3.9",
    include_package_data=True,
    license="MIT",
    # description="",
    long_description=README,
    long_description_content_type="text/markdown",
    # classifiers=[
    #     'Development Status :: 4 - Beta',
    #     # 'Development Status :: 5 - Production/Stable',
    #     'License :: OSI Approved :: BSD License',
    #     'Programming Language :: Python :: 3.10',
    #     'Programming Language :: Python :: 3.9',
    #     'Programming Language :: Python :: 3.8',
    #     'Programming Language :: Python :: 3.7',
    # ],
    #
    # entry_points={
    #     "pyinstaller40": [
    #         "hook-dirs = qt_material:get_hook_dirs"
    #     ]
    # },
)
