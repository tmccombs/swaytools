from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
        name='swaytools',
        version='0.1.0',
        description='Quality of life tools for sway',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        license='GPL3',
        author='Thayne McCombs',
        url='https://github.com/tmccombs/swaytools',
        keywords='sway i3 tools',
        python_requires='>=3.8.0',
        entry_points={
            'console_scripts': [
                'swayinfo = swaytools.info:main',
                'winfocus = swaytools.winfocus:main',
            ]
        },
        classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 3",
            "Topic :: Desktop Environment",
        ]
)
