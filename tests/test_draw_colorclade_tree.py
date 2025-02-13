import functools
import random
import typing

from matplotlib import pyplot as plt
import pandas as pd
import pytest
from teeplot import teeplot as tp

from colorclade import draw_colorclade_tree


def save_plot(f: typing.Callable):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        tp.tee(
            f,
            *args,
            teeplot_outattrs={
                k: "lambda" if isinstance(v, typing.Callable) else v
                for k, v in kwargs.items()
            },
            teeplot_outdir="/tmp",
            **kwargs,
        )

    return inner


@pytest.mark.parametrize(
    "label_tips",
    [True, False, lambda node: node.name if random.random() < 0.7 else ""],
)
@pytest.mark.parametrize(
    "color_labels",
    ["black", lambda _: random.choice(["blue", "red", "green"])],
)
@save_plot
def test_draw_colorclade_tree(label_tips, color_labels):
    alifestd_df1 = pd.DataFrame(
        {
            "id": [0, 1, 2, 3, 4],
            "ancestor_id": [0, 0, 1, 1, 0],
            "taxon": [
                "root",
                "inner",
                " " * 23 + "woof",
                " " * 17 + "meow",
                " " * 23 + "glubglub",
            ],
            "origin_time": [0.0, 0.7, 2.4, 2.7, 2.3],
            "ancestor_list": ["[none]", "[0]", "[1]", "[1]", "[0]"],
        },
    )
    alifestd_df2 = pd.DataFrame(
        {
            "id": [0, 1, 2, 3, 4],
            "ancestor_id": [0, 0, 1, 0, 1],
            "taxon": [
                "root",
                "inner",
                " " * 23 + "woof",
                " " * 17 + "meow",
                " " * 23 + "glubglub",
            ],
            "origin_time": [0.0, 0.7, 2.4, 2.7, 2.3],
            "ancestor_list": ["[none]", "[0]", "[1]", "[0]", "[1]"],
        },
    )

    plt.clf()
    fig, axes = plt.subplots(1, 2)
    draw_colorclade_tree(
        alifestd_df1,
        taxon_name_key="taxon",
        ax=axes.flat[0],
        backend="biopython",
        label_tips=label_tips,
        color_labels=color_labels,
    )
    draw_colorclade_tree(
        alifestd_df2,
        taxon_name_key="taxon",
        ax=axes.flat[1],
        backend="biopython",
        label_tips=False,
    )
    axes.flat[1].set_xlim(reversed(axes.flat[1].get_xlim()))
    fig.set_size_inches(7, 2.5)
    plt.tight_layout()
