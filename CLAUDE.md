# Seja Fotografie — Projektkontext

## Projekt

Wir helfen Svenja, ihre Fotografie-Website auf Wix aufzusetzen. Das Layout wird
manuell im Wix-Editor gebaut; dieses Repo dient als Arbeits- und Wissensbasis
für Claude-Sessions (Konzepte, Analysen, API-Skripte, Projektstand).

## Rollen von Claude

1. **Design-Berater**: Svenja sammelt Inspirationsseiten. Claude analysiert sie
   (Layout, Typografie, Farben, Bildsprache, Navigation) und leitet daraus eine
   konsistente Designrichtung ab. Ergebnis sind Konzepte und konkrete
   Anweisungen für den Wix-Editor — kein automatisierter Layout-Bau.
2. **Wix-API-Arbeiter**: Lesen und Berichten über die Site per Wix REST API.
   **Schreiboperationen nur auf ausdrückliche Anweisung.**

## Wix-API-Konventionen

- **Site-ID**: `1f8308b9-7e8c-471f-ac37-488ac3ca2fa9`
- **Site-URL** (noch unveröffentlicht): https://sdobbelstein.wixsite.com/seja-fotografie
- **API-Key**: liegt in der Umgebungsvariable `WIX_API_KEY`
  (Account-API-Key; **Wert niemals ausgeben oder loggen**).
- **Basis-URL**: `https://www.wixapis.com`
- **Header** für Site-Ebene-APIs:
  - `Authorization: $WIX_API_KEY` — roher Key, **kein** `Bearer`-Präfix
  - `wix-site-id: 1f8308b9-7e8c-471f-ac37-488ac3ca2fa9`
- Account-Ebene-APIs brauchen stattdessen den Header `wix-account-id`
  (Account-ID noch unbekannt).
- Grundsatz: erst lesen und berichten; nichts an der Site verändern, solange
  Svenja/der Owner es nicht ausdrücklich anweist.

### Bewährte Lese-Endpunkte

```bash
SITE="1f8308b9-7e8c-471f-ac37-488ac3ca2fa9"

# Site Properties (kanonischer Berechtigungs-Check) — funktioniert
curl -s -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  https://www.wixapis.com/site-properties/v4/properties

# Media Manager: Dateien + Ordner — funktioniert
curl -s -X POST -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  -H "Content-Type: application/json" -d '{"paging":{"limit":100}}' \
  https://www.wixapis.com/site-media/v1/files/search
curl -s -X POST -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  -H "Content-Type: application/json" -d '{}' \
  https://www.wixapis.com/site-media/v1/folders/search

# Members — funktioniert
curl -s -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  "https://www.wixapis.com/members/v1/members?paging.limit=1"

# CMS / Wix Data — Berechtigung vorhanden, aber Site-seitig nicht aktiv:
# GET /wix-data/v2/collections → 400 „WDE0110: Wix Code not enabled".
# D. h. auf der Site ist kein CMS/Wix Code aktiviert. Falls Collections
# gewünscht: im Wix-Editor das CMS hinzufügen (bzw. Dev-Modus aktivieren).
```

Interpretation der Statuscodes: ungültiger Key → 401; gültiger Key ohne
Berechtigung → 403 (site-properties nennt dabei die fehlende Permission,
z. B. `site-settings.view`); falsche Pfade und Wix-HTML-Fehlerseiten → 404.

**Keine Seitenstruktur-API gefunden**: Für klassische Wix-Editor-Sites gibt es
keinen REST-Endpunkt für die Seitenliste (diverse Kandidaten → 404). Die
Live-Sitemap geht erst nach Veröffentlichung der Site.

## Bestandsaufnahme der Site (Stand 2026-06-12)

- **Name/Branding**: „Seja Fotografie", Claim/Beschreibung „Ewige Erinnerungen
  in jedem Bild". Kategorie: photography / Hochzeitsfotografiestudio.
- **Locale**: Deutsch (DE), Währung EUR, Zeitzone Europe/Berlin.
- **Veröffentlichung**: Die Site ist noch **nicht publiziert**
  (Live-URL liefert 404).
- **Media Manager**: 68 Dateien, alle Bilder:
  - Ordner „Portfolio" (`0b5aa1743f074373a6d6149ea8627975`): 54 große
    Original-JPGs (`DSC_*.jpg`, je ca. 5–15 MB) — das eigentliche Portfolio.
  - Zweiter Ordner „Portfolio" (`3646b983ca694351a7f32bb72bfcb0cb`): 6 kleine
    JPGs mit UUID-Namen (~0,2–0,3 MB), vermutlich Testbilder/Duplikat-Ordner.
  - Ordner „My Logos": leer.
  - Root: Logo-PNGs, 3 KI-generierte Bilder, 1 großes JPG, 3 kleine UUID-JPGs.
  - Hinweis fürs Design: Die Portfolio-JPGs sind unkomprimierte Originale;
    für die Live-Site übernimmt Wix die Auslieferungs-Optimierung, aber die
    Bildauswahl/Kuratierung steht noch aus.
  - **Herkunft der Portfolio-Bilder**: bestätigt von Svenja (geklärt
    2026-06-12). EXIF: Nikon D750, einheitlich mit Adobe Lightroom (Mac)
    bearbeitet. Die EXIF-Aufnahmedaten (2014) sind eine falsch gestellte
    Kamera-Uhr.
- **Members**: 1 Mitglied (sdobbelstein = Svenja/Owner, angelegt 2026-05-14).
- **CMS**: nicht eingerichtet — Wix Data meldet `WDE0110: Wix Code not
  enabled`. Der API-Key hat inzwischen alle vergebbaren Berechtigungen
  (Stand 2026-06-12, vom Owner bestätigt); das CMS müsste bei Bedarf im
  Wix-Editor aktiviert werden.
- **Design-Arbeit** (Stand 2026-06-12): Briefing und Inspirationen liegen vor
  und sind analysiert:
  - `briefing/onboarding-briefing.md` — strategisches Onboarding-Briefing
    (Positionierung, Zielgruppe, Seitenstruktur, Tonalität, SEO, No-Gos).
  - `design/inspirationen.md` — Analyse der Referenzen
    thelightseeker.photography (WordPress/Divi) und amourfotografie.com
    (selbst eine Wix-Site!) inkl. Svenjas Notizen.
  - `design/designrichtung.md` — Designrichtung v2 „Quiet Editorial",
    abgeglichen mit Svenjas Brandkit (SEJA-Wortmarke, Hände-Motiv,
    Palette Rostrot/Greige/Dusty Rose auf hellem Grund, dunkle
    About-Kontrast-Sektion): Farbpalette, Typografie (Brand-Serif bzw.
    Prata-Fallback + Avenir/Raleway), fünf Signatur-Elemente (Foto-Fade,
    Linien+Schrift im Bild, Foto-Trenner, Reveal-Scroll-Effekt, Weißraum)
    und konkrete Wix-Editor-Anweisungen.
  - **Offen**: Name/Dateien/Lizenz der Brand-Display-Serif; Einsatz des
    Script-Fonts klären; Bildmaterial kommt via Google Drive → danach
    Kuratierung (Hero, Foto-Trenner, Reportage, Svenja-Portrait).

## Repo

- GitHub: `Tronje182/seja-fotografie`
- Hauptbranch: `main`. Achtung: GitHub hat als Default-Branch zunächst
  `claude/happy-maxwell-0j22wz` gesetzt (erster Push in leeres Repo);
  der Default muss einmalig in den GitHub-Settings auf `main` umgestellt
  werden, falls noch nicht geschehen.
- Arbeitsweise: Feature-Branches, PR gegen `main`.
