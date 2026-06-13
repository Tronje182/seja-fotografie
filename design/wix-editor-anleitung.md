# Schritt-für-Schritt: Seite im Wix Harmony Editor aufsetzen

Stand: 2026-06-13. Praktische Klick-Anleitung für den Aufbau von „Seja
Fotografie" im **Wix Harmony Editor** (der Editor, in dem Svenja arbeitet —
nicht der klassische Wix-Editor und nicht Wix Studio). Basis:
`design/designrichtung.md` (v2 „Quiet Editorial"),
`briefing/onboarding-briefing.md` und der visuelle Referenz-Entwurf
`design/entwurf-homepage-v1.jpg`.

> **Harmony-Begriffe in Kürze** (weicht vom klassischen Editor ab):
> - **Brand-Panel** (oben in der Leiste) → hier liegen **Farben** und
>   **Text/Schriften** zentral. (Im klassischen Editor hieß das „Site-Design".)
> - **Sektionen** sind die Bausteine der Seite (im klassischen Editor „Strips").
>   Hinzufügen über **+ Add** (oben links) → **Sektionen**.
> - **Elemente hinzufügen** über das **+ Add**-Panel links (Text, Linien,
>   Galerien, Formulare, Buttons …).
> - **Hintergrund einer Sektion** ändern: Sektion wählen →
>   **Hintergrund ersetzen** (Replace Background) → Farbe / Bild / Video.
> - **Scroll-Effekte**: Sektion wählen → **Animation-Icon** → z. B.
>   **Freeze (Einfrieren)**, **Parallax**, **Zoom**, **Fade**.
> - **Seiten** verwalten über das **Site-Seiten-Panel** oben.
> - **Aria (Ask AI)** unten rechts kann beim Layout helfen.

**Reihenfolge ist Absicht.** Erst die globalen Grundlagen (Phase 0–1) — sie
sparen später an jeder Seite Zeit, weil Farben, Schriften und Header/Footer
einmal definiert werden und überall greifen. Dann die Homepage (Phase 2) als
Blaupause, dann die Unterseiten (Phase 3), dann Conversion/Recht/SEO
(Phase 4–6) und zuletzt der Mobile-Durchgang + Launch (Phase 7–8).

**Kopiervorlage Farben** (im Brand-Panel → Farben → unter „Gespeicherte
Farben" auf **Hinzufügen** und Hex eingeben):

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

## Phase 0 — Vorbereitung

1. Site „Seja Fotografie" im **Harmony Editor** öffnen
   (Site-ID `1f8308b9-7e8c-471f-ac37-488ac3ca2fa9`).
2. **Template-Reste aufräumen**: Die Site basiert noch auf einem Wix-Template
   (Platzhalter-Claim, Demo-Navigation „Portfolioseite", „Jetzt buchen", evtl.
   ein Profilfoto im Header). Diese Default-Inhalte werden in den folgenden
   Phasen durch die abgestimmten Inhalte ersetzt — siehe den Abschnitt
   **„Abgleich mit dem aktuellen Stand"** am Ende.
3. **Medien bereit** (Media Manager, bereits sortiert):
   - **„Website-Auswahl"** — 18 kuratierte Website-Fotos (Hero, Foto-Trenner,
     Teaser).
   - **„Website-Portraits Svenja"** — 14 Studio-Portraits (About-Teaser,
     Über-Svenja-Seite).
   - **„My Logos"** — `SEJA-Fotografie-Logo-schwarz.png` (Header auf Hell),
     `SEJA-Fotografie-Logo-weiss.png` (auf dunklen Flächen/Footer).
4. **Reportage-Material** für die Klick-Reportage im Portfolio steht teils noch
   aus → diese Sektion später nachziehen (nicht launch-blockierend).

---

## Phase 1 — Globale Grundlagen (Brand-Panel)

Einmal sauber machen, dann nie wieder anfassen.

### 1.1 Farbpalette hinterlegen

Oben in der Leiste auf **Brand** → **Farben**. Das Harmony-Panel ist in
**Grundfarbe**, **Schattierungen** (per Schloss aus der Grundfarbe abgeleitet),
**Akzent** und **Gespeicherte Farben** gegliedert. Die Template-Palette ist
schon warm/erdig — am einfachsten **die vorhandenen Felder anklicken und auf
unsere exakten Hex-Werte setzen** (nicht zwingend „Palette ändern"). Zuordnung:

- **Grundfarbe** (die zwei Arbeitstiere, seitenweit):
  - Hell → `#F4F1EE` (Off-White, Haupthintergrund)
  - Dunkel → `#181719` (Fast-Schwarz, Text & dunkle Sektion)
- **Schattierungen** (Schloss-Icon anklicken → manuell setzen):
  - `#E9E2DD` (helles Greige) · `#B09993` (Greige, Linien) · `#755A51` (Taupe,
    Reserve)
- **Akzent**:
  - `#732E1F` (Rostrot, CTA) · `#A38177` (Dusty Rose, Labels) · `#E9E2DD` ·
    `#181719`
- **Gespeicherte Farben** (per „+" hinzufügen — die reinen Textfarben):
  - `#2E2B2B` (weicher Fließtext) · `#F2F2F2` (Text auf Dunkel/Bildern)

Wichtig: Off-White + Fast-Schwarz gehören in die **Grundfarbe** (Harmony wendet
sie seitenweit an), **Rostrot muss ein Akzent** sein (Buttons/Links greifen
darauf zu). Off-White `#F4F1EE` ist zugleich Voraussetzung für den Foto-Fade
(siehe 2.1).

### 1.2 Heller Grundlook für alle Sektionen

Im Harmony Editor hat **jede Sektion ihren eigenen Hintergrund** (es gibt kein
einzelnes „Seitenhintergrund"-Feld wie früher). Deshalb:

1. Beim Bauen jede Text-/Inhaltssektion ohne Foto auf **Hintergrund ersetzen →
   Farbe → `#F4F1EE`** setzen.
2. **Exakt dieselbe** Off-White-Farbe verwenden, wo ein Foto in den
   Hintergrund auslaufen soll (Foto-Fade) — sonst entsteht eine sichtbare
   Kante.

### 1.3 Schriften / Text-Styles

Brand-Heading-Font ist „Adore". Prata war als Wix-Fallback geplant, ist im
**Harmony Editor aber nicht in der Schriftliste** (Stand 2026-06-13). Deshalb
gilt als Heading-Font **Playfair Display** (Entscheidung 2026-06-13) — eine
verfügbare Display-Serif mit hohem Strichkontrast, am nächsten an der
Adore-Anmutung. **Fließtext: Avenir Light** (so im Editor gesetzt, 2026-06-13 —
die erste Wahl aus der Designrichtung).

> Das Template stellt aktuell **„Braggadocio"** als Heading ein — eine schwere
> Art-Déco-Schrift, die **nicht** zum ruhigen Editorial-Look passt. Auf
> Playfair Display umstellen.

1. Oben auf **Brand** → **Text**. Schriftartenset: **Playfair Display /
   Avenir Light**.
2. **Font für Überschriften** = Playfair Display (im Schrift-Menü oben ins
   **Suchfeld** „Playfair" tippen), **Font für Absätze** = Avenir Light.
3. Finale Typo-Skala (im Editor gesetzt), **Textfarbe** pro Stil bzw. pro
   Element (siehe unten), nicht zentral als ein Feld:
   - **Überschrift 1 (H1)**: Playfair Display, 64px, Farbe `#181719`.
   - **Überschrift 2 (H2)**: Playfair Display, 40px, `#181719`.
   - **Überschrift 3 (H3)**: Playfair Display, 28px (H4 ggf. auf ~24px für eine
     feinere Abstufung).
   - **Überschrift 5/6**: 22px / 18px.
   - **Textabschnitt 1/2**: Avenir Light, 18px / 16px, Farbe `#2E2B2B`,
     **Zeilenhöhe 1.6–1.8**, Zeilenbreite im Layout max. ~650px.
   - **Textabschnitt 3 (14px)**: als **Eyebrow-Label** nutzen — GROSSBUCHSTABEN,
     Laufweite ~+0.15em, Farbe Dusty Rose `#A38177`.
4. **Feinschliff**:
   - Große Playfair-Headlines (64px) mit **engerer Zeilenhöhe ~1.05–1.15** und
     einem Hauch negativer Laufweite, damit mehrzeilige Headlines nicht
     ausfransen.
   - **Avenir Light** ist eine dünne Schnittstärke: im **Mobil-View** auf
     Lesbarkeit prüfen; wirkt der Haupt-Fließtext zu fein/blass, auf
     **Avenir (Book/Regular)** gehen und Light nur für große/ruhige Stellen.
5. **Textfarbe setzen** (es gibt kein globales „Textfarbe"-Feld im Branding):
   - **Global pro Stil**: Brand → Text → Stil (z. B. Absatz/Überschrift)
     bearbeiten → dort in der Formatierung die **Farbe** aus der Palette wählen.
   - **Pro Element**: Text markieren → Action-Bar → **„Alle Textoptionen"** →
     **Textfarbe** aus der Palette (z. B. `#F2F2F2` auf dunklen Sektionen).
6. **Eigene Fonts (Adore)**: Ob Harmony Webfont-Upload schon unterstützt, ist
   offen (in der Brand-Doku nicht bestätigt). **Bis das geklärt und die Lizenz
   vorhanden ist, bleibt Playfair Display.** Lizenz-Hinweis: Desktop-Lizenz
   deckt **keine** Webfont-Einbettung; dafür braucht es eine Web-/Webfont-Lizenz.

### 1.4 Header (Navigation)

1. Header-Bereich anklicken (Harmony hat einen eigenen Header-Customizer).
2. **Logo**: `SEJA-Fotografie-Logo-schwarz.png` aus „My Logos" einsetzen.
   **Achtung Variante**: die abgestimmte Subline ist **„SEJA Fotografie"** —
   nicht „Media & Fotografie" (siehe Abgleich am Ende).
3. **Menü** auf die abgestimmte Navigation umstellen: **Hochzeiten ·
   Portraits & Paare · Portfolio · Über Svenja · Kontakt**. Schrift Avenir
   Light, `#181719`, Hover `#732E1F`.
4. **CTA-Button**: **Ghost-/Textbutton** in Rostrot `#732E1F` (nicht flächig
   gefüllt). Text **„Anfrage senden"** — *nicht* „Jetzt buchen" (zum Start kein
   direkter Kalender/Buchung; siehe Briefing). Verlinkt zur Kontaktseite/zum
   Formular-Anker.
5. Instagram **nicht** in den Header; ein evtl. vorhandenes Profil-/Member-Foto
   im Header entfernen, falls es nicht gewollt ist.

### 1.5 Footer

1. Footer-Hintergrund dunkel (`#181719`) oder Off-White (am Gesamtbild
   entscheiden).
2. Inhalt: **Logo** (auf Dunkel die weiße Variante), Kurzclaim,
   **Instagram-Icon** im Linienstil (Taupe), Links **Impressum** und
   **Datenschutz**.
3. Keine Instagram-Feed-Einbettung.

---

## Phase 2 — Homepage bauen

> **Sektion hinzufügen**: **+ Add** (oben links) → **Sektionen** → wählen
> zwischen **Leere Sektion**, **Designte Sektion** (vorgefertigte Layouts) oder
> **Mit KI generieren**. Alternativ am oberen/unteren Rand einer Sektion auf
> **+ Sektion hinzufügen**. **Reihenfolge** ändern: Sektion wählen → Pfeil-Icons
> links (rauf/runter).
>
> Für den ruhigen Editorial-Look meist **leere Sektion** + eigene Elemente —
> oder eine schlichte designte Sektion als Startgerüst und dann ausdünnen.

Jede Sektion großzügig polstern (Desktop ≥ 100px oben/unten). Faustregel pro
Sektion: 1 Eyebrow, 1 Headline, max. 1 kurzer Absatz, max. 1 CTA.

### 2.1 Hero (Full-Bleed mit Freeze-Effekt)

1. Sektion → **Hintergrund ersetzen → Bild** → Foto aus „Website-Auswahl"
   (querformatig, ruhige Komposition). Fokuspunkt setzen, Skalierung füllend,
   Höhe ~90–100vh.
2. **Scroll-Effekt**: Sektion wählen → **Animation-Icon** → **„Freeze"
   (Einfrieren)**. Das ist der Light-Seeker-Effekt: das Bild bleibt fixiert,
   der nächste Content schiebt sich darüber. (Alternative: **Parallax** —
   etwas mehr Bewegung. Pro Seite nur **eine** Variante, nicht mischen.)
   Hinweis: Scroll-Effekte sind **nur in der Vorschau / live** korrekt sichtbar,
   nicht im Editor.
3. **Textbox** auf dem Bild (über **+ Add → Text**):
   - Eyebrow: „Hochzeitsfotografie · Deutschland & Niederlande" (Farbe `#F2F2F2`
     auf dunklem Bild).
   - Headline (H1): **„Nicht nur wie es aussah. Sondern wie es sich angefühlt
     hat."** — Farbe `#F2F2F2`. (Den generischen Template-Claim „Ewige
     Erinnerungen in jedem Bild" ersetzen.)
   - **Feine Linie** (+ Add → Element/Linie), 1px: auf dunklem Bild `#F2F2F2`
     ~70 % Deckkraft, auf hellem `#B09993`.
   - Lesbarkeit: Text in ruhigen Bildbereich legen; bei Bedarf hinter dem Text
     eine sehr dezente halbtransparente Box, **kein** flächiges Overlay.
4. **Foto-Fade unten** (Signatur-Element 1) — Harmony-spezifisch:
   Der Sektion-Hintergrund selbst kennt **keinen Verlauf**. Daher als
   **Overlay-Element** über eine fertige Verlaufs-PNG lösen:
   - **Asset**: `design/assets/foto-fade-offwhite.png` (transparent oben →
     `#F4F1EE` deckend unten, 1920×1000, weiche Smoothstep-Blende). Für dunkle
     Sektionen: `design/assets/foto-fade-dunkel.png` (→ `#181719`). Neu
     erzeugen / Farbe ändern: `python3 design/foto-fade.py`.
   - **Einbauen**: PNG in den Media Manager hochladen → in der Hero-Sektion über
     **+ Add → Bild** einfügen → **auf volle Breite** ziehen und **bündig an die
     Unterkante** legen (Höhe nach Geschmack, ~25–40 % der Sektion). Die nächste
     Sektion hat exakt `#F4F1EE` → das Foto „löst sich auf".
   - Wichtig: Die Folgesektion muss **exakt** dieselbe Farbe haben wie das
     deckende PNG-Ende, sonst entsteht eine Kante.
   - Sparsam: 1–2 Fades pro Seite. (Falls Harmony für Box-/Form-Elemente eine
     Verlaufsfüllung bietet, geht es alternativ auch damit — die PNG ist aber
     der editor-sichere Weg und mobil unkritisch.)

### 2.2 Intro / Haltung

- Hintergrund `#F4F1EE`. 2–3 Sätze Positionierung (Briefing-Hero-Richtung als
  Basis, **Svenjas „ich"-Stimme**, nicht „wir"). Dezenter Textlink „Über Svenja".

### 2.3 Foto-Trenner (Full-Bleed)

- Sektion mit Bild-Hintergrund aus „Website-Auswahl", Höhe ~60–75vh, **ohne
  Text** oder max. eine Zeile. Querformat, ruhige Komposition. Optional derselbe
  Freeze-Effekt (aber nur **eine** Effekt-Variante pro Seite).

### 2.4 Hochzeiten-Teaser

- Zweispaltig: **Text links** (Eyebrow + H2 + 1 Absatz + CTA „Zu den
  Hochzeiten"), **Hochformat-Bild rechts**. Harmony stapelt das mobil
  automatisch; im Mobil-View prüfen (Text über Bild).

### 2.5 Reportage-Teaser

- Eyebrow + Headline „Eine Hochzeit, von Anfang bis Ende" + 1 Absatz + CTA zur
  Klick-Reportage im Portfolio. (Inhalt nachziehen, sobald Material da ist.)

### 2.6 About-Teaser (die EINE dunkle Sektion)

- **Hintergrund ersetzen → Farbe → `#181719`**. Portrait aus „Website-Portraits
  Svenja" (Svenja trägt meist Schwarz → harmoniert mit der dunklen Fläche).
- Text in `#F2F2F2`: 2–3 Sätze aus dem About-Text + Link „Über Svenja".
  Optional Signatur „Svenja" als einzelnes handschriftliches Wort (Script „The
  Impressionist", nur hier, sparsam).

### 2.7 Testimonials (bauen, aber AUSBLENDEN)

- Hintergrund helles Greige `#E9E2DD`. Slideshow/Slider mit **reinen
  Textfolien** (kein Bewertungs-Widget): 2–3 Zitate, kursive Serif, Name in
  Dusty-Rose-Versalien.
- **Es gibt noch keine Testimonials** → Sektion bauen, dann **ausblenden**
  (Sektion wählen → Rechtsklick/Aktionsmenü → **Ausblenden**). So füllt Svenja
  später nur Texte und blendet ein. **Launch ohne diese Sektion.**

### 2.8 Q&A kompakt

- **Aufklappbarer Text / Accordion** (über + Add suchen) — bevorzugt vor der
  FAQ-App (volle Designkontrolle, kein App-Branding). 4–6 wichtigste Fragen aus
  dem Briefing. Link „Alle Fragen" → vollständige FAQ auf Kontakt-/Hochzeiten-
  Seite.

### 2.9 Get in touch

- Headline („Erzählt mir von eurem Tag" o. ä.) + **Anfrage-Formular** (Felder
  in Phase 4). Davor optional zweiter Foto-Fade.

> Der Footer (Phase 1.5) schließt jede Seite automatisch ab.

---

## Phase 3 — Unterseiten anlegen

**Seiten verwalten**: oben **Site-Seiten-Panel** → **Seite hinzufügen**. Saubere
URL je Seite (SEO). Header/Footer erscheinen automatisch. Die Template-Seite
„Portfolioseite" zur echten Portfolio-Seite umbauen/umbenennen.

Struktur (Launch):

1. **Hochzeiten** — Hauptfokus. Hero-Bild + Haltung + Leistungsumfang
   (Ganztagsbegleitung) + Ablauf (Anfrage → Antwort → Call → Angebot →
   Vorbereitung → Tag → Bildübergabe) + Preisrahmen weich
   („Hochzeitsreportagen starten ab X €.") + FAQ + CTA zum Formular.
2. **Portraits & Paare** — ergänzend, klar nachgeordnet. Bildstrecke + kurze
   Texte + ggf. transparentere Startpreise + CTA.
3. **Portfolio** — stark kuratiert. Galerie + **Klick-Reportage** „Eine ganze
   Hochzeit": **Wix Pro Gallery**, Layout **Slideshow** (oder Vollbild beim
   Klick), Pfeile dezent, **Autoplay aus**, Bildqualität hoch, ~60–100 Bilder in
   erzählter Reihenfolge (Vorbereitung → Zeremonie → Paar → Feier). (Nachziehen,
   sobald Material da.)
4. **Über Svenja** — kein Nebenschauplatz. Persönlicher Text (About-Richtung),
   Portraits aus „Website-Portraits Svenja". Hier darf eine dunkle Hero-/Intro-
   Sektion stehen. Optional dezenter „Follow my recent work"-Instagram-Link.
5. **Kontakt** — Anfrage-Formular prominent + ggf. vollständige FAQ.
6. **Impressum** und **Datenschutz** — eigene Seiten, nur im Footer verlinkt.

Pro Seite: hell ist Normalzustand, **max. eine** dunkle Sektion, Rostrot nur als
Akzent, viel Weißraum.

---

## Phase 4 — Anfrage-Formular (Wix Forms)

1. Über **+ Add** ein **Formular** (Wix Forms) auf Kontakt- und Homepage-Sektion
   (dasselbe Formular wiederverwenden).
2. **Felder** (aus dem Briefing):
   - Name · E-Mail · Sprache (DE/EN)
   - Art der Anfrage (Hochzeit / Paarshooting / Portrait / mobiles Studio /
     Sonstiges)
   - Datum / Zeitraum · Ort / Land · kurze Beschreibung
   - optionaler Budgetrahmen (weich formuliert, Briefing-Text)
   - „Wie habt ihr Seja gefunden?"
   - **Datenschutz-Checkbox** (Pflicht)
3. **Stil**: Felder im Palette-Look — **Linien statt Boxen** (nur untere Border
   `#B09993`), Hintergrund transparent/Off-White. Senden-Button Rostrot
   `#732E1F`.
4. **Benachrichtigung** an Svenjas E-Mail einrichten und **Testversand** prüfen.

---

## Phase 5 — Recht & DSGVO

1. **Impressum** und **Datenschutz** als Seiten füllen (Wix-Vorlagen anpassen,
   nicht blind übernehmen).
2. **Cookie-Banner / Consent** aktivieren, auf DE/EU einstellen.
3. **Google Fonts möglichst datenschutzfreundlich**; unnötige Drittanbieter-
   Skripte vermeiden.

---

## Phase 6 — SEO-Basics

Pro Seite (Site-Seiten-Panel → SEO-Einstellungen):

1. **Seitentitel** (Meta Title) — z. B. „Hochzeitsfotografin Deutschland &
   Niederlande | Seja Fotografie".
2. **Meta Description** — emotional + Keyword, ~150 Zeichen.
3. **Saubere URL-Slugs** (`/hochzeiten`, `/ueber-svenja` …).
4. **Alt-Texte** für **alle** Bilder direkt beim Einpflegen.
5. **Überschriften-Hierarchie** sauber (eine H1 pro Seite, dann H2/H3).
6. Struktur so anlegen, dass spätere regionale Landingpages und die EN-Version
   (Wix Multilingual) leicht ergänzbar sind.

---

## Phase 7 — Mobile-Durchgang

Harmony ist responsiv und passt vieles automatisch an — trotzdem oben in den
**Mobil-View** wechseln und jede Seite prüfen:

- Headlines ~32–40px, gut lesbar.
- Hochformat-Bilder als Standard, kein Layout-Chaos.
- Foto-Fade / Overlay auf Mobilhöhe prüfen.
- Scroll-Effekte werden mobil teils deaktiviert — okay, mobil zählt das stehende
  Bild.
- Formular einspaltig, CTA im sichtbaren Bereich.
- Überflüssige Elemente mobil ausblenden statt quetschen.

---

## Phase 8 — Veröffentlichen

1. **Vorschau** über alle Seiten (Desktop + Mobil); Scroll-Effekte und Fade nur
   hier/live korrekt sichtbar. Links und Formular testen.
2. **Texte von Svenja gegenlesen** lassen.
3. Testimonials-Sektion **ausgeblendet**, Reportage-Sektion vorhanden oder
   sauber ausgeblendet bis Material kommt.
4. **Veröffentlichen** — zunächst unter `wixsite.com`-URL. Die Domain
   `sejafotografie.com`/`.de` (im Editor als „verfügbar" angezeigt) später
   verbinden; Weiterleitung von `seja-fotografie-coaching.de` nachziehen.

---

## Nach dem Launch (nicht blockierend)

- **Testimonials** einblenden, sobald 2–3 Zitate da sind.
- **Adore-Webfont** (sobald Lizenz/Upload möglich) → ersetzt Playfair Display.
- **Englische Version** via **Wix Multilingual**.
- **Eigene Domain** + Weiterleitung.
- **Regionale SEO-Landingpages**.
- **Klick-Reportage** vervollständigen / zweite Reportage.

---

## Abgleich mit dem aktuellen Stand (Screenshot 2026-06-13)

Im aktuellen Editor stehen noch Template-Defaults, die von der abgestimmten
Designrichtung abweichen — diese beim Aufbau ersetzen:

| Aktuell im Editor | Abgestimmt → ändern auf |
|---|---|
| Logo-Subline „SEJA **Media & Fotografie**" | **„SEJA Fotografie"** (geklärt 2026-06-12) — richtige Logo-Variante verwenden |
| Hero-Claim „Ewige Erinnerungen in jedem Bild …" (generisch, „wir") | **„Nicht nur wie es aussah. Sondern wie es sich angefühlt hat."** — Svenjas „ich"-Stimme |
| CTA „**Jetzt buchen**" | **„Anfrage senden"** (zum Start kein Direkt-Buchung/Kalender) |
| Navigation „Home · Portfolioseite · (Profilfoto)" | **Hochzeiten · Portraits & Paare · Portfolio · Über Svenja · Kontakt** |
| Hero-Foto in **hartem Schwarz-Weiß** | warmes, atmosphärisches Bild — harte S/W-Kontraste sind ein Briefing-No-Go |

Gut ist bereits: der Ghost-CTA-Button in Rostrot und das helle, ruhige
Grundlayout mit großem Foto — das passt zur Richtung.

---

## Schnell-Checkliste

- [ ] Brand → Farben (9 Farben) hinterlegt
- [ ] Inhaltssektionen-Hintergrund exakt `#F4F1EE`
- [ ] Brand → Text: Playfair-Display-Headings (nicht Braggadocio) +
      Avenir-Light-Fließtext + Eyebrow-Stil (Textabschnitt 3)
- [ ] Header: richtiges Logo („SEJA Fotografie"), abgestimmtes Menü, Ghost-CTA
      „Anfrage senden"
- [ ] Footer: weißes Logo, Instagram, Impressum/Datenschutz
- [ ] Homepage-Sektionen 2.1–2.9 (Testimonials ausgeblendet)
- [ ] Foto-Fade + Freeze-Effekt funktionieren (in der Vorschau geprüft)
- [ ] Template-Defaults ersetzt (Claim, CTA, Navigation, Logo, Hero-Bild)
- [ ] Unterseiten Hochzeiten / Portraits & Paare / Portfolio / Über Svenja /
      Kontakt
- [ ] Impressum + Datenschutz
- [ ] Anfrage-Formular + Testversand geprüft
- [ ] SEO (Titel, Descriptions, Slugs, Alt-Texte) pro Seite
- [ ] Mobile-Durchgang
- [ ] Veröffentlicht
