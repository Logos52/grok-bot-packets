# for-bots/bank — the research bank, box side

Copy this folder to /workspace/bank/ (後台 does this on "bank setup"). Layout on the box mirrors the Mac:

    /workspace/bank/raw/<lane>/<id>.md     bots write here, one file per source, block from SCHEMA.md on top
    /workspace/bank/cards/<lane>/<id>.md   the Mac sends these back; read only
    /workspace/bank/INDEX.md, index.jsonl  made by: python3 /workspace/bank/scripts/bank.py --root /workspace/bank --index
    /workspace/bank/scripts/bank.py        stdlib only
    /workspace/bank/SCHEMA.md

Write one item:

    python3 /workspace/bank/scripts/bank.py --root /workspace/bank --text --lane ai --via grok-bot/brief \
      --source "<url>" --title "<title>" --author "<author>" --published 2026-08-28 < body.txt

Lanes: ai learning politics money ideas culture yuedu cast gaming grok-bot misc.
Steward's weekday push carries /workspace/bank/raw/ up to this repo. The Mac pulls it and merges.
