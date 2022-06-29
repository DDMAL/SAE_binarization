from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='SAE_binarization',
    version='1.0.0',
    description='Selectional auto-encoder (SAE) binarization.',
    url='https://github.com/DDMAL/SAE_binarization',
    author='Khoi Nguyen, Wanyi Lin',
    license='MIT License',
    packages=find_packages(include=['SAE_binarization', 'SAE_binarization.*']),
    install_requires=requirements,
    package_data={"":["MODELS/*.h5"]},
    python_requires=">=3.7.5"
)
