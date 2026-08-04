import pandas as pd
import matplotlib.pyplot as plt

def plot_EnBalance(network, carrier, ax, bus_sizes, bus_scale = 3e-10, title = 'En balance'):

    #filtering buses and bus sizes for the carrier of interest
    cr_buses = network.buses[network.buses.carrier == carrier].index
    bus_sizes_cr = bus_sizes.loc[bus_sizes.index.get_level_values(0).isin(cr_buses)]
    
    #Setting link width only for carrier of interest, and the remaining zero
    link_width = pd.Series(0.0, index=network.links.index)
    link_width[network.links['carrier'] == carrier] = 1.5
    if carrier == 'thermal':
        link_width[network.links['carrier'] == 'DHN'] = 1.5
 
    #Merging LT and HT into a single thermal bus, renaming HT to LT, and summing the sizes
    bus_sizes_cr.index = pd.MultiIndex.from_tuples([
        (bus.replace('_HT', '_LT'), tech) for bus, tech in bus_sizes_cr.index
    ], names = bus_sizes_cr.index.names)

    bus_sizes_cr = bus_sizes_cr.groupby(level = [0,1]).sum()

    network.plot(
        ax=ax,
        bus_sizes=bus_sizes_cr * bus_scale,
        link_widths=link_width,
        geomap = False,
        title = title,
        bus_split_circle = False
    )

    # Anootation text with bus names, offset a bit
    offset = 0.00015  
    for name, row in network.buses.loc[bus_sizes_cr.index.get_level_values(0).unique()].iterrows():
        ax.text(
            row.x + offset,
            row.y + offset,
            name.strip('_LT'),
            fontsize=14,
            zorder = 10000
        )
    handles = []

    # Creating legends based on carriers
    for carrier in bus_sizes_cr.index.get_level_values(1).unique():
        handles.append(
            plt.Line2D(
                [],
                [],
                marker="o",
                linestyle="",
                color=network.carriers.loc[carrier, "color"],
                label=carrier
            )
        )

    plt.legend(handles=handles)