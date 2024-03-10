import typing

from Bio import Phylo as BioPhylo
import opytional as opyt

from ._val_to_color import val_to_color


def biopython_color_tree(
    tree: BioPhylo.BaseTree, salt: typing.Optional[int] = None
) -> None:
    """Recursively color tree nodes based on dominant color among terminals."""
    name = min(
        (opyt.or_value(y.name, "") for y in tree.get_terminals()),
        default=tree.name,
    )
    tree.color = val_to_color(name, salt=salt)

    for clade in tree.clades:
        biopython_color_tree(clade, salt=salt)
