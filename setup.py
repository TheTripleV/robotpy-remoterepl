import subprocess
import setuptools

try:
    ret = subprocess.check_output("git describe --tags --abbrev=0", shell=True,)
    version = ret.decode("utf-8").strip()
except:
    version = "master"

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="robotpy-remoterepl",
    version=version,
    author="Vasista Vovveti",
    author_email="vasistavovveti@gmail.com",
    description="Python REPL that runs within robotpy robot code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheTripleV/robotpy-remoterepl",
    install_requires=["robotpy>=2022"],
    packages=["remoterepl"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    console_scripts=["robotpy-remoterepl=remoterepl.__main__:start"],
)