"""Build clip/latest.json from the published GitHub release event."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: update_feed.py <GitHub release event JSON>")
    event = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    release = event["release"]
    tag = release["tag_name"]
    match = re.fullmatch(r"zeus-clip-v(\d+\.\d+\.\d+)", tag)
    if not match:
        raise SystemExit(f"Tag Zeus Clip invalide : {tag}")

    version = match.group(1)
    expected_name = f"ZeusClip-{version}-Windows-x64.zip"
    asset = next((item for item in release.get("assets", [])
                  if item.get("name") == expected_name), None)
    if asset is None:
        raise SystemExit(f"Archive attendue absente de la release : {expected_name}")

    digest = asset.get("digest") or ""
    if digest.startswith("sha256:"):
        digest = digest[7:]
    feed = {
        "product": "zeus-clip",
        "name": "Zeus Clip",
        "version": version,
        "channel": "preview" if release.get("prerelease") else "stable",
        "available": True,
        "windows": "10/11 x64",
        "asset_name": asset["name"],
        "download_url": asset["browser_download_url"],
        "size_bytes": asset["size"],
        "sha256": digest,
        "released_at": release.get("published_at"),
        "message": "Version publiée.",
    }
    feed_path = Path("clip/latest.json")
    feed_path.parent.mkdir(parents=True, exist_ok=True)
    feed_path.write_text(
        json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

