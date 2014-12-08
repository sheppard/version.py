import os
from setuptools import setup

LONG_DESCRIPTION = """
Make an image containing a version number (or other text)
"""


def parse_markdown_readme():
    """
    Convert README.md to RST via pandoc, and load into memory
    (fallback to LONG_DESCRIPTION on failure)
    """
    # Attempt to run pandoc on markdown file
    import subprocess
    try:
        subprocess.call(
            ['pandoc', '-t', 'rst', '-o', 'README.rst', 'README.md']
        )
    except OSError:
        return LONG_DESCRIPTION

    # Attempt to load output
    try:
        readme = open(os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ))
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()

setup(
    name='version.py',
    version='0.0.2',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='http://github.com/sheppard/version.py',
    license='MIT',
    scripts=['version.py'],
    description=LONG_DESCRIPTION.strip(),
    long_description=parse_markdown_readme(),
    install_requires=['Pillow'],
)
