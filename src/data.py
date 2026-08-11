'''
A place for data handling functions for the KEKS project. This includes functions for loading and saving data, as well as functions for manipulating and transforming data.
'''
import pandas as pd

def clean_index(snaps, df):
    """
    Function to clean the index of a dataframe to match the snapshots of the network.
    This is useful when the index of the dataframe does not match the snapshots of the network.
    Will sort out small float point erros, and also point if big errors
    """
    df.index = pd.to_datetime(df.index)
    missing_idxs = set(snaps) - set(df.index)
    if len(missing_idxs) > 0:
        print(f"{set(snaps) - set(df.index)} missing from dataframe index.")
    if len(df.index) != len(snaps):
        raise ValueError(f"Length of dataframe index ({len(df.index)}) does not match length of snapshots ({len(snaps)}).")
    else:
        print(f"Length of both match, overwriting dataframe index with snapshots.")
        df.index = snaps
    return df

