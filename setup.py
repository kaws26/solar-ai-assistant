from setuptools import setup, find_packages

setup(
    name="solar-ai-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain-core",
        "langchain-groq",
        "streamlit",
        "python-dotenv",
        "opencv-python",
        "numpy"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered rooftop solar analysis system using satellite imagery and LLM-powered insights.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/solar-ai-assistant",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 