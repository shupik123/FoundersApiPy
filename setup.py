import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="founders",
	version="0.1.1",
	author="shupik",
	description="A small package for the founders api",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/shupik123/FoundersApiPy",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	install_requires=[
          'requests'
      ]
)