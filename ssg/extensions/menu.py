from typing import Callable, Any

from ssg import parsers, hooks

files = []


@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: isinstance(p, parsers.ResourceParser)
    valid = not valid
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parsers)):
            if path.suffix in parser.valid_file_ext():
                files.append(path)
