# Projekt 6 – Automatizované testy v Playwright

Tento projekt obsahuje 3 automatizované testy webové stránky Rohlik.cz.  
Testy jsou napsané v Pythonu pomocí frameworku Playwright a pluginu pytest-playwright.

## Testovaná stránka

https://www.rohlik.cz

## Co testy ověřují

1. Vyhledání produktu zobrazí výsledky hledání.
2. Kliknutí na tlačítko Přihlásit otevře přihlašovací formulář.
3. Kontaktní stránka obsahuje adresu společnosti.

## Použité technologie

- Python
- pytest
- Playwright
- pytest-playwright

## Instalace závislostí

Nejprve je potřeba nainstalovat Python balíčky:

```bash
pip install -r requirements.txt

Poté je potřeba jednorázově nainstalovat prohlížeče pro Playwright:

python -m playwright install