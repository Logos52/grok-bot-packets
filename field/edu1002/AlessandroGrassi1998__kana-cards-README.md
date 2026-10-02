# Kana cards

Flashcards for learning Japanese: hiragana, 100 common words, and a pair mode where two phones share one card.

## Files

- `index.html` – the whole app
- `peerjs.min.js` – PeerJS 1.5.5 (MIT license), used for the phone-to-phone connection in pair mode

## Publish on GitHub Pages

1. Create a new **public** repository (for example `kana-cards`).
2. Click **Add file → Upload files**, drag in `index.html`, `peerjs.min.js` and this README, then **Commit changes**.
3. Go to **Settings → Pages**. Under "Build and deployment", set **Source** to *Deploy from a branch*, branch **main**, folder **/ (root)**, and click **Save**.
4. After a minute or two the app is live at `https://<your-username>.github.io/kana-cards/`.

## How pair mode connects

The free PeerJS cloud service (0.peerjs.com) is used only to introduce the two phones. After that, cards and answers travel directly between the phones over WebRTC. Being on the same Wi-Fi makes the connection most reliable.

To use your own PeerJS server instead, add parameters to the URL:
`?peerHost=your.server.com&peerPort=443&peerPath=/`

A join link looks like `https://<your-username>.github.io/kana-cards/?join=ABCDE`.
