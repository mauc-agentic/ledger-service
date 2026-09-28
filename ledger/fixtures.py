"""Carga los datos de referencia (cuentas) desde un archivo YAML."""

import yaml


def load_fixtures(path):
    with open(path) as f:
        return yaml.load(f)
