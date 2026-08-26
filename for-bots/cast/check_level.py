#!/usr/bin/env python3
"""check_level.py — known-vocabulary gate for Chinese messages to Wedge. Stdlib only.

Modes
  gate     (default) rewrite until at most --max-new new words; also fails a message of
           8+ words whose known-ratio is under --floor.
  natural  write freely; report new words as a review list (word · pinyin · gloss);
           fails only when known-ratio is under --floor.
  word     one word: prints KNOWN, LEARNING, or NEW <word> · <pinyin> · <gloss>.
           exit 0 for KNOWN/LEARNING, 1 for NEW. For XIAOTU's cross-check.

Segmentation: longest match against the known list; punctuation, digits and Latin are
boundaries that no word may cross; runs the known list cannot cut are re-cut against the
dictionary word list; a dictionary word the known list cut in half (發 + 射) is re-joined.
Cast names are exempt from the count. A message with no Chinese content fails.

Usage:  python3 check_level.py "<text>"      echo text | python3 check_level.py -
        python3 check_level.py --mode natural --floor 0.90 "<text>"
        python3 check_level.py --mode word "衛星"
Exit: 0 PASS/KNOWN, 1 FAIL/NEW, 2 setup error (lexicon missing).
"""
import sys, json, os, argparse

CAST = {"沈文","阮草","星野遙香","星野","金多恩","多恩","阿迪","白龍","林薇","小圖","蘇老師","吳老闆","橘將軍"}
PUNCT = set("，。！？、；：「」『』（）()《》〈〉…⋯—～~ 　\t\n\r:!?,.·－_/\\\"'0123456789０１２３４５６７８９%％ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
B = "\x00"  # boundary marker

def load(path):
    if not os.path.exists(path):
        print(f"FAIL: lexicon not found at {path}"); sys.exit(2)
    d = json.load(open(path, encoding="utf-8"))
    known = set(d.get("known", [])); learning = set(d.get("learning", []))
    return known, learning, set(ch for w in known for ch in w)

def load_dict(path):
    D = {}
    if not path or not os.path.exists(path): return D
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip(): continue
        p = line.rstrip("\n").split("\t")
        if p and p[0] and p[0] not in D: D[p[0]] = (p + ["", "", ""])[1:4]
    return D

def _longest(text, vocab, maxlen=6):
    """Longest match; every punctuation/digit/Latin character becomes one boundary marker."""
    i, out = 0, []
    while i < len(text):
        ch = text[i]
        if ch in PUNCT:
            if not out or out[-1] != B: out.append(B)
            i += 1; continue
        hit = None
        for L in range(min(maxlen, len(text) - i), 0, -1):
            w = text[i:i+L]
            if w in vocab and B not in w: hit = w; break
        if hit is None: hit = ch
        out.append(hit); i += len(hit)
    return out

def segment(text, vocab, D):
    toks = _longest(text, vocab)
    dictset = set(D)
    out, run = [], ""
    def flush():
        nonlocal run
        if run:
            out.extend(_longest(run, dictset) if dictset else [run]); run = ""
    for t in toks:
        if t == B: flush(); out.append(B)
        elif t in vocab: flush(); out.append(t)
        else: run += t
    flush()
    # re-join a dictionary word the known list cut in half, never across a boundary
    i = 0
    while i < len(out):
        t = out[i]
        if t != B and t not in vocab:
            if i > 0 and out[i-1] != B and out[i-1] in vocab and (out[i-1]+t) in dictset and (out[i-1]+t) not in vocab:
                out[i-1:i+1] = [out[i-1]+t]; continue
            if i+1 < len(out) and out[i+1] != B and out[i+1] in vocab and (t+out[i+1]) in dictset and (t+out[i+1]) not in vocab:
                out[i:i+2] = [t+out[i+1]]; continue
        i += 1
    return [t for t in out if t != B]

def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("text")
    ap.add_argument("--lexicon", default=os.path.join(here, "level-lexicon.json"))
    ap.add_argument("--dict", default=os.path.join(here, "dict-words.tsv"))
    ap.add_argument("--mode", choices=["gate", "natural", "word"], default="gate")
    ap.add_argument("--max-new", type=int, default=2)
    ap.add_argument("--floor", type=float, default=0.90)
    a = ap.parse_args()
    text = sys.stdin.read() if a.text == "-" else a.text
    known, learning, chars = load(a.lexicon)
    D = load_dict(a.dict)
    vocab = known | learning | CAST
    toks = segment(text, vocab, D)
    content = [t for t in toks if t not in CAST]

    if a.mode == "word":
        w = text.strip()
        if not w or all(ch in PUNCT for ch in w): print("FAIL: no Chinese content"); sys.exit(1)
        if w in known: print("KNOWN"); sys.exit(0)
        if w in learning: print("LEARNING"); sys.exit(0)
        if content and all(t in known or t in learning for t in content):
            print("KNOWN (all parts known: " + " ".join(content) + ")"); sys.exit(0)
        g = D.get(w)
        print("NEW " + w + (f" · {g[0]} · {g[1]}" if g else " · (not in dictionary; gloss by hand)")); sys.exit(1)

    total = len(content)
    if total == 0: print("FAIL: no Chinese content"); sys.exit(1)
    new_words = sorted(set(t for t in content if t not in known and t not in learning))
    new_chars = sorted(set(ch for t in content for ch in t if ch not in chars and ch not in PUNCT))
    bad = sum(1 for t in content if t in new_words)
    ratio = (total - bad) / total
    head = f"words {total} · known-ratio {ratio:.2f} · new words {len(new_words)}"
    if a.mode == "gate": head += f" (max {a.max_new})"
    print(head + f" · new chars {len(new_chars)}")
    if new_words: print("NEW WORDS:", " ".join(new_words))
    if new_chars: print("NEW CHARS:", " ".join(new_chars))
    if a.mode == "natural":
        print("REVIEW LIST (append under 生詞, one per line: word · pinyin · gloss):")
        for w in new_words:
            g = D.get(w); print("  -", w, "·", g[0], "·", g[1]) if g else print("  -", w, "· (not in dictionary; gloss by hand)")
        ok = ratio >= a.floor
        print("PASS" if ok else f"FAIL: known-ratio {ratio:.2f} is under the floor {a.floor:.2f}, simplify the sentences that carry the most new words")
        sys.exit(0 if ok else 1)
    ok = len(new_words) <= a.max_new and (total < 8 or ratio >= a.floor)
    if ok: print("PASS")
    elif len(new_words) > a.max_new: print(f"FAIL: rewrite so that at most {a.max_new} words are new, and gloss each new word once in brackets")
    else: print(f"FAIL: known-ratio {ratio:.2f} is under the floor {a.floor:.2f}")
    sys.exit(0 if ok else 1)

if __name__ == "__main__": main()
