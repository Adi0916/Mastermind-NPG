# Mastermind NPG

Implementacja klasycznej gry logicznej Mastermind w języku Python z interfejsem graficznym opartym na **PySide6**. Zadaniem gracza jest odgadnięcie sekretnego kodu kolorów w ograniczonej liczbie prób.

## Funkcje gry

* **Konfigurowalny poziom trudności:** Możliwość ustawienia liczby pól (3–6) oraz maksymalnej liczby prób (5–20) w oknie menu.

* **Tryb Hardcore:** Stałe ustawienia (3 pola, 10 prób) bez wyświetlania historii wcześniejszych ruchów.

* **Historia ruchów i podpowiedzi:** Podgląd poprzednich prób wraz z informacją o trafieniach na właściwych pozycjach (*W dobrym miejscu*) oraz właściwych kolorach na innych pozycjach (*W złym miejscu*).

* **Statystyki:** Zapisywanie i podgląd liczby wygranych oraz przegranych partii.

* **Interaktywny interfejs GUI:** Kolorowe pola zmieniane kliknięciem z wykorzystaniem Qt (`PySide6`).

## Instalacja i uruchamianie

Domyślnie w głównym katalogu repozytorium nie ma gotowej paczki `.deb` — można ją pobrać z sekcji **Releases** (jeśli została opublikowana) albo zbudować i zainstalować samodzielnie.

### Linux — dwa sposoby uruchomienia

#### Sposób 1: Paczka `.deb`

1. **Pobranie lub samodzielne zbudowanie:**
   * Pobierz gotowy plik `*.deb` z [GitHub Releases](https://github.com/Adi0916/Mastermind-NPG/releases) (jeśli jest dostępny).
   * Lub zbuduj paczkę samodzielnie w katalogu głównym repozytorium (z wykorzystaniem przygotowanej struktury `deb-build/` zawierającej `DEBIAN`, `opt`, `usr`):

     ```bash
     dpkg-deb --build --root-owner-group deb-build mastermind_0.1.0_all.deb
     ```

2. **Instalacja:**

   ```bash
   sudo apt install ./mastermind_0.1.0_all.deb
   ```

3. **Uruchomienie:**

   ```bash
   mastermind
   ```

   *(Aplikacja w razie potrzeby automatycznie wymusza platformę `xcb` przy sesji Wayland; jeśli po instalacji w katalogu systemowym wystąpi problem z zapisem statystyk, upewnij się, że ścieżka zapisu wskazuje na katalog użytkownika.)*

4. **Odinstalowanie:**

   ```bash
   sudo apt remove mastermind
   ```

   *(Aby usunąć pakiet wraz z plikami konfiguracyjnymi/systemowymi: `sudo apt purge mastermind-npg`.)*

#### Sposób 2: Uruchomienie przez `uv`

1. Zainstaluj narzędzie [uv](https://docs.astral.sh/uv/).

2. Sklonuj repozytorium (lub pobierz i wypakuj archiwum źródłowe z Releases):

   ```bash
   git clone https://github.com/Adi0916/Mastermind-NPG.git
   cd Mastermind-NPG
   ```

3. Zsynchronizuj środowisko i zależności:

   ```bash
   uv sync
   ```

4. Uruchom aplikację:

   ```bash
   uv run src/mastermind_npg/__init__.py
   ```

### Windows i macOS — uruchomienie przez `uv`

Paczka `.deb` dotyczy wyłącznie systemów opartych na Debianie/Ubuntu — na **Windowsie** oraz **macOS** aplikację uruchamia się przez `uv` z repozytorium lub archiwum źródłowego:

1. Zainstaluj narzędzie [uv](https://docs.astral.sh/uv/) (np. w PowerShellu na Windowsie lub przez `brew` / skrypt instalacyjny na macOS).

2. Sklonuj repozytorium (lub pobierz i wypakuj archiwum źródłowe z Releases):

   ```bash
   git clone https://github.com/Adi0916/Mastermind-NPG.git
   cd Mastermind-NPG
   ```

3. Zsynchronizuj środowisko i zależności:

   ```bash
   uv sync
   ```

4. Uruchom aplikację:

   ```bash
   uv run src/mastermind_npg/__init__.py
   ```

## Jak grać

1. Uruchom grę.

2. *(Opcjonalnie)* Wejdź w **Menu**, aby zmienić poziom trudności, przełączyć **Tryb Hardcore** lub sprawdzić **Statystyki**.

3. Klikaj na kolorowe pola, aby przełączać się między 6 kolorami (*Czerwony, Niebieski, Zielony, Żółty, Fioletowy, Pomarańczowy*).

4. Kliknij **Zatwierdź**, aby sprawdzić swoją propozycję:

   * **W dobrym miejscu** — poprawny kolor na właściwej pozycji.

   * **W złym miejscu** — poprawny kolor, ale na innej pozycji.

5. Odgadnij cały kod przed wyczerpaniem dostępnych prób, aby wygrać.

## Struktura projektu

Projekt podzielony jest na moduły odpowiadające za uruchomienie aplikacji, interfejs graficzny oraz logikę gry:

```text
Mastermind-NPG/
├── pyproject.toml              # Konfiguracja projektu i zależności
├── uv.lock                     # Zablokowane wersje zależności dla uv
├── deb-build/                  # Struktura katalogów (DEBIAN, opt, usr) do budowy paczki .deb
└── src/
    ├── mastermind_npg/         # Punkt wejścia i inicjalizacja aplikacji Qt
    ├── gui/                    # Okno główne, menu opcji oraz komponenty pól/planszy
    └── rand/                   # Logika losowania kodu, sprawdzania prób i obsługa statystyk
```

## Współtwórcy

* M. Skowron

* K. Salamon

* J. Siuzdak

* M. Sakłak