"""
The setup file for GSBG.
"""

# Created by Wenjie Du <wenjay.du@gmail.com>
# License: GLP-v3


from setuptools import find_packages
from setuptools import setup

from gsbg import __version__

with open("./README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="gsbg",
    version=__version__,
    description="A tool for Google Scholar citation badge generation.",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GPL-3.0",
    author="Wenjie Du",
    author_email="wenjay.du@gmail.com",
    url="https://github.com/WenjieDu/Google_Scholar_Badge_Generator",
    download_url="https://github.com/WenjieDu/Google_Scholar_Badge_Generator/archive/main.zip",
    keywords=[
        "Google Scholar",
        "citation",
        "citation number",
        "shields.io",
        "badge",
        "svg",
        "generating",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    python_requires=">=3.5",
    setup_requires=["setuptools>=64.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
