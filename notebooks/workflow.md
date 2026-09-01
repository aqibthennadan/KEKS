Quickly drafting the prototyping workflow.  
Currently includes a combination of Excel and python scripts.  
1. With excel, the buses, the loads, their names and associated buses, the generators, the links would be defined.  
2. The script is used now only to prepare the load profiles, generation profiles, and their peak magnitudes.  

# README - Prototype
The file `build_network.ipybn' imports the energy system data from the excel sheets in the data directory, and builds the network in pypsa, which is subsequently saved in the data directory.

The file Prototype_2.ipynb imports this network, and plots insightful plots. Comments along the code, will help you follow better.
