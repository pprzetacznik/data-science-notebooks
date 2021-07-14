import os
from pkg_resources import resource_filename


def resource_filepath(filename, package="tests", subdirectory="resources"):
    return resource_filename(package, os.path.join(subdirectory, filename))


def resource_file_content(filepath):
    with open(filepath) as f:
        return f.read()


def remove_file(filepath):
    os.remove(filepath)
