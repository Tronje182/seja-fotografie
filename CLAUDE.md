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

### Bewährte Lese-Probes (Onboarding-Check)

```bash
# Site Properties (kanonischer Berechtigungs-Check)
curl -s -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  https://www.wixapis.com/site-properties/v4/properties

# CMS-Collections
curl -s -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  https://www.wixapis.com/wix-data/v2/collections

# Media Manager
curl -s -X POST -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  -H "Content-Type: application/json" -d '{}' \
  https://www.wixapis.com/site-media/v1/files/search

# Members
curl -s -H "Authorization: $WIX_API_KEY" -H "wix-site-id: $SITE" \
  "https://www.wixapis.com/members/v1/members?paging.limit=1"
```

Interpretation: ungültiger Key → 401; gültiger Key ohne Berechtigung → 403
(site-properties nennt dabei die fehlende Permission, z. B.
`site-settings.view`); HTML-Fehlerseiten von Wix sind ebenfalls 403/404.

## Aktueller Stand (2026-06-12)

- Netzwerk und Authentifizierung funktionieren: ungültiger Key → 401, unser
  Key → 403 mit benanntem Berechtigungsfehler.
- **Der Key hat weiterhin KEINE Berechtigungen auf der Site.** Alle
  Lese-Probes (site-properties, wix-data/collections, members,
  site-media/files) liefern 403; site-properties meldet explizit
  `Unauthorized to perform site-settings.view`.
- Nächster Schritt (Owner): unter https://manage.wix.com/account/api-keys dem
  Key Berechtigungen geben — mindestens Site Properties lesen, CMS/Wix Data,
  Media Manager; optional Members und SEO.
- Sobald Berechtigungen da sind: Onboarding-Check wiederholen, dann
  Bestandsaufnahme der Site (Seitenstruktur, CMS-Collections,
  Media-Bestand) erstellen.
- Design-Arbeit: noch keine Inspirationsseiten analysiert, noch keine
  Designrichtung festgelegt.

## Repo

- GitHub: `Tronje182/seja-fotografie`
- Dieses Repo war bis zum 2026-06-12 leer; diese CLAUDE.md ist der erste Inhalt.
