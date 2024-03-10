[
![PyPi](https://img.shields.io/pypi/v/colorclade.svg?)
](https://pypi.python.org/pypi/colorclade)
[
![CI](https://github.com/mmore500/colorclade/actions/workflows/ci.yaml/badge.svg)
](https://github.com/mmore500/colorclade/actions)
[
![GitHub stars](https://img.shields.io/github/stars/mmore500/colorclade.svg?style=round-square&logo=github&label=Stars&logoColor=white)](https://github.com/mmore500/colorclade)
[![DOI](https://zenodo.org/badge/770006855.svg)](https://zenodo.org/doi/10.5281/zenodo.10802404)

**_colorclade_** draws phylogenies with hierarchical coloring for
easier visual comparison

- Free software: MIT license
- Repository: <https://github.com/mmore500/colorclade>
- Documentation: <https://github.com/mmore500/colorclade/blob/master/README.md>

## Install

`python3 -m pip install colorclade`

## Example Usage

```python3
from colorclade import draw_colorclade_tree

fig, axes = plt.subplots(1, 2)
draw_colorclade_tree(
    alifestd_df1,
    taxon_name_key="taxon",
    ax=axes.flat[0],
    backend="biopython",
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
```

![example](docs/assets/test_draw_colorclade_tree.png)

See `tests/test_draw_colorclade_tree.py` for full example code.

## Citing

If colorclade contributes to a scientific publication, please cite it as

> Matthew Andres Moreno. (2024). mmore500/colorclade. Zenodo. TODO

```bibtex
@software{moreno2024colorclade,
  author = {Matthew Andres Moreno},
  title = {mmore500/colorclade},
  month = mar,
  year = 2024,
  publisher = {Zenodo},
  doi = {10.5281/zenodo.10802404},
  url = {https://zenodo.org/doi/10.5281/zenodo.10802404}
}
```

Consider also citing [Biopython](https://biopython.org/wiki/Publications) and [matplotlib](https://matplotlib.org/stable/users/project/citing.html).
And don't forget to leave a [star on GitHub](https://github.com/mmore500/colorclade/stargazers)!
