import re, glob
files = sorted(glob.glob("/workspace/field/atom-*-20260906.xml")) + ["/workspace/field/atom-mansour-master-20260906.xml"]
for f in files:
    try:
        data = open(f, errors="replace").read()
    except Exception as e:
        print("====", f, "ERR", e)
        continue
    print("====", f, "bytes", len(data))
    if "Not Found" in data or len(data) < 50:
        print("  EMPTY/404")
        continue
    entries = re.findall(r"<entry>(.*?)</entry>", data, re.S)
    for e in entries[:6]:
        title = re.search(r"<title[^>]*>(.*?)</title>", e, re.S)
        updated = re.search(r"<updated>(.*?)</updated>", e)
        author = re.search(r"<name>(.*?)</name>", e)
        link = re.search(r'href="(https://github.com/[^"]+/commit/[^"]+)"', e)
        t = (title.group(1).strip() if title else "?")[:120]
        u = updated.group(1) if updated else "?"
        a = author.group(1) if author else "?"
        l = link.group(1) if link else "?"
        print(f"  {u} | {a} | {t}")
        print(f"    {l}")
