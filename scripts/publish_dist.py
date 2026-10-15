#!/usr/bin/env python3
"""Copy Astro's dist/ output to the repository root for branch-based Pages deploy.

GitHub Pages is currently served from the repository root. Source directories and
project files remain untouched; only generated static-site paths are overwritten.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
MANIFEST = ROOT / '.astro-build-manifest.json'
PROTECTED = {
    '.astro', '.astro-build-manifest.json', '.git', '.gitignore', '.github',
    'astro.config.mjs', 'build.py', 'dist', 'make_assets.py', 'make_og.py',
    'node_modules', 'package-lock.json', 'package.json', 'public', 'README.md',
    'SEO.md', 'scripts', 'src', 'tsconfig.json'
}


def protected_path(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return relative.parts[0] in PROTECTED


def remove_empty_parents(path: Path) -> None:
    parent = path.parent
    while parent != ROOT:
        if protected_path(parent) or any(parent.iterdir()):
            return
        parent.rmdir()
        parent = parent.parent


def clean_previous(current: set[str]) -> None:
    if not MANIFEST.exists():
        return
    previous = set(json.loads(MANIFEST.read_text(encoding='utf-8')))
    for relative in sorted(previous - current, reverse=True):
        target = ROOT / relative
        if protected_path(target):
            continue
        if target.is_file() or target.is_symlink():
            target.unlink()
            remove_empty_parents(target)


def clean_unmanaged(current: set[str]) -> None:
    """First-run cleanup for a checkout that already contains old generated output."""
    for path in sorted((candidate for candidate in ROOT.rglob('*') if candidate.is_file()), reverse=True):
        relative = str(path.relative_to(ROOT))
        if relative in current or protected_path(path):
            continue
        path.unlink()
        remove_empty_parents(path)


def dist_files() -> list[Path]:
    if not DIST.is_dir():
        raise SystemExit('dist/ does not exist. Run: npx astro build')
    return sorted(path for path in DIST.rglob('*') if path.is_file())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean-only', action='store_true', help='remove files recorded by the previous root publish')
    args = parser.parse_args()

    if args.clean_only:
        clean_previous(set())
        MANIFEST.unlink(missing_ok=True)
        return

    files = dist_files()
    current = {str(path.relative_to(DIST)) for path in files}
    if MANIFEST.exists():
        clean_previous(current)
    else:
        clean_unmanaged(current)

    for source in files:
        relative = source.relative_to(DIST)
        target = ROOT / relative
        if protected_path(target):
            raise SystemExit(f'Refusing to overwrite project file: {relative}')
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    MANIFEST.write_text(json.dumps(sorted(current), indent=2) + '\n', encoding='utf-8')
    print(f'Published {len(files)} static files to repository root.')


if __name__ == '__main__':
    main()
