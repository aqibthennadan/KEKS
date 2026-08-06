import pandas as pd

def calc_bus_sizes(n):
    """
    Function to calculate the size of each bus in the network.
    This is useful for visualizing the network and for understanding the relative sizes of the buses.
    Calculates the energy balance at each bus, and the contribution of each generator and Xlink to the bus.
    Parameters:
    n: pypsa.Network
    Returns:
    bus_sizes: Multi-index pandas series with generations shares.
    norm_bus_sizes: Normalized multi-index pandas series with generation shares, normalized by total generation at each bus.
    """
    ## Classical generators and their contribution at each bus
    gen_bus_sizes = (
        n.generators_t.p
        .sum()
        .groupby(
            [n.generators.bus, n.generators.carrier]
        )
        .sum()
    )

    ## sector-coupling gens, and their contribution at each bus. 
    link_bus_sizes = (
        n.links_t.p1
        .sum()
        .groupby(
            [n.links.bus1, n.links.carrier]
        )
        .sum()
    )
    link2_bus_sizes = (
        n.links_t.p2
        .sum()
        .groupby(
            [n.links.bus2, n.links.carrier]
        )
        .sum()
    )

    ##considering only the charging into the export sink, and not the discharging from it, which is the export to grid. 
    # export = pd.Series(
    #     {
    #         ("Extern_grid", n.stores.loc['Export_sink', 'carrier']): -1 * n.stores_t.p["Export_sink"][n.stores_t.p["Export_sink"] < 0].sum() 
    #     }
    # )

    bus_sizes = pd.concat([gen_bus_sizes, -1 * link_bus_sizes, -1 * link2_bus_sizes])
    bus_sizes = bus_sizes[bus_sizes > 1e-6] #removing zeroes and very small values
    # bus_sizes = pd.concat([bus_sizes, export])

    bus_sizes_norm = bus_sizes/bus_sizes.groupby(level = 0).sum()

    return bus_sizes, bus_sizes_norm