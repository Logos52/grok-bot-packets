# 字 Vở tập viết HSK

Vở ô ly luyện viết chữ Hán cho người Việt. Chạy trên máy tính và điện thoại, không cần cài đặt, không cần build.

- **Bìa vở**: vào trang là thấy quyển vở tập viết (ghi được họ tên, lớp trên nhãn vở). Bấm vào bìa để lật mở.
- **Trang vở A4 kẻ ô ly**: mỗi chữ một ô 田 (hoặc 米), pinyin tô màu theo thanh điệu nằm trên mỗi chữ,
  chữ xếp từ trái qua phải, hết dòng thì xuống dòng.
- **Ô nhập chữ Hán**: gõ hoặc dán đoạn chữ Hán cần tập viết.
- **Viết**: viết mẫu lần lượt từng nét, từng chữ, từ trái qua phải, từ trên xuống dưới. Xong chữ này mới sang chữ kia.
- **Tập viết**: bạn tự viết lại từng chữ bằng chuột hoặc ngón tay. Sai 2 lần thì nét cần viết tự nháy sáng; có nút
  **Gợi ý**, **Bỏ qua**, đếm số lần sai từng chữ và tổng kết cuối bài, kèm nút **Tập lại chữ sai**.
- **Xoay ngang (điện thoại)**: nút xoay màn hình sang ngang (Android; iPhone thì tự xoay máy). Khi máy nằm ngang,
  **Viết** và **Tập viết** chạy trên bảng viết lớn cao gần hết màn hình, các nút nằm ở cột bên phải.
- **Bộ thủ & cấu tạo chữ** bên dưới trang vở: mỗi chữ một thẻ gồm thứ tự nét (Viết / Tập viết), pinyin, âm Hán Việt,
  loại chữ (tượng hình, hội ý, hình thanh…), nghĩa, cách đọc khác, bộ thủ, các thành phần, kiểu cấu trúc và lời giải thích.
- Tuỳ chọn: tốc độ viết mẫu, cỡ ô, kiểu ô 田/米, bật/tắt pinyin, tô đỏ bộ thủ, chữ mờ để tô theo, in trang vở.
- Giao diện sáng/tối, nghe đọc cả đoạn, cài lên điện thoại như ứng dụng (PWA), dùng offline sau lần mở đầu.

---

## 1. Chạy thử trên máy

**Cách 1: mở trực tiếp.** Nhấp đúp `index.html` (nên dùng **Microsoft Edge** hoặc **Google Chrome**).

**Cách 2: chạy server tĩnh** (nên dùng: chế độ offline chỉ chạy qua `localhost` hoặc HTTPS).
Mở PowerShell trong thư mục này:

```bash
powershell -ExecutionPolicy Bypass -File tools/serve.ps1
```

Sau đó mở <http://localhost:5174>. Thêm `#vo` vào cuối địa chỉ (`http://localhost:5174/#vo`) để bỏ qua bìa, vào thẳng trang vở.

## 2. Đưa lên GitHub Pages

Giống dự án HSK Flashcard: đẩy **nội dung thư mục `hsk-notebook`** lên gốc một repo, rồi vào
**Settings → Pages → Deploy from a branch → main / (root)**. Web chạy tại `https://<ten-cua-ban>.github.io/<repo>/`.

> Mỗi lần cập nhật nội dung, hãy tăng `VERSION` trong `sw.js` để máy người dùng tải bản mới.

## 3. Thứ tự nét và tập viết

Hoạt hình và chấm nét dùng [Hanzi Writer](https://hanziwriter.org). Dữ liệu nét của từng chữ tải từ CDN khi cần,
nên cần mạng ở lần đầu gặp chữ đó (sau đó được lưu lại nếu chạy qua HTTPS/localhost).
Chữ không có dữ liệu nét (chữ rất hiếm) vẫn hiện ở dạng tĩnh và được bỏ qua khi viết mẫu.

## 4. Dữ liệu chữ Hán

| Tệp | Nội dung | Nguồn |
|---|---|---|
| `data/radicals.js` | 214 bộ thủ Khang Hy: tên Hán Việt, nghĩa, số nét, biến thể, gợi ý | Biên soạn (dựa trên HSK Flashcard) |
| `data/curated.js` | Giải thích bộ thủ & cấu tạo viết tay cho 348 chữ HSK 1–2 | Dự án HSK Flashcard |
| `data/hanzi-1.js` | 3.500 chữ thông dụng cấp 1 của 通用规范汉字表 | Tự động tạo |
| `data/hanzi-2.js` | 4.605 chữ còn lại (chỉ tải khi gặp chữ không có ở trên) | Tự động tạo |
| `data/words.js` | Pinyin theo ngữ cảnh của ~1.100 từ HSK (觉得 = jué de, 银行 = yín háng) | Tự động tạo |

Chữ có trong `curated.js` dùng lời giải thích viết tay. Các chữ khác dùng lời giải thích tạo tự động từ dữ liệu cấu tạo
(ví dụ: *“Chữ hình thanh: 口 (bộ Khẩu – cái miệng) gợi nghĩa, 米 (mǐ · MỄ) gợi âm”*).

**Tạo lại dữ liệu tự động** (cần Perl, có sẵn trong Git Bash): tải các nguồn dưới đây vào một thư mục
(`unihan/` giải nén từ `Unihan.zip`, `mmah_dictionary.txt`, `CVDICT.u8`, `hanviet.csv`, `hsk_complete.min.json`) rồi chạy:

```bash
perl tools/build-data.pl <thư mục nguồn> data --curated-from ../hsk-flashcard
```

## 5. Cấu trúc thư mục

```
hsk-notebook/
├── index.html               Khung trang: bìa vở (HTML tĩnh, hiện ngay) + trang vở
├── manifest.webmanifest     Thông tin cài đặt ứng dụng (PWA)
├── sw.js                    Service worker, dùng offline
├── assets/icons/            Favicon, icon ứng dụng
├── css/
│   ├── tokens.css           Màu, font, bóng; màu vở ô ly và bìa vở; giao diện sáng/tối
│   ├── base.css · layout.css
│   └── components/          controls · cover · notebook · analysis · overlays
├── js/
│   ├── core/                namespace · dom (template an toàn) · icons · store
│   ├── services/            storage · loader · pinyin · speech · hanzi · strokes
│   ├── components/          cover · header · notebook · analysis · toast
│   └── app.js               Khởi động: store + actions
├── data/                    radicals · curated · hanzi-1 · hanzi-2 · words
└── tools/
    ├── serve.ps1            Server tĩnh để chạy thử (cổng 5174)
    └── build-data.pl        Tạo dữ liệu chữ Hán từ các nguồn mở
```

**Kiến trúc**: JavaScript thuần, không framework, không bước build, cùng cách tổ chức với HSK Flashcard
(namespace `HSK`, store + actions, template tự escape). Dữ liệu chữ Hán được nạp khi cần để bìa vở hiện ngay.

## 6. Nguồn & giấy phép

- Hoạt hình thứ tự nét: [Hanzi Writer](https://hanziwriter.org) (MIT); dữ liệu nét và cấu tạo chữ
  [Make Me a Hanzi](https://github.com/skishore/makemeahanzi) (Arphic Public License / LGPL).
- Nghĩa tiếng Việt: [CVDICT](https://github.com/ph0ngp/CVDICT) © Phong Phan (CC BY-SA 4.0), dịch từ CC-CEDICT.
- Âm Hán Việt theo pinyin: [hanviet-pinyin-wordlist](https://github.com/ph0ngp/hanviet-pinyin-wordlist) © Phong Phan (MIT).
- Cách đọc, số nét, bộ thủ, bảng 通用规范汉字表: [Unicode Unihan](https://www.unicode.org/charts/unihan.html) (Unicode License v3).
- Pinyin theo từ: [complete-hsk-vocabulary](https://github.com/drkameleon/complete-hsk-vocabulary) (MIT).
- Các tệp `data/hanzi-*.js` chứa nghĩa lấy từ CVDICT nên phát hành theo **CC BY-SA 4.0**.
- Phông chữ: Be Vietnam Pro, Noto Serif SC (SIL Open Font License) qua Google Fonts.
