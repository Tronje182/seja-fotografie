#!/usr/bin/env python3
# Homepage-Entwurf "Quiet Editorial" für Seja Fotografie
# Setzt designrichtung.md v2 als statisches Mockup um (1440px breit).
from PIL import Image, ImageDraw, ImageFont, ImageOps

W = 1440
BG      = (244, 241, 238)   # F4F1EE Off-White
GREIGE  = (233, 226, 221)   # E9E2DD Fläche 2
INK     = (24, 23, 25)      # 181719 Fast-Schwarz
BODY    = (46, 43, 43)      # 2E2B2B Fließtext
ROSE    = (163, 129, 119)   # A38177 Dusty Rose
LINE    = (176, 153, 147)   # B09993 Greige-Linien
RUST    = (115, 46, 31)     # 732E1F Rostrot
PAPER   = (242, 242, 242)   # F2F2F2 Text auf Dunkel

FOTOS = "/tmp/drive/Seja Website/Fotos/"
ME    = "/tmp/drive/Seja Website/Me/"

def prata(s):   return ImageFont.truetype("/tmp/fonts/Prata.ttf", s)
def ral(s, w=400):
    f = ImageFont.truetype("/tmp/fonts/Raleway.ttf", s)
    f.set_variation_by_axes([w]); return f

def cover(path, w, h, fy=0.5):
    im = Image.open(path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, fy))

def tw(d, txt, font, ls=0):
    if ls == 0: return d.textlength(txt, font=font)
    return sum(d.textlength(c, font=font) + ls for c in txt) - ls

def text(d, xy, txt, font, fill, ls=0, anchor=None):
    x, y = xy
    if ls == 0:
        d.text((x, y), txt, font=font, fill=fill, anchor=anchor); return
    if anchor and "m" in anchor[0]: x -= tw(d, txt, font, ls) / 2
    for c in txt:
        d.text((x, y), c, font=font, fill=fill, anchor="l"+(anchor[1] if anchor else "a"))
        x += d.textlength(c, font=font) + ls

def center(d, y, txt, font, fill, ls=0):
    text(d, (W/2, y), txt, font, fill, ls, anchor="mm")

def vfade(img, x, y, w, h, color, top_to_bottom):
    grad = Image.new("RGBA", (w, h))
    g = ImageDraw.Draw(grad)
    for i in range(h):
        a = int(255 * (i / h)) if top_to_bottom else int(255 * (1 - i / h))
        g.line([(0, i), (w, i)], fill=color + (a,))
    img.alpha_composite(grad, (x, y))

logo_black = Image.open("/tmp/drive/Seja Website/Logos/seasalt (Instagram Story) (Logo).png").convert("RGBA")
logo_black = logo_black.crop(logo_black.getbbox())
logo_white = Image.open("/tmp/SEJA-Fotografie-Logo-weiss.png").convert("RGBA")
logo_white = logo_white.crop(logo_white.getbbox())
def logo_h(logo, h):
    return logo.resize((int(logo.width * h / logo.height), h), Image.LANCZOS)

H_TOTAL = 5760
page = Image.new("RGBA", (W, H_TOTAL), BG + (255,))
d = ImageDraw.Draw(page)
y = 0

# ---------- Header ----------
lg = logo_h(logo_black, 54)
page.alpha_composite(lg, (70, y + 23))
nav = ["HOCHZEITEN", "PORTRAITS & PAARE", "PORTFOLIO", "ÜBER SVENJA", "KONTAKT"]
nx = 430
for item in nav:
    text(d, (nx, y + 50), item, ral(13, 500), BODY, ls=2, anchor="lm")
    nx += tw(d, item, ral(13, 500), 2) + 38
# CTA ghost button
bw = 170; bx = W - 70 - bw
d.rectangle([bx, y + 30, bx + bw, y + 70], outline=RUST, width=1)
text(d, (bx + bw/2, y + 50), "ANFRAGE SENDEN", ral(12, 500), RUST, ls=2, anchor="mm")
y += 100

# ---------- Hero ----------
HH = 840
hero = cover(FOTOS + "DSC_2424.jpg", W, HH, fy=0.35).convert("RGBA")
scrim = Image.new("RGBA", (W, HH), (10, 8, 8, 80))
hero.alpha_composite(scrim)
page.alpha_composite(hero, (0, y))
hd = ImageDraw.Draw(page)
center(hd, y + 330, "HOCHZEITSFOTOGRAFIE · DEUTSCHLAND & NIEDERLANDE", ral(14, 500), PAPER, ls=4)
hd.line([(W/2 - 50, y + 372), (W/2 + 50, y + 372)], fill=PAPER, width=1)
center(hd, y + 442, "Nicht nur wie es aussah.", prata(58), PAPER)
center(hd, y + 522, "Sondern wie es sich angefühlt hat.", prata(58), PAPER)
vfade(page, 0, y + HH - 260, W, 260, BG, top_to_bottom=True)   # Foto-Fade
y += HH

# ---------- Intro ----------
y += 70
center(d, y + 20, "SEJA FOTOGRAFIE", ral(13, 500), ROSE, ls=4)
center(d, y + 80, "Bilder, die sich nach euch anfühlen.", prata(40), INK)
center(d, y + 150, "Ich begleite euch ruhig und aufmerksam — und halte die leisen,", ral(18, 300), BODY)
center(d, y + 182, "echten Momente fest, ohne dass ihr posen müsst.", ral(18, 300), BODY)
center(d, y + 248, "ÜBER SVENJA  ›", ral(13, 500), RUST, ls=3)
y += 340

# ---------- Foto-Trenner ----------
TH = 440
page.alpha_composite(cover(FOTOS + "DSC_6372.jpg", W, TH, fy=0.5).convert("RGBA"), (0, y))
y += TH

# ---------- Hochzeiten-Teaser ----------
y += 100
tx = 140
text(d, (tx, y), "HOCHZEITEN", ral(13, 500), ROSE, ls=4)
d.text((tx, y + 40), "Euer Tag, ruhig begleitet.", font=prata(38), fill=INK)
para = ["Vom Ankleiden bis zum letzten Tanz: dokumentarisch,",
        "nah und unaufdringlich. Ihr müsst nichts performen —",
        "ihr dürft einfach da sein."]
for i, ln in enumerate(para):
    d.text((tx, y + 122 + i * 32), ln, font=ral(18, 300), fill=BODY)
bw2 = 230
d.rectangle([tx, y + 250, tx + bw2, y + 296], outline=RUST, width=1)
text(d, (tx + bw2/2, y + 273), "MEHR ZU HOCHZEITEN", ral(12, 500), RUST, ls=2, anchor="mm")
tease = cover(FOTOS + "DSC_8476.jpg", 420, 540, fy=0.4)
page.alpha_composite(tease.convert("RGBA"), (W - 140 - 420, y - 30))
y += 600

# ---------- Reportage-Teaser ----------
y += 60
center(d, y, "EINE GANZE HOCHZEIT", ral(13, 500), ROSE, ls=4)
center(d, y + 56, "Von Anfang bis Ende — zum Durchklicken.", prata(36), INK)
thumbs = ["DSC_8183.jpg", "DSC_8297.jpg", "DSC_8266.jpg"]
tw_, th_, gap = 380, 300, 28
x0 = (W - 3 * tw_ - 2 * gap) / 2
for i, fn in enumerate(thumbs):
    page.alpha_composite(cover(FOTOS + fn, tw_, th_, fy=0.35).convert("RGBA"),
                         (int(x0 + i * (tw_ + gap)), y + 120))
center(d, y + 470, "ZUR REPORTAGE  ›", ral(13, 500), RUST, ls=3)
y += 540

# ---------- About (dunkle Kontrast-Sektion) ----------
y += 70
AH = 620
d.rectangle([0, y, W, y + AH], fill=INK)
por = cover(ME + "Svenja-62-2.jpg", 360, 480, fy=0.25)
page.alpha_composite(por.convert("RGBA"), (160, y + 70))
ax = 640
lgw = logo_h(logo_white, 64)
page.alpha_composite(lgw, (ax, y + 92))
d.text((ax, y + 196), "Ich bin Svenja.", font=prata(34), fill=PAPER)
ab = ["Mich interessiert, was zwischen Menschen passiert,",
      "wenn sie sich sicher fühlen. Die kleinen Blicke. Die Hände,",
      "die sich suchen. Der Moment, in dem Anspannung weich wird."]
for i, ln in enumerate(ab):
    d.text((ax, y + 268 + i * 32), ln, font=ral(18, 300), fill=PAPER)
text(d, (ax, y + 396), "MEHR ÜBER MICH  ›", ral(13, 500), ROSE, ls=3)
y += AH

# ---------- Testimonials ----------
TH2 = 400
d.rectangle([0, y, W, y + TH2], fill=GREIGE)
center(d, y + 90, "AUS EINER ZUSAMMENARBEIT", ral(13, 500), ROSE, ls=4)
center(d, y + 165, "„Svenja hat Momente gesehen,", prata(30), INK)
center(d, y + 215, "die wir selbst kaum bemerkt haben.“", prata(30), INK)
center(d, y + 285, "LISA & JONAS · HOCHZEIT IN KÖLN", ral(12, 500), BODY, ls=3)
for i in range(3):
    cx = W/2 - 24 + i * 24
    d.ellipse([cx - 3, y + 330, cx + 3, y + 336], fill=(LINE if i else RUST))
y += TH2

# ---------- Q&A ----------
y += 90
center(d, y, "Q&A", ral(13, 500), ROSE, ls=4)
center(d, y + 52, "Oft gestellte Fragen", prata(36), INK)
qs = ["Wie früh sollten wir anfragen?",
      "Was ist, wenn wir uns vor der Kamera unsicher fühlen?",
      "Begleitest du auch ganztägig?",
      "Wann bekommen wir die Bilder?"]
qx0, qx1 = 320, W - 320
qy = y + 130
for q in qs:
    d.text((qx0, qy), q, font=ral(18, 400), fill=BODY)
    d.text((qx1 - 14, qy - 2), "+", font=ral(22, 300), fill=ROSE)
    d.line([(qx0, qy + 44), (qx1, qy + 44)], fill=LINE, width=1)
    qy += 78
center(d, qy + 26, "ALLE FRAGEN  ›", ral(13, 500), RUST, ls=3)
y = qy + 100

# ---------- Get in touch ----------
y += 70
center(d, y, "GET IN TOUCH", ral(13, 500), ROSE, ls=4)
center(d, y + 56, "Erzählt mir von eurem Tag.", prata(40), INK)
center(d, y + 122, "Kein Funnel, keine Automatik — ihr schreibt, ich antworte persönlich.", ral(17, 300), BODY)
fx0, fx1 = 400, W - 400
fw = (fx1 - fx0 - 40) / 2
fy0 = y + 190
fields = [("NAME", "E-MAIL"), ("DATUM / ZEITRAUM", "ORT / LAND")]
for r, (a, b) in enumerate(fields):
    ry = fy0 + r * 90
    text(d, (fx0, ry), a, ral(11, 500), ROSE, ls=2)
    d.line([(fx0, ry + 42), (fx0 + fw, ry + 42)], fill=LINE, width=1)
    text(d, (fx0 + fw + 40, ry), b, ral(11, 500), ROSE, ls=2)
    d.line([(fx0 + fw + 40, ry + 42), (fx1, ry + 42)], fill=LINE, width=1)
ry = fy0 + 180
text(d, (fx0, ry), "EUER TAG IN EIN PAAR SÄTZEN", ral(11, 500), ROSE, ls=2)
d.line([(fx0, ry + 42), (fx1, ry + 42)], fill=LINE, width=1)
bw3 = 230; bx3 = W/2 - bw3/2; by3 = ry + 90
d.rectangle([bx3, by3, bx3 + bw3, by3 + 50], fill=RUST)
text(d, (W/2, by3 + 25), "ANFRAGE SENDEN", ral(12, 500), PAPER, ls=2, anchor="mm")
y = by3 + 130

# ---------- Footer ----------
FH = H_TOTAL - y
d.rectangle([0, y, W, y + FH], fill=INK)
lgf = logo_h(logo_white, 72)
page.alpha_composite(lgf, (int(W/2 - lgf.width/2), y + 48))
center(d, y + 160, "NICHT NUR WIE ES AUSSAH. SONDERN WIE ES SICH ANGEFÜHLT HAT.", ral(11, 400), (LINE), ls=3)
# Instagram-Icon (Linienstil)
icx, icy = W/2, y + 205
d.rounded_rectangle([icx - 11, icy - 11, icx + 11, icy + 11], radius=6, outline=LINE, width=1)
d.ellipse([icx - 5, icy - 5, icx + 5, icy + 5], outline=LINE, width=1)
d.ellipse([icx + 5.5, icy - 7.5, icx + 8.5, icy - 4.5], fill=LINE)
center(d, y + 248, "IMPRESSUM    ·    DATENSCHUTZ", ral(11, 400), LINE, ls=2)

page.convert("RGB").save("/tmp/entwurf_homepage.jpg", quality=90)
print("OK", page.size)
