from setuptools import setup, find_packages

setup(
    name='bigparser',
    version='0.0.4',
    url='https://github.com/ajayarjun-bka/bigparser-python-lib',
    author='Ajay Arjun',
    author_email='arjun.bka@gmail.com',
    description='Python client library for BigParser API.',
    packages=find_packages(exclude=['tests','app.py']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='MIT',
    python_requires=">=3.3",
    install_requires=[
        'requests', 'pandas', 'numpy'
    ],
)
