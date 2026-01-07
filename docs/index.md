# k3utfjson

[![Action-CI](https://github.com/pykit3/k3utfjson/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3utfjson/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3utfjson/badge/?version=stable)](https://k3utfjson.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3utfjson)](https://pypi.org/project/k3utfjson)

JSON dump and load with enforced UTF-8 encoding.

k3utfjson is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3utfjson
```

## Quick Start

```python
import k3utfjson

# Load JSON from string (UTF-8)
data = k3utfjson.load('"hello 世界"')
print(data)  # hello 世界

# Dump to JSON string (UTF-8)
json_str = k3utfjson.dump({'msg': '你好'})
print(json_str)  # {"msg": "你好"}
```

## API Reference

::: k3utfjson

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
