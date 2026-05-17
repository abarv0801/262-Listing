# 262 Willowbrook — For Sale by Owner

A storytelling landing page for 262 Willowbrook Drive, North Brunswick, NJ 08902.

## Live site

Once GitHub Pages is enabled, the site will be available at:
`https://YOURUSERNAME.github.io/willowbrook-listing/`

## Structure

- `index.html` — the main page (HTML, CSS, JS all inline)
- `img/` — all photos referenced by the page
- `flyer.html` — printable single-page summary with QR code
- `qr-placeholder.png` — placeholder QR code (regenerate with `generate-qr.py` once your URL is live)
- `generate-qr.py` — Python script to regenerate the QR code

## Editing

All content lives in `index.html`. Open it in any text editor and edit directly.

Photos are referenced via relative paths (`img/01-exterior-spring.jpeg` etc.). To swap a photo, just replace the file in `img/` with one of the same name.

## Local preview

Just open `index.html` in a browser. No build step.

## Deployment

1. Push to GitHub
2. Repo Settings → Pages → Source: `main` branch, root folder
3. Wait 1–2 minutes
4. Done

## Regenerate the QR code

After deployment, run:

```bash
python3 generate-qr.py https://YOUR-LIVE-URL/
```

This updates `qr-placeholder.png` (you can rename to `qr.png` if you prefer). Then regenerate the flyer PDF.

## Contact

Phone/Text/WhatsApp: (971) 277-8212
