from collections import abc
import copy
import typing

from Bio import Phylo as BioPhylo
from matplotlib import pyplot as plt
from matplotlib.axes import Axes as mpl_Axes

from ._biopython_color_tree import biopython_color_tree as color_tree
from ._biopython_pare_tree import biopython_pare_tree as pare_tree
from ._biopython_sort_tree import biopython_sort_tree as sort_tree
from ._matplotlib_drop_overlapping_labels import (
    matplotlib_drop_overlapping_labels,
)


def biopython_draw_colorclade_tree(
    tree: BioPhylo.BaseTree,
    ax: typing.Union[plt.Axes, tuple, None] = None,
    drop_overlapping_labels: bool = False,
    fig_size: typing.Optional[tuple] = None,
    label_tips: bool = True,
    line_width: float = 4.0,
    max_leaves: typing.Optional[int] = None,
    salt_color: typing.Optional[int] = None,
    use_branch_lengths: bool = True,
) -> mpl_Axes:

    biopy_tree = copy.deepcopy(tree)
    if not use_branch_lengths:
        for clade in biopy_tree.find_clades(order="postorder"):
            clade.branch_length = 1.0

    if max_leaves is not None:
        biopy_tree = pare_tree(biopy_tree, max_leaves)

    sort_tree(biopy_tree.root)
    color_tree(biopy_tree.root, salt=salt_color)

    if isinstance(ax, abc.Sequence):
        _fig, ax = plt.subplots(figsize=fig_size, squeeze=True)
    elif ax is None:
        ax = plt.gca()
    elif not isinstance(ax, plt.Axes):
        raise TypeError(f"ax must be a Axes instance or tuple, not {type(ax)}")

    with plt.rc_context({"lines.linewidth": line_width}):
        BioPhylo.draw(
            biopy_tree,
            axes=ax,
            label_func=lambda node: (
                node.name if label_tips and node.is_terminal() else ""
            ),
            do_show=False,
        )
        if drop_overlapping_labels:
            matplotlib_drop_overlapping_labels(ax)

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        ax.spines["left"].set_visible(False)
        ax.set_yticklabels([])
        ax.set_yticks([])
        ax.axes.get_yaxis().set_visible(False)

    return ax
