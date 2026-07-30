import pandas as pd
import matplotlib.pyplot as plt

def plot_EnBalance(n, carrier, ax, bus_sizes, bus_scale = 3e-10, title = 'En balance'):

    #filtering buses and bus sizes for the carrier of interest
    cr_buses = n.buses[n.buses.carrier == carrier].index
    bus_sizes_cr = bus_sizes.loc[bus_sizes.index.get_level_values(0).isin(cr_buses)]
    
    #Setting link width only for carrier of interest, and the remaining zero
    link_width = pd.Series(0.0, index=n.links.index)
    link_width[n.links['carrier'] == carrier] = 1.5

    n.plot(
        ax=ax,
        bus_sizes=bus_sizes_cr * bus_scale,
        link_widths=link_width,
        geomap = False,
        title = title,
        bus_split_circle = False
    )

    # Anootation text with bus names, offset a bit
    offset = 0.00015  
    for name, row in n.buses.loc[cr_buses].iterrows():
        ax.text(
            row.x + offset,
            row.y + offset,
            name,
            fontsize=8
        )
    handles = []

    # Creating legends based on carriers
    for carrier in bus_sizes.index.get_level_values(1).unique():
        handles.append(
            plt.Line2D(
                [],
                [],
                marker="o",
                linestyle="",
                color=n.carriers.loc[carrier, "color"],
                label=carrier
            )
        )

    plt.legend(handles=handles)