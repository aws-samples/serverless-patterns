"""Setup script for Serverless AI Agent Gateway."""

from setuptools import setup, find_packages

setup(
    name='serverless-ai-agent-gateway',
    version='0.1.0',
    description='Serverless AI Agent Gateway with AWS Bedrock and AgentCore',
    author='Development Team',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.12',
    install_requires=[
        'boto3>=1.34.0',
        'PyJWT>=2.8.0',
        'cryptography>=41.0.0',
        'requests>=2.31.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'pytest-asyncio>=0.21.0',
            'hypothesis>=6.92.0',
            'mypy>=1.7.0',
            'black>=23.12.0',
            'flake8>=6.1.0',
        ]
    }
)
