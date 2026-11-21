# safestrip

Clean leading and trailing whitespace from a Python string with a small source-available function. The intended reader is a Python developer inspecting this example repository.

The demonstrated operation is `clean(" a ") == "a"`. The evidence does **not** establish other normalization behavior, distribution to PyPI, supported operating systems, a license or production use.

## Run from a source checkout

**Prerequisite:** Python 3.11 or newer, as declared in `pyproject.toml`. From the repository root, without installing a distribution:

```sh
PYTHONPATH=src python -c "from safestrip.format import clean; print(clean(' a '))"
```

Expected output:

```text
a
```

The command was executed in a controlled local fixture using Python 3.13.5. It was **not** tested as a published package installation, a Windows shell command or across the full supported version range. On Windows, set the module search path using the current shell's appropriate mechanism rather than assuming POSIX `PYTHONPATH=...` syntax works unchanged.

## Verify the example

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
```

The controlled fixture contains a passing source test of this one operation; the example does not establish the rest of a future library's quality.

## Source map

- `pyproject.toml`: package identity and declared Python version floor.
- `src/safestrip/format.py`: the implementation of `clean`.
- `tests/test_format.py`: the demonstrated operation's regression test.

## Project status and contributing

This is a controlled source-checkout example, not a verified published package. The source snapshot provides no evidenced public release, license, contact address, support policy, contribution workflow or security guarantee. Review actual source and repository governance before depending on it or submitting changes.
