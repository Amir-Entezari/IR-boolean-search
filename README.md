
# Information Retrieval System with Advanced Boolean Search

## Overview
This project aims to develop an Information Retrieval (IR) system that supports both standard Boolean queries and proximity queries. The system is designed to handle a collection of text documents, building an Inverted Index and a Positional Index to facilitate efficient document retrieval.

## Features
- **Boolean Queries**: Supports AND, OR, and NOT operations.
- **Proximity Queries**: Finds documents where terms appear within a specified distance from each other.
- **Inverted Index**: Efficiently stores mappings from terms to the documents they appear in.
- **Positional Index**: Tracks the positions of terms within documents for proximity queries.

## Installation
To run this project, you will need to have Python installed along with the following libraries:
- `nltk`
- `string`

You can install the required libraries using pip:
```bash
pip install nltk
```

## Description

The repository contains:
- `preprocessing.py`: Script for data cleaning and preparation.
- `indexing.py`: Utilities for data indexing.
- `querying.py`: Implementation of various data querying methods.
- `experiments.ipynb`: Jupyter notebook containing experimental analysis and results.

## Installation

To get started with this project, clone this repository using:
```bash
git clone https://github.com/your-github-username/your-repository-name.git
```
Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Here's how you can run the scripts:

For a detailed walkthrough, open the `experiments.ipynb` in Jupyter Notebook or JupyterLab:
```bash
jupyter notebook experiments.ipynb
```

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.