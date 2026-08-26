import subprocess
tracked = subprocess.check_output(["git","ls-files"], text=True).splitlines()
wiki = [f for f in tracked if f.startswith("wiki/") and f.endswith(".md")]
print("tracked", len(tracked))
print("wiki", len(wiki))
glob = subprocess.check_output(["git","ls-files","wiki/**/*.md"], text=True).splitlines()
print("glob", len(glob))
print("only python", set(wiki)-set(glob))
print("only glob", set(glob)-set(wiki))
