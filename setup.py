'''
Build the aiml Py3 package
'''

from setuptools import setup
import io

# Extract version from constants.py
with io.open('aiml/constants.py', encoding='utf-8') as fid:
    for line in fid:
        if line.startswith('VERSION'):
            VERSION = line.strip().split()[-1][1:-1]
            break

# Read long description from README.md
with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aiml.py",
    version=VERSION,
    author="AlphasT101",
    author_email="anlexalphast@gmail.com",
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Required if using README.md
    url="https://github.com/calysto/aiml",
    python_requires='>=3.10',
    platforms=["any"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Chat",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    install_requires=['setuptools'],  # Add other dependencies here
    packages=["aiml", 'aiml.script'],
    include_package_data=True,
    package_data={
        'aiml': [
            'botdata/standard/*.aiml',
            'botdata/standard/*.xml',
            'botdata/alice/*.aiml',
            'botdata/alice/*.xml',
        ]
    },
    entry_points={
        'console_scripts': [
            'aiml-validate = aiml.script.aimlvalidate:main',
            'aiml-bot = aiml.script.bot:main',
        ]
    },
    test_suite='test.__main__.load_tests',
)