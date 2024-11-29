from setuptools import setup, find_packages

setup(
    name='shadowfinder',
    version='1.0.0',
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Uma ferramenta CLI para rastrear perfis em redes sociais.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/shadowfinder',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=7.0',
        'requests[socks]>=2.25.1',
        'rich>=9.0.0',
        'tweepy>=4.0.0',
    ],
    entry_points={
        'console_scripts': [
            'shadowfinder=shadowfinder.cli:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
