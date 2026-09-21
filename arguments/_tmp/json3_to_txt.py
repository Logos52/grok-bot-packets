from pathlib import Path
import json, sys

def json3_to_txt(json3_path, out_path):
    data = json.loads(Path(json3_path).read_text())
    events = data.get("events") or []
    lines = []
    for ev in events:
        segs = ev.get("segs")
        if not segs:
            continue
        t = ev.get("tStartMs", 0)
        text = "".join(s.get("utf8", "") for s in segs)
        text = text.replace("\n", " ").strip()
        if not text:
            continue
        total_s = t // 1000
        h, rem = divmod(total_s, 3600)
        m, s = divmod(rem, 60)
        ts = f"[{h}:{m:02d}:{s:02d}]" if h else f"[{m:02d}:{s:02d}]"
        lines.append(f"{ts} {text}")
    Path(out_path).write_text("\n".join(lines) + ("\n" if lines else ""))
    return len(lines)

if __name__ == "__main__":
    n = json3_to_txt(sys.argv[1], sys.argv[2])
    print(n)
