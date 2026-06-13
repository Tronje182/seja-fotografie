# Schritt-für-Schritt: Seite im Wix-Editor aufsetzen

Stand: 2026-06-13. Praktische Klick-Anleitung für den Aufbau von „Seja
Fotografie" im Wix-Editor. Basis: `design/designrichtung.md` (v2 „Quiet
Editorial"), `briefing/onboarding-briefing.md` und der visuelle Referenz-
Entwurf `design/entwurf-homepage-v1.jpg`.

**Reihenfolge ist Absicht.** Erst die globalen Grundlagen (Phase 0–1) — sie
sparen später an jeder Seite Zeit, weil Farben, Schriften und Header/Footer
einmal definiert werden und überall greifen. Dann die Homepage (Phase 2) als
Blaupause, dann die Unterseiten (Phase 3), dann Conversion/Recht/SEO
(Phase 4–6) und zuletzt der Mobile-Durchgang + Launch (Phase 7–8).

**Kopiervorlage Farben** (in jedem Farbwähler unter „Hinzufügen" → Hex
eingeben):

| Rolle | Hex |
|---|---|
| Hintergrund Off-White | `#F4F1EE` |
| Fläche 2 (helles Greige) | `#E9E2DD` |
| Text Fast-Schwarz | `#181719` |
| Fließtext weicher | `#2E2B2B` |
| Text sekundär / Labels (Dusty Rose) | `#A38177` |
| Linien (Greige) | `#B09993` |
| Akzent / CTA (Rostrot) | `#732E1F` |
| Dunkle Sektion | `#181719` |
| Text auf Dunkel / auf Bildern | `#F2F2F2` |

---

## Phase 0 — Vorbereitung (vor dem Editor)

1. **Bei Wix einloggen** und die Site „Seja Fotografie" öffnen
   (`https://sdobbelstein.wixsite.com/seja-fotografie`,
   Site-ID `1f8308b9-7e8c-471f-ac37-488ac3ca2fa9`).
2. **Editor-Variante prüfen**: Diese Anleitung geht vom klassischen
   **Wix-Editor** aus (nicht „Editor X"/Studio). Falls die Site in Wix Studio
   liegt, heißen die Menüs teils anders, die Schritte bleiben sinngemäß gleich.
3. **Medien bereit**: Die kuratierten Bilder liegen im Media Manager bereits
   sortiert:
   - Ordner **„Website-Auswahl"** — die 18 kuratierten Website-Fotos
     (Hero, Foto-Trenner, Teaser).
   - Ordner **„Website-Portraits Svenja"** — 14 Studio-Portraits (für
     About-Teaser und Über-Svenja-Seite).
   - Ordner **„My Logos"** — `SEJA-Fotografie-Logo-schwarz.png` (Header auf
     Hell) und `SEJA-Fotografie-Logo-weiss.png` (auf dunklen Flächen/Footer).
4. **Reportage-Material**: Steht für die Klick-Reportage im Portfolio teils
   noch aus — diese eine Sektion später nachziehen, sie ist nicht
   launch-blockierend.

---

## Phase 1 — Globale Grundlagen einrichten

Diese Phase einmal sauber machen, dann nie wieder anfassen.

### 1.1 Farbpalette hinterlegen

1. Linke Leiste → **Site-Design** (Pinsel-Symbol) → **Farbe** /
   **Farbpalette**.
2. Auf **„Palette bearbeiten"** und die neun Farben aus der Tabelle oben als
   Site-Farben anlegen. Tipp: Off-White `#F4F1EE` auf den **ersten
   Hauptplatz** legen — das ist die globale Hintergrundfarbe und Voraussetzung
   für den Foto-Fade-Effekt.

### 1.2 Globalen Seitenhintergrund auf Off-White

1. **Site-Design → Hintergrund** (oder pro Seite über „Seitenhintergrund").
2. Hintergrundfarbe auf exakt `#F4F1EE` setzen — **überall identisch**. Der
   Foto-Fade (Element 1) funktioniert nur, wenn jeder angrenzende Hintergrund
   exakt dieselbe Farbe hat.

### 1.3 Schriften / Text-Themes

Brand-Heading-Font ist „Adore", aber bis die Webfont-Lizenz geklärt ist gilt
**Prata als Heading-Font** (Entscheidung Hagen). Fließtext: Raleway oder
Avenir Light.

1. **Site-Design → Text** → **Text-Themes** bearbeiten.
2. Folgende Themes definieren (Werte als Startwert, am Entwurf feinjustieren):
   - **H1**: Prata, ~48–64px Desktop, Farbe `#181719`.
   - **H2**: Prata, ~32–40px, `#181719`.
   - **H3**: Prata, ~24–28px.
   - **Absatz / Fließtext**: Raleway (oder Avenir Light), 16–18px,
     Zeilenhöhe 1.6–1.8, Farbe `#2E2B2B`, max. ~650px Zeilenbreite.
   - **Eyebrow-Label** (eigenes Absatz-Theme): Raleway in VERSALIEN, 13–14px,
     Laufweite +0.15em, Farbe Dusty Rose `#A38177`.
3. **Eigene Fonts** (für später, wenn Adore lizenziert ist): Site-Design →
   Text → **Schriften hochladen** (TTF/OTF/WOFF). Lizenz-Check zuerst:
   Desktop-Lizenz reicht **nicht** für Webfont-Einbettung — Web-/Webfont-
   Lizenz nötig.

### 1.4 Header (Navigation)

1. Header-Bereich anklicken → ggf. auf ein ruhiges, transparentes oder
   Off-White-Design stellen.
2. **Logo** einfügen: `SEJA-Fotografie-Logo-schwarz.png` aus „My Logos",
   dezent skaliert, links oder mittig.
3. **Menü** (Hauptnavigation): Hochzeiten · Portraits & Paare · Portfolio ·
   Über Svenja · Kontakt. Schrift Raleway, ruhig, Farbe `#181719`,
   Hover `#732E1F`.
4. **CTA-Button** „Anfrage senden": **Ghost-/Textbutton**, Schrift Rostrot
   `#732E1F`, **nicht** flächig gefüllt. Verlinkt zur Kontaktseite/zum
   Formular-Anker.
5. Header **auf allen Seiten anzeigen** (Standard in Wix). Instagram **nicht**
   in den Header — kommt nur in den Footer.

### 1.5 Footer

1. Footer-Bereich → Hintergrund dunkel (`#181719`) oder Off-White, je nach
   Gesamtbild (Entwurf prüfen).
2. Inhalt: **Logo** (auf Dunkel die weiße Variante
   `SEJA-Fotografie-Logo-weiss.png`), Kurzclaim, **Instagram-Icon** im
   Linienstil (Taupe), Links **Impressum** und **Datenschutz**.
3. Keine Instagram-Feed-Einbettung.

---

## Phase 2 — Homepage bauen

Sektionen exakt in dieser Reihenfolge (entspricht dem Sektionsplan). Jede
Sektion großzügig polstern (Desktop ≥ 100px oben/unten). Faustregel pro
Sektion: 1 Eyebrow, 1 Headline, max. 1 kurzer Absatz, max. 1 CTA.

> **Sektion hinzufügen**: linke Leiste → **Hinzufügen (+)** → **Sektion/Strip**
> bzw. **Streifen**. Im klassischen Editor sind das „Strips" mit
> Hintergrund-Option.

### 2.1 Hero (Full-Bleed mit Reveal-Effekt)

1. Strip anlegen, **Hintergrund = Foto** aus „Website-Auswahl" (querformatig,
   ruhige Komposition), Skalierung **„ausfüllen"**, Höhe ~90–100vh.
2. **Scroll-Effekt „Reveal"**: Strip-Hintergrund → **Hintergrund ändern →
   Einstellungen → Scroll-Effekte → „Reveal" (Aufdecken)**. Das Bild bleibt
   fixiert, der nächste Content schiebt sich darüber.
3. **Textbox** auf dem Bild:
   - Eyebrow: „Hochzeitsfotografie · Deutschland & Niederlande"
     (Eyebrow-Theme, auf dunklem Bild Farbe `#F2F2F2`).
   - Headline (H1): „Nicht nur wie es aussah. Sondern wie es sich angefühlt
     hat." — Text in `#F2F2F2`.
   - **Feine Linie** daneben/darunter: Wix-Linie, 1px, auf dunklem Bild
     `#F4F1EE`/`#F2F2F2` mit ~70 % Deckkraft; auf hellem Bild `#B09993`.
   - Lesbarkeit: Text in ruhigen Bildbereich legen; wenn nötig sehr dezenter
     Verlauf (Schwarz 0 → 25 %) hinter dem Text, **kein** flächiges Overlay.
4. **Foto-Fade unten** (Signatur-Element 1):
   - Über den unteren ~25–40 % des Strips ein **Rechteck in voller Breite**,
     bündig an der Unterkante.
   - Füllung: **Linearer Verlauf, 90° senkrecht**, von `#F4F1EE` 100 %
     (außen/unten) zu `#F4F1EE` 0 % (innen/oben). Kein Rand, kein Schatten.
   - Nächste Sektion hat exakt `#F4F1EE` → das Bild „löst sich auf".

### 2.2 Intro / Haltung

- Off-White-Hintergrund. 2–3 Sätze Positionierung (Briefing-Hero-Richtung als
  Basis), zentriert oder linksbündig. Dezenter Textlink „Über Svenja".

### 2.3 Foto-Trenner (Full-Bleed)

- Vollbreiter Bildstreifen aus „Website-Auswahl", Höhe ~60–75vh, **ohne Text**
  oder höchstens eine Zeile. Querformat, ruhige Komposition. Optional
  derselbe „Reveal"-Effekt — aber pro Seite nur **eine** Effekt-Variante
  (Reveal **oder** Parallax), nicht mischen.

### 2.4 Hochzeiten-Teaser

- Zweispaltig: **Text links** (Eyebrow + H2 + 1 Absatz + CTA „Zu den
  Hochzeiten"), **Hochformat-Bild rechts**. Mobil gestapelt (Text über Bild).
- CTA-Button im Palette-Stil (Rostrot-Text, dezent).

### 2.5 Reportage-Teaser

- Eyebrow + Headline „Eine Hochzeit, von Anfang bis Ende" + 1 Absatz + CTA, der
  zur Klick-Reportage im Portfolio führt. (Inhalt nachziehen, sobald
  Reportage-Material da ist.)

### 2.6 About-Teaser (die EINE dunkle Sektion)

- Strip-Hintergrund `#181719`. Portrait von Svenja aus „Website-Portraits
  Svenja" (sie trägt meist Schwarz → harmoniert mit der dunklen Fläche).
- Text in `#F2F2F2`: kurze Vorstellung (2–3 Sätze aus dem About-Text) + Link
  „Über Svenja". Optional Signatur „Svenja" als einzelnes handschriftliches
  Wort (Script „The Impressionist" — nur hier, sparsam).

### 2.7 Testimonials (bauen, aber AUSBLENDEN)

- Hintergrund helles Greige `#E9E2DD`. **Wix-Slideshow mit reinen Textfolien**
  (kein Bewertungs-Widget): 2–3 Zitate, kursive Serif, Name in
  Dusty-Rose-Versalien.
- **Wichtig**: Es gibt noch keine Testimonials. Sektion bauen, dann
  **ausblenden** (Sektion/Element rechtsklick → „Ausblenden" bzw.
  Sichtbarkeit aus). Svenja blendet sie später nur ein und füllt Texte ein —
  keine Layoutarbeit mehr. **Launch ohne diese Sektion.**

### 2.8 Q&A kompakt

- **Aufklappbarer Text / Accordion** (bevorzugt vor der FAQ-App — volle
  Designkontrolle, kein App-Branding). 4–6 wichtigste Fragen aus dem Briefing.
- Link „Alle Fragen" → vollständige FAQ auf Kontakt- oder Hochzeiten-Seite.

### 2.9 Get in touch

- Headline („Erzählt mir von eurem Tag" o. ä.) + **Anfrage-Formular** (Felder
  siehe Phase 4). Davor optional zweiter Foto-Fade.

> Der Footer (Phase 1.5) schließt jede Seite automatisch ab.

---

## Phase 3 — Unterseiten anlegen

**Seiten verwalten**: Menü/Seiten-Panel → **Seite hinzufügen**. Für jede Seite
eine saubere URL vergeben (SEO). Header/Footer erscheinen automatisch.

Struktur (Launch):

1. **Hochzeiten** — Hauptfokus. Hero-Bild + Haltung + Leistungsumfang
   (Ganztagsbegleitung) + Ablauf (Anfrage → Antwort → Call → Angebot →
   Vorbereitung → Tag → Bildübergabe) + Preisrahmen weich
   („Hochzeitsreportagen starten ab X €.") + FAQ + CTA zum Formular.
2. **Portraits & Paare** — ergänzend, klar nachgeordnet. Bildstrecke +
   kurze Texte + ggf. transparentere Startpreise + CTA.
3. **Portfolio** — stark kuratiert. Bildgalerie + **Klick-Reportage** „Eine
   ganze Hochzeit": **Wix Pro Gallery**, Layout **„Slideshow"** (oder Vollbild
   beim Klick), Pfeile dezent, **Autoplay aus**, Bildqualität hoch, ~60–100
   Bilder in erzählter Reihenfolge (Vorbereitung → Zeremonie → Paar → Feier).
   (Reportage nachziehen, sobald Material da.)
4. **Über Svenja** — kein Nebenschauplatz. Persönlicher Text (About-Richtung
   aus dem Briefing), Portraits aus „Website-Portraits Svenja". Hier darf eine
   dunkle Hero-/Intro-Sektion stehen (die dunkle Sektion dieser Seite).
   Optional dezenter „Follow my recent work"-Instagram-Link.
5. **Kontakt** — Anfrage-Formular prominent + ggf. vollständige FAQ.
6. **Impressum** und **Datenschutz** — eigene Seiten, nur im Footer verlinkt
   (nicht im Hauptmenü).

Pro Seite gilt: hell ist Normalzustand, **maximal eine** dunkle Sektion,
Rostrot nur als Akzent, viel Weißraum.

---

## Phase 4 — Anfrage-Formular (Wix Forms)

1. **Hinzufügen → Kontakt → Wix Forms** auf Kontakt- und Homepage-Sektion
   (dasselbe Formular wiederverwenden).
2. **Felder** (aus dem Briefing):
   - Name
   - E-Mail
   - Sprache (DE/EN)
   - Art der Anfrage (Hochzeit / Paarshooting / Portrait / mobiles Studio /
     Sonstiges)
   - Datum / Zeitraum
   - Ort / Land
   - kurze Beschreibung
   - optionaler Budgetrahmen (weich formuliert, siehe Briefing-Text)
   - „Wie habt ihr Seja gefunden?"
   - **Datenschutz-Checkbox** (Pflicht)
3. **Stil**: Felder im Palette-Look — **Linien statt Boxen**: nur untere
   Border in `#B09993`, Hintergrund transparent/Off-White. Senden-Button
   Rostrot `#732E1F`.
4. **Benachrichtigung** einrichten (an Svenjas E-Mail) und **Testversand**
   prüfen, bevor die Seite live geht.

---

## Phase 5 — Recht & DSGVO

1. **Impressum** und **Datenschutz** als Seiten füllen (Texte abstimmen;
   Wix-Standardvorlagen anpassen, nicht blind übernehmen).
2. **Cookie-Banner / Consent**: Einstellungen → Datenschutz / Cookie-Banner
   aktivieren und auf DE/EU einstellen.
3. **Google Fonts möglichst datenschutzfreundlich**; unnötige Drittanbieter-
   Skripte vermeiden.
4. Formular ist datenschutzfreundlich konfiguriert (Checkbox + sparsame
   Felder).

---

## Phase 6 — SEO-Basics

Pro Seite (Seiten-Panel → **SEO-Grundlagen** / SEO-Tab):

1. **Seitentitel** (Meta Title) — z. B. „Hochzeitsfotografin Deutschland &
   Niederlande | Seja Fotografie".
2. **Meta Description** — emotional + Keyword, ~150 Zeichen.
3. **Saubere URL-Slugs** (z. B. `/hochzeiten`, `/ueber-svenja`).
4. **Alt-Texte** für **alle** Bilder direkt beim Einpflegen vergeben.
5. **Überschriften-Hierarchie** sauber (eine H1 pro Seite, dann H2/H3).
6. Struktur so anlegen, dass spätere regionale Landingpages
   (NRW/Düsseldorf/Köln …) und die EN-Version (Wix Multilingual) leicht
   ergänzbar sind.

---

## Phase 7 — Mobile-Durchgang

Im Editor oben auf das **Mobil-Symbol** umschalten und **jede** Seite/Sektion
prüfen (Wix verwaltet die Mobilansicht separat):

- Headlines ~32–40px, gut lesbar.
- Hochformat-Bilder als Standard, **kein Layout-Chaos**.
- Fade-Rechtecke auf Mobilhöhe nachjustieren.
- Scroll-Effekte: Wix deaktiviert sie mobil teils automatisch — okay, mobil
  zählt das stehende Bild.
- Formular **einspaltig**, CTA im sichtbaren Bereich.
- Überflüssige Elemente mobil ausblenden statt quetschen.

---

## Phase 8 — Veröffentlichen

1. **Vorschau** über alle Seiten (Desktop + Mobil), Links und Formular testen.
2. **Texte von Svenja gegenlesen** lassen.
3. Sicherstellen: Testimonials-Sektion ist **ausgeblendet**, Reportage-Sektion
   ist vorhanden oder sauber leer/ausgeblendet bis Material kommt.
4. **Veröffentlichen** — zunächst unter der `wixsite.com`-URL. Eigene Domain
   (`sejafotografie.de` o. ä.) + Weiterleitung von
   `seja-fotografie-coaching.de` folgt später.

---

## Nach dem Launch (nicht blockierend)

- **Testimonials** einblenden, sobald 2–3 Zitate da sind.
- **Adore-Webfont** hochladen, sobald Lizenz/Dateien da sind (ersetzt Prata).
- **Englische Version** via **Wix Multilingual** (Struktur ist vorbereitet).
- **Eigene Domain** + Weiterleitung einrichten.
- **Regionale SEO-Landingpages** ergänzen.
- **Klick-Reportage** vervollständigen / zweite Reportage.

---

## Schnell-Checkliste (zum Abhaken)

- [ ] Farbpalette (9 Farben) hinterlegt
- [ ] Globaler Hintergrund exakt `#F4F1EE`
- [ ] Text-Themes (Prata-Headings + Raleway-Fließtext + Eyebrow) gesetzt
- [ ] Header mit Logo, Menü, Ghost-CTA „Anfrage senden"
- [ ] Footer mit weißem Logo, Instagram, Impressum/Datenschutz
- [ ] Homepage-Sektionen 2.1–2.9 gebaut (Testimonials ausgeblendet)
- [ ] Foto-Fade + Reveal-Effekt funktionieren (Hintergründe identisch)
- [ ] Unterseiten Hochzeiten / Portraits & Paare / Portfolio / Über Svenja /
      Kontakt
- [ ] Impressum + Datenschutz angelegt
- [ ] Anfrage-Formular gebaut + Testversand geprüft
- [ ] SEO (Titel, Descriptions, Slugs, Alt-Texte) pro Seite
- [ ] Mobile-Durchgang aller Seiten
- [ ] Veröffentlicht
