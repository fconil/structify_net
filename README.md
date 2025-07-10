# structify-net

## Description

**structify-net** is a Python library for generating networks with customizable structures, node counts, and link numbers. It provides a unified framework to model various network structures, including community/bloc structures, spatial structures, and more.

A structure is defined by:
- The number of nodes `n`
- A ranking of all node pairs, from most likely to least likely to be connected

---

## Documentation

- Full documentation: [https://structify-net.readthedocs.io/en/latest/](https://structify-net.readthedocs.io/en/latest/)
- Method description: See our upcoming paper (to be published)

---

## Installation

To install the latest release of structify-net, use:

```bash
pip install structify-net
```

## Usage

Once installed, you can import the main modules as follows:

```python
import structify_net as stn
import structify_net.viz as viz
import structify_net.zoo as zoo
import structify_net.scoring as scoring
```

---

## Development

If you want to contribute or work on structify-net, follow these steps:

### Install in editable mode with development dependencies

To set up the development environment, you can install the package in [editable mode](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs) along with the [dependency group](https://pip.pypa.io/en/stable/user_guide/#dependency-groups) named `dev`.

Editable mode allows you to make changes to the source code and have them immediately reflected without reinstalling the package. This is useful for development and testing.

```bash
pip install -e . --group dev
```

---

### If you want to use uv

If you want to use the new [uv](https://github.com/astral-sh/uv) tool.

1. Create a virtual environment

```bash
uv venv .venv
source .venv/bin/activate
```

2. Install structify-net in editable mode

```bash
uv pip install -e .
```

3. Install the packages of the `dev` dependency group with [uv sync](https://docs.astral.sh/uv/reference/cli/#uv-sync)

```bash
uv sync --group dev
```
