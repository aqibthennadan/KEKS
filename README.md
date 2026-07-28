# KEKS – Kommunale Energiesysteme Krisen Simulator

## Overview

KEKS is a Python-based modelling framework for analysing the resilience of municipal energy systems under critical supply scenarios. The model focuses on the interaction between electricity, heating, and gas networks while considering network constraints and the supply requirements of critical infrastructure.

The objective of KEKS is to enable a detailed assessment of municipal energy system resilience by combining energy network modelling with scenario-based analysis. The framework is designed to support the evaluation of critical situations such as supply shortages and to investigate the impact of network limitations on energy supply reliability.

The model is developed within the scope of the Kores project, with the aim of establishing a transferable methodology for resilience assessment across different municipalities.

## Current Development Status

KEKS is currently under active development. The initial prototype is implemented using the open-source Python framework PyPSA and includes simplified electricity, heating, and gas networks. The prototype serves to evaluate the modelling approach, identify required data structures, and establish the foundation for future application to municipal use cases.

## Installation

### 1. Clone the repo
```bash
git clone https://github.com/aqibthennadan/KEKS.git
cd KEKS
```   

### 2. Create and activate conda environment
```bash
conda env create -f environment.yml
conda activate keks_env
```
Alternatively, mamba could be used; faster at resolving packages (need to check-it, conda was slow here)  

### 3. Setup VS-code
This repository has been developed to work well with VS-code, and would be recomended here as well.  
However, it is not a must. If the user chooses to use any other tool, then the folder settings enabling jupyter notebooks to be opened by default from project-root will not work.  
Instead, the working directory must be set manually for all notebooks in the directory "root/notebooks/..."
```python
import os

os.chdir(os.getcwd(), '..')
```

## Repository structure  
```text
KEKS/  
|  
|── notebooks/              # Analysis and experiment notebooks  
|  
|── src/                    # Reusable Python functions and modules  
|   
|── data/                   # Input datasets  
|  
|── results/                # Generated results and figures  
|    
|── environment.yml         # Conda environment definition  
|    
|── README.md  
```

## Contribution workflow

Direct commits to `main` should be avoided.  

Changes should be developed in feature branches and merged through pull requests.