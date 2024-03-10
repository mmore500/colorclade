import typing

import alifedata_phyloinformatics_convert as apc
from matplotlib.figure import Figure as mpl_Figure
import pandas as pd

from ._biopython_draw_colorclade_tree import biopython_draw_colorclade_tree


def draw_colorclade_tree(
    tree: pd.DataFrame,
    backend: typing.Literal["biopython"],
    taxon_name_key: str,
    mutate: bool = False,
    *args,
    **kwargs,
) -> mpl_Figure:
    if not mutate:
        tree = tree.copy()

    tree["name"] = tree[taxon_name_key]  # biopython expects "name" column

    rosetta_tree = apc.RosettaTree(tree)
    tree = {"biopython": lambda x: x.as_biopython}[backend](rosetta_tree)

    plotter = {"biopython": biopython_draw_colorclade_tree}[backend]
    return plotter(
        tree,
        *args,
        **kwargs,
    )
