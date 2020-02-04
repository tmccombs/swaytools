from setuptools import setup, find_packages

setup(
        name='swaytools',
        version='0.1.0',
        description='Quality of life tools for sway',
        packages=find_packages(),
        license='GPL3',
        author='Thayne McCombs',
        python_requires='>=3.8.0',
        entry_points={
            'console_scripts': [
                'swayinfo = swaytools.info:main',
                'winfocus = swaytools.winfocus:main',
            ]
        }
)
