#!/usr/bin/env python3
"""Generiert Foto-Fade-Verlaufs-PNGs für die Wix-Site (Signatur-Element 1).

Der Harmony Editor kennt für Sektion-Hintergründe keinen Verlauf. Der
„Foto-Fade" (Bild läuft in die Off-White-Fläche aus) wird deshalb als
Overlay-Element gebaut: eine breite PNG-Grafik, die von oben transparent
nach unten in der Zielfarbe deckend verläuft. Über die untere Kante der
Foto-Sektion legen (volle Breite); die nächste Sektion hat exakt dieselbe
Farbe → das Foto „löst sich auf".

Die Alpha-Kurve ist eine Smoothstep-Blende (weicher als linear), damit der
Übergang ruhig wirkt. Unten ~12 % voll deckend, damit die Kante sicher
mit der Folgesektion verschmilzt.

Aufruf:  python3 design/foto-fade.py
Ausgabe: design/assets/foto-fade-offwhite.png  (transparent -> #F4F1EE)
         design/assets/foto-fade-dunkel.png    (transparent -> #181719)
"""

from pathlib import Path

from PIL import Image

WIDTH = 1920          # ausreichend breit; Wix streckt horizontal sauber
HEIGHT = 1000         # Höhe der Fade-Bahn
SOLID_TAIL = 0.12     # unterste 12 % voll deckend
GAMMA = 1.0           # Feinjustage der Kurvenmitte (1.0 = neutral)

VARIANTS = {
    "foto-fade-offwhite.png": (0xF4, 0xF1, 0xEE),  # Off-White
    "foto-fade-dunkel.png": (0x18, 0x17, 0x19),    # Fast-Schwarz
}


def smoothstep(t: float) -> float:
    """Klassisches Smoothstep 3t^2 - 2t^3 auf [0,1]."""
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def alpha_at(y: int) -> int:
    """Alpha 0 (oben) -> 255 (unten), Smoothstep + deckendes Ende."""
    pos = y / (HEIGHT - 1)
    if pos >= 1.0 - SOLID_TAIL:
        return 255
    t = pos / (1.0 - SOLID_TAIL)
    a = smoothstep(t) ** GAMMA
    return round(a * 255)


def build(color: tuple[int, int, int]) -> Image.Image:
    r, g, b = color
    # Eine Spalte berechnen, dann horizontal strecken (vertikaler Verlauf).
    column = Image.new("RGBA", (1, HEIGHT))
    column.putdata([(r, g, b, alpha_at(y)) for y in range(HEIGHT)])
    return column.resize((WIDTH, HEIGHT))


def main() -> None:
    out_dir = Path(__file__).resolve().parent / "assets"
    out_dir.mkdir(exist_ok=True)
    for name, color in VARIANTS.items():
        img = build(color)
        path = out_dir / name
        img.save(path)
        print(f"geschrieben: {path}  ({WIDTH}x{HEIGHT}, RGBA)")


if __name__ == "__main__":
    main()
