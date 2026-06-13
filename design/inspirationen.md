# Inspirations-Analyse

Stand: 2026-06-12. Analysierte Referenzen (von Svenja ausgewählt) plus ihre
Notizen dazu. Technische Analyse per HTML/CSS-Auswertung der Live-Seiten.

## Svenjas Notizen (Original)

Zu The Light Seeker (why-choose-me + elopement-planning):

> „Die finde ich ganz nice, vor allem die Linien und Schrift im Bild (nicht
> unbedingt den Frame mit Bildern). Die Fotos, die die Abschnitte ‚trennen'
> finde ich auch nice und unter ‚elopements' mag ich sehr, wie das Foto in
> den Hintergrund übergeht: love it"

Wünsche:

- sehr minimalistisch, soll nicht overwhelming sein
- Foto und Hintergrund ineinanderblenden wie bei amourfotografie.com
- Testimonials-Teil
- Q&A-Teil mit Antworten zu oft gestellten Fragen
- „Get in touch"-Part mit Anfrage-Formular
- (erstmal eine) ganze Reportage zum Durchklicken
- Socials verlinken

---

## Referenz 1+2: thelightseeker.photography

Seiten: `/why-choose-me/`, `/your-elopement-planning-start-here/`

**Plattform**: WordPress mit Divi-Theme (für uns nur als Muster relevant,
nicht als Technik).

**Typografie**:

- Headlines: **Playfair Display** (elegante Serif, hohe Strichstärken-Kontraste)
- Fließtext: **Open Sans** (neutrale Sans-Serif)
- Muster: große Serif-Headlines, darüber/darunter kleine Label in
  Versalien mit weiter Laufweite („Eyebrow"-Zeilen)

**Farben**:

- Weiß/Off-White-Flächen, fast-schwarzer Text (`#08090a`)
- Akzente: Salbei-/Olivgrün (`#9aaf72`, `#6e783c`), Bronze/Gold-Töne
  (`#BF995F`, `#ad853a`), Taupe (`#8f8873`)
- Wirkung: warm, naturnah, editorial

**Layout-Muster, die Svenja gefallen** (und die wir übernehmen):

1. **Dünne Linien + Schrift im Bild**: Text-Overlays auf Fotos, kombiniert
   mit feinen horizontalen/vertikalen Linien (1px) — wirkt wie ein
   Magazin-Layout, gibt Bildern Struktur ohne Rahmen-Deko.
2. **Vollbreite Foto-Trenner**: Zwischen Inhaltssektionen stehen volle
   Bildstreifen (Full-Bleed) statt Linien oder Farbflächen — das Portfolio
   selbst gliedert die Seite.
3. **Foto-in-Hintergrund-Übergang** (Abschnitt „Elopements"): Bild läuft
   weich in die Hintergrundfarbe der Seite aus statt hart zu enden.
3b. **Content scrollt über das Hintergrundbild** (Nachtrag Svenja,
   2026-06-12): Das Hero-Bild bleibt beim Scrollen stehen, die folgende
   Sektion (inkl. der hineinragenden Galerie-Kacheln) schiebt sich
   darüber — Fixed-Background-/Reveal-Effekt, in Wix als Scroll-Effekt
   „Reveal"/„Parallax" verfügbar.
4. Erzählstruktur: abwechselnd Text-Sektion → Bildstreifen → Text-Sektion;
   Headlines stellen Nutzen/Gefühl in den Vordergrund („A Wedding Day That
   Breathes", „Presence Over Performance" — passt inhaltlich exakt zu
   Sejas Positionierung).

**Nicht übernehmen** (explizit bzw. No-Go-Abgleich):

- Collagen-„Frames" mit mehreren gerahmten Bildern (Svenja: ausdrücklich nicht)
- Die Standard-Divi-Blautöne bei Links (`#2ea3f2`) — Fremdkörper
- Awards-/Accomplishments-Block (für den Start nicht relevant)
- Insgesamt textlastige, lange Seiten — Svenja will minimalistischer bleiben

---

## Referenz 3: amourfotografie.com

**Plattform: Wix!** — wichtigster Befund: Diese Referenz ist selbst eine
Wix-Site. Alles, was Svenja daran mag, ist nachweislich im Wix-Editor baubar.

**Typografie**:

- Serif-Familien: **Cormorant Garamond Light**, Forum, EB Garamond
- Sans-Serif: Raleway, Avenir Light, DIN Next Light, Helvetica Light
- Wirkung: leichte, luftige Serifen + sehr leichte Sans → ruhig und hochwertig

**Farben**:

- Weißer/heller Hintergrund, Text in warmem Dunkelgrau `rgb(47,46,46)`
  statt hartem Schwarz — genau die „weichen Kontraste" aus dem Briefing

**Der Foto-Fade-Effekt** (Svenjas „love it"): technisch gelöst über
**lineare Gradient-Overlays in der Hintergrundfarbe** über dem Bild:
`linear-gradient(rgba(255,255,255,0) → rgba(255,255,255,0.7))`. Das Bild
endet nicht an einer Kante, sondern löst sich in die Seitenfarbe auf.
→ In Wix umsetzbar (siehe designrichtung.md, Abschnitt „Foto-Fade").

---

## Synthese: gemeinsamer Nenner der Referenzen

Beide Referenzen treffen dieselbe Richtung, die auch das Briefing vorgibt:

| Element | Light Seeker | Amour | Briefing |
|---|---|---|---|
| Serif-Display-Headlines | Playfair Display | Cormorant Garamond | „elegante Serif" |
| Leichte Sans für Text | Open Sans | Raleway/Avenir Light | „gut lesbare Sans" |
| Weiche Kontraste | #08090a auf Weiß | rgb(47,46,46) auf Weiß | „kein hartes S/W" |
| Warme, gedämpfte Akzente | Olive/Bronze/Taupe | sehr reduziert | Terracotta/Olive/Taupe |
| Bilder gliedern die Seite | Full-Bleed-Trenner | Fades in Hintergrund | „viel Raum für Bilder" |
| Editorial-Codes | Linien + Eyebrows | luftige Typo | „emotional editorial" |

Daraus abgeleitete Designrichtung: siehe `design/designrichtung.md`.

## Offene Punkte

- **Brandkit kommt noch** (Logo + Typografie von Svenja, via Hagen):
  Farb- und Schriftvorschläge in der Designrichtung sind Platzhalter, bis
  das Brandkit da ist — dann abgleichen und ggf. anpassen.
- Weiteres Bildmaterial kommt per Google Drive (u. a. für die
  Klick-Reportage).
