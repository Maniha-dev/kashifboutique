KASHIF BOUTIQUE - DEMO WEBSITE
==============================
index.html  -> the finished website. One file, works offline. Double-click to open,
               or upload it to any hosting (Vercel, Netlify, cPanel) as index.html.

source/     -> editable project
  template.html   all HTML, CSS and JavaScript (products, prices, colours, phone number)
  frames/         120 frames of the scroll banner animation
  products/       product photos (12 products x 3 colours x 2 photos)
  build.py        run "python3 build.py" to rebuild ../index.html after edits

Common edits (in source/template.html)
- WhatsApp number: search for 923212365451 (also 0321-2365451) and replace.
- Products, prices, colours, descriptions: the "P=[" array in the script.
- Hero captions: the four <div class="ch"> blocks near the top of <main>.
- Address, hours and Google Map: the "Visit our boutique" section (map address is in the iframe src, q=...).
- Fonts load from Google Fonts (internet needed for fonts only).

Notes
- Product photos are sample images cut from the banner footage. Replace the
  files in source/products/ with real photos (same names), then run build.py.
- Checkout is WhatsApp-only: it opens a pre-filled message to the boutique number.

Google Map
- The live Google Map loads automatically when index.html is opened from your own
  hosting or a local file. Inside the Claude preview, outside content is blocked, so a
  styled map card with the Get directions / Open in Google Maps buttons shows instead.
