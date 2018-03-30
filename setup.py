from setuptools import setup, find_packages


setup(
    name='jupyter-sql',
    version='0.1.0',

    description='Simple SQL kernel for Jupyter',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='jupyter sql kernel',
    packages=find_packages(),
    install_requires=[
        'jupyter',
        'jupyter_client',
        'ipython',
        'sqlparse',
        'sqlalchemy'
    ],
    entry_points={
    }
)
