from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='southern_hemisphere',
    version='0.1.3',
    description="A module used for a lightning talk at ChiPy meetup group",
    long_description=readme,
    author="Janis Lesinskis",
    author_email='janis@pythoncharmers.com',
    packages=[
        'southern_hemisphere',
    ],
    package_dir={'southern_hemisphere':
                 'southern_hemisphere'},
    include_package_data=True,
    install_requires=[
        "upsidedown",
    ],
    zip_safe=False,
    keywords='ChiPy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
