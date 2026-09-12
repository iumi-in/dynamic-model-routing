"""Build the deterministic plugin distribution archive."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate import EXPECTED_FILES, validate


REPOSITORY = Path(__file__).resolve().parents[1]
DEFAULT_ROOT = REPOSITORY / "plugins/dynamic-model-routing"
DEFAULT_OUTPUT = REPOSITORY / "output/plugins/dynamic-model-routing-0.1.0.zip"
ARCHIVE_TIMESTAMP = (2026, 9, 12, 0, 0, 0)


def build(root: Path, output: Path) -> None:
    errors = validate(root)
    if errors:
        raise ValueError("Invalid package:\n" + "\n".join(errors))

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(EXPECTED_FILES):
            info = ZipInfo(name, ARCHIVE_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (root / name).read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        build(args.root.resolve(), args.output.resolve())
    except (OSError, ValueError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(f"Built {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
