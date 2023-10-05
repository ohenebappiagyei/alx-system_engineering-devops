#!/usr/bin/python3


import importlib.util


def import_variable_from_file(filename):
    spec = importlib.util.spec_from_file_location("variable_module", filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return (module.a)


if __name__ == "__main__":
    value_of_a = import_variable_from_file("variable_load_5.py")
    print(value_of_a)
