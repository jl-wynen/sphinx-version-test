import argparse
import json
from pathlib import Path
import string


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=Path, required=True, help="Path of repo")
    parser.add_argument("--url", type=str, required=True, help="URL to deployed docs")
    return parser.parse_args()


def get_versions(base_path: Path):
    return [
        path.name
        for path in base_path.iterdir()
        if path.is_dir() and not path.name.startswith("_") and not path.name.startswith(".")
    ]


def read_version_switcher_template():
    with open(Path(__file__).resolve().parent / "templates/version-switcher.json.template",
              "r") as f:
        return string.Template(f.read())


def make_version_switcher(*, versions, url, base):
    template = read_version_switcher_template()
    switcher = [json.loads(template.substitute(VERSION=version, URL=url))
                for version in sorted(versions)]
    with open(base/"_static/version-switcher.json", "w") as f:
        json.dump(switcher, f)


def read_index_template():
    with open(Path(__file__).resolve().parent / "templates/index.html.template",
              "r") as f:
        return string.Template(f.read())


def make_index(*, versions, url, base):
    template = read_index_template()
    latest_version = sorted(versions)[-1]
    index = template.substitute(BASE_URL=url, VERSION=latest_version)
    with open(base/"index.html", "w") as f:
        f.write(index)


def main():
    args = parse_args()
    versions = get_versions(args.base)
    make_version_switcher(versions=versions, url=args.url, base=args.base)
    make_index(versions=versions, url=args.url, base=args.base)


if __name__ == '__main__':
    main()
