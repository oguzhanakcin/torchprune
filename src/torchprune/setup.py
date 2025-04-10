"""The setup sript for the torchprune package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="torchprune",
    version="2.0.0",
    author="The torchprune authors",
    author_email="lucasl@mit.edu",
    description="Pytorch-based pruning for efficient neural networks",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    licence="MIT Licence",
    url="https://github.com/lucaslie/torchprune",
    install_requires=[
        "cvxpy",
        "h5py",
        "imagecorruptions",
        "Mosek",
        "numpy",
        "opencv-python",
        "pyyaml",
        "requests",
        "scikit-learn",
        "scikit-image",
        "sentencepiece",
        "torch",
        "torchvision",
        "tensorboard",
        "torchdyn",
        "protobuf",
        "wand",
        "transformers @ git+https://github.com/huggingface/transformers.git",
        "datasets @ git+https://github.com/huggingface/datasets.git",
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
    ],
    python_requires=">=3.6,<3.12",
)
