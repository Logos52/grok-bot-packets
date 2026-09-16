# Dcard harvest 2026-08-28 (Asia/Taipei)

Thorough retry after the 06:00 stub. Page-level Chrome and desktop Chrome both hit a hard Cloudflare deny on every dcard.tw URL. No challenge, captcha, or login. No post bodies. Nothing invented.

## access
- page-level Chrome: blocked (https://www.dcard.tw/f/talk, title "Attention Required! | Cloudflare")
- desktop Chrome: blocked (same text on /f/talk, /, /f, /f/food)
- https://m.dcard.tw/f/talk: does not resolve (DNS_PROBE_FINISHED_NXDOMAIN)
- visible text: Sorry, you have been blocked / You are unable to access dcard.tw
- Cloudflare Ray ID (page-level): a321c5deaba8503f

## talk
- status: blocked
- url: https://www.dcard.tw/f/talk
- body: blocked

## relationship
- status: blocked
- url: https://www.dcard.tw/f/relationship
- body: blocked

## job
- status: blocked
- url: https://www.dcard.tw/f/job
- body: blocked

## mood
- status: blocked
- url: https://www.dcard.tw/f/mood
- body: blocked

## food
- status: blocked
- url: https://www.dcard.tw/f/food
- body: blocked

## 3c
- status: blocked
- url: https://www.dcard.tw/f/3c
- body: blocked
