import setuptools

setuptools.setup(
    name='mac-youtube',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
