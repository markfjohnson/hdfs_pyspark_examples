from setuptools import setup, find_packages
setup(
    name="SimpleHDFSwriter",
    version="0.1",
    packages=find_packages(),
    scripts=['file_writer_simple.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3', 'Faker'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Mark Johnson",
    author_email="mjohnson@mesosphere.com",
    description="This is a Spark write to HDFS Simple Example Package",
    license="PSF",
    keywords="Spark HDFS DCOS Mesos Mesosphere",
    #url="http://example.com/HelloWorld/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)