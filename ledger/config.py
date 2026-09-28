"""Carga la configuración del servicio desde un archivo YAML."""

import yaml


def load_config(path):
    with open(path) as f:
        return yaml.load(f)
