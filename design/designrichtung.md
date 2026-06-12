# Designrichtung v1 — „Quiet Editorial"

Stand: 2026-06-12. Abgeleitet aus dem Onboarding-Briefing
(`briefing/onboarding-briefing.md`) und der Inspirations-Analyse
(`design/inspirationen.md`). **Vorbehalt**: Farb- und Schriftwahl sind
Vorschläge, die nach Eintreffen von Svenjas Brandkit (Logo, Typografie)
abgeglichen werden müssen.

## Leitidee

Ein ruhiges, warmes Magazin-Layout, in dem die Fotos die Seite gliedern —
nicht Boxen, Rahmen oder Deko. Wenige Elemente pro Sektion, viel Weißraum,
feine Linien als einziges grafisches Schmuckelement. Jede Seite führt leise,
aber klar zur Anfrage.

Ein Satz als Prüfstein für jede Designentscheidung:
**„Würde das in einem ruhigen Bildband stehen — oder ist es Template-Deko?"**

## Farbpalette (Vorschlag, bis Brandkit da ist)

| Rolle | Farbe | Hex | Verwendung |
|---|---|---|---|
| Hintergrund | warmes Off-White | `#F7F4EF` | Seitenhintergrund überall — wichtig für den Foto-Fade |
| Fläche 2 | Sand/Creme | `#ECE5DA` | ruhige Wechsel-Sektionen (z. B. Testimonials) |
| Text | warmes Anthrazit | `#2E2B28` | Fließtext, Headlines — kein reines Schwarz |
| Text sekundär | Taupe | `#8A8273` | Eyebrow-Labels, Bildunterschriften, Captions |
| Linien | Taupe hell | `#C9C1B4` | 1px-Linien, Trenner, Formularränder |
| Akzent | Terracotta gedämpft | `#A9684B` | CTAs („Anfrage senden"), Hover, sparsame Hervorhebung |

Regeln:

- Genau **ein** Akzent (Terracotta). Olive/Dusty Rose nur, falls das
  Brandkit es vorgibt — nicht beides mischen.
- Kein reines Weiß `#FFFFFF` und kein reines Schwarz `#000000` großflächig.
- Text auf Bildern: Off-White `#F7F4EF`, nie reines Weiß.

## Typografie (Vorschlag, bis Brandkit da ist)

Beide Schriften sind in Wix nativ verfügbar (keine Uploads nötig):

- **Headlines: Cormorant Garamond** (Light/Regular) — die Serif der
  Amour-Referenz; eleganter, weicher als Playfair Display, weniger
  „fashion". Groß einsetzen (Desktop H1 ~60–72px, H2 ~40–48px), Zeilenhöhe
  1.2–1.3, keine Versalien.
- **Eyebrow-Labels: Avenir Light oder Raleway** in Versalien, klein
  (13–14px), Laufweite (letter spacing) +0.15em, Farbe Taupe — das
  „Linien + kleine Schrift"-Editorial-Gefühl von The Light Seeker.
- **Fließtext: Avenir Light oder Raleway Light**, 16–18px, Zeilenhöhe
  1.6–1.8, Farbe Anthrazit, Zeilenbreite max. ~650px (Textboxen nicht
  über die volle Breite ziehen).
- Keine Script-/Handschrift-Fonts. Kursive Cormorant sparsam als
  Stilmittel in Zitaten (Testimonials) erlaubt.

Im Wix-Editor einmalig unter **Site-Design → Text-Themes** hinterlegen
(H1–H6 + Absatz), damit alle Seiten konsistent bleiben und Svenja später
nur Inhalte tauscht.

## Die vier Signatur-Elemente

Diese vier Muster machen den Look aus — alles andere bleibt weg:

### 1. Foto-Fade in den Hintergrund (Svenjas „love it")

So baut man den Amour-Effekt im Wix-Editor nach:

1. Sektion/Strip anlegen, Hintergrund = Foto (Skalierung „ausfüllen").
2. Darüber ein **Rechteck in voller Strip-Breite** legen (Höhe ca. 25–40 %
   des Strips, bündig an der Kante, an der das Bild auslaufen soll —
   meist unten).
3. Rechteck-Füllung: **Linearer Verlauf**, 90° senkrecht, von
   `#F7F4EF` mit 100 % Deckkraft (außen) zu `#F7F4EF` mit 0 % (innen).
4. Kein Rand, kein Schatten. Angrenzende Sektion hat exakt `#F7F4EF` als
   Hintergrund → das Foto „löst sich auf".

Wichtig: Funktioniert nur, wenn die Seitenhintergrundfarbe überall exakt
gleich ist — deshalb Off-White als globale Hintergrundfarbe festlegen.
Sparsam einsetzen: 1–2 Fades pro Seite (z. B. Hero unten, Abschluss vor
dem Footer), sonst verliert der Effekt seine Wirkung.

### 2. Schrift + feine Linie im Bild

- Textbox direkt auf dem Foto (Eyebrow in Versalien + Serif-Headline).
- Daneben/darunter eine **Wix-Linie, 1px, Farbe `#C9C1B4`** (auf dunklen
  Bildern `#F7F4EF` mit ~70 % Deckkraft), z. B. 80–120px kurze Linie
  links neben dem Label oder eine vertikale Linie als ruhige Achse.
- Lesbarkeit ohne schwere Overlays: Textposition in ruhige Bildbereiche
  legen (Himmel, Unschärfe); wenn nötig, sehr dezenter Verlauf
  (Schwarz 0 → 25 %) hinter dem Text statt flächigem Overlay.

### 3. Vollbreite Foto-Trenner

Zwischen Inhaltssektionen volle Bildstreifen (Full-Bleed-Strips,
Desktop-Höhe ~60–75vh) ohne Text oder höchstens mit einer Zeile.
Querformat-Bilder mit ruhiger Komposition wählen. Optional dezenter
Parallax-Effekt (Wix-Strip-Einstellung „Scroll-Effekt: Parallax") —
maximal eine Effektart pro Seite, keine Animations-Spielereien.

### 4. Weißraum als Standard

- Sektionen großzügig polstern (Desktop ≥ 100px oben/unten).
- Pro Sektion: 1 Eyebrow, 1 Headline, max. 1 kurzer Absatz, max. 1 CTA.
- Im Zweifel Element löschen statt verkleinern.

## Seitenstruktur (Launch, aus dem Briefing)

1. Home
2. Hochzeiten
3. Portraits & Paare
4. Portfolio (inkl. eine Reportage zum Durchklicken)
5. Über Svenja
6. Kontakt
7. Impressum / Datenschutz (Footer)

Navigation (Header, ruhig): Hochzeiten · Portraits & Paare · Portfolio ·
Über Svenja · Kontakt + dezenter CTA-Button „Anfrage senden" (Terracotta,
Ghost- oder Textbutton, nicht fett gefüllt). Instagram-Icon nur im Footer.
Bilingual (DE/EN) kommt später über Wix Multilingual — Struktur jetzt
schon so benennen, dass die EN-Spiegelung leichtfällt.

## Homepage — Sektionsplan

1. **Hero**: Full-Bleed-Foto, Claim als Serif-Headline („Nicht nur wie es
   aussah. Sondern wie es sich angefühlt hat."), Eyebrow „Hochzeitsfotografie ·
   Deutschland & Niederlande", feine Linie, unten **Foto-Fade** in Off-White.
2. **Intro/Haltung**: 2–3 Sätze Positionierung (aus dem Briefing), Link
   „Über Svenja".
3. **Foto-Trenner** (Full-Bleed).
4. **Hochzeiten-Teaser**: Eyebrow + Headline + 1 Absatz + CTA zur
   Hochzeiten-Seite. Layout: Text links, hochformatiges Bild rechts (mobil
   gestapelt).
5. **Reportage-Teaser**: „Eine Hochzeit, von Anfang bis Ende" → führt zur
   Klick-Reportage im Portfolio.
6. **Testimonials**: Sand-Hintergrund `#ECE5DA`, 2–3 Zitate als Slider
   (kursive Cormorant, Name in Taupe-Versalien). Inhaltlich: wie sich die
   Zusammenarbeit angefühlt hat, nicht „schöne Bilder".
7. **Q&A kompakt**: 4–6 wichtigste Fragen als Accordion, Link „Alle Fragen"
   (vollständige FAQ auf der Kontakt- oder Hochzeiten-Seite).
8. **Get in touch**: Headline („Erzählt mir von eurem Tag" o. ä.) +
   Anfrage-Formular (Felder siehe unten), davor optional zweiter Foto-Fade.
9. **Footer**: Logo, Kurzclaim, Instagram-Icon, Impressum/Datenschutz.

## Wix-Umsetzungsnotizen (je Feature)

- **Klick-Reportage**: Wix **Pro Gallery**, Layout „Slideshow" (oder
  „Vollbild" beim Klick), Pfeile dezent, Autoplay aus, Bildqualität in den
  Pro-Gallery-Einstellungen hoch. Eine eigene Seite/Sektion „Eine ganze
  Hochzeit" mit kuratierten ~60–100 Bildern in erzählter Reihenfolge
  (Vorbereitung → Zeremonie → Paar → Feier).
- **Testimonials**: Wix-Slideshow mit reinen Textfolien (kein
  Bewertungs-Widget) — passt besser zum ruhigen Look.
- **Q&A**: Wix-Element „Aufklappbarer Text"/Accordion oder die FAQ-App;
  Accordion bevorzugen (volle Designkontrolle, kein App-Branding).
- **Anfrage-Formular**: Wix Forms mit den Briefing-Feldern: Name, E-Mail,
  Sprache (DE/EN), Art der Anfrage (Hochzeit/Paarshooting/Portrait/mobiles
  Studio/Sonstiges), Datum/Zeitraum, Ort/Land, kurze Beschreibung,
  optionaler Budgetrahmen (weich formuliert), „Wie habt ihr Seja
  gefunden?", Datenschutz-Checkbox. Formularfelder im Palette-Stil
  (Linien statt Boxen: nur untere Border in `#C9C1B4`).
- **Socials**: Instagram-Icon (Linienstil, Taupe) im Footer; auf der
  About-Seite optional ein dezenter „Follow my recent work"-Link. Keine
  Feed-Einbettung.
- **Bilder**: Vor dem Einbau kuratieren (Briefing: wenige starke Serien).
  Alt-Texte direkt beim Einpflegen vergeben (SEO). Wix optimiert die
  Auslieferung automatisch; Originale können im Media Manager bleiben.
- **Mobile-Check je Sektion** (Wix-Editor Mobilansicht): Headlines ~32–40px,
  Hochformat-Bilder als Standard, Fade-Rechtecke auf Mobilhöhe prüfen,
  Formular einspaltig, CTA im sichtbaren Bereich.

## No-Gos (Kurzfassung aus dem Briefing)

Keine Bilderrahmen-Collagen, keine Script-Fonts, kein Gold/Luxus-Look,
keine harten S/W-Kontraste, keine grellen Farben, keine unruhigen
Animationen, keine Instagram-Wand, keine überladene Startseite, keine
generischen Hochzeitsfloskeln.

## Nächste Schritte

1. Brandkit (Logo, Typografie) von Svenja abgleichen → Palette/Fonts
   finalisieren.
2. Neues Bildmaterial aus dem Google Drive sichten; Kuratierung:
   Hero-Kandidaten, Foto-Trenner (Querformat, ruhig), Reportage-Strecke.
3. Im Wix-Editor: globale Farben + Text-Themes anlegen (einmalig), dann
   Homepage-Sektionen in obiger Reihenfolge bauen.
4. Texte: Claims/Hero/About aus dem Briefing als Basis, von Svenja
   gegenlesen lassen.
