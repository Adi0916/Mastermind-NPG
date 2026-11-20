# Mastermind NPG

A desktop implementation of the classic Mastermind logic game written in Python with a **PySide6** graphical user interface. Try to crack the secret color code within a limited number of attempts.

## Features

- **Customizable Difficulty:** Adjust the number of code slots (3–6) and maximum attempts (5–20) in the options menu.
- **Hardcore Mode:** Fixed 3-slot, 10-attempt challenge with move feedback history hidden.
- **Attempt History & Feedback:** Track your guesses with indicators for exact matches (*"W dobrym miejscu"*) and color-only matches (*"W złym miejscu"*).
- **Persistent Statistics:** Tracks total wins and losses across sessions.
- **Responsive GUI:** Interactive color-cycling tiles built with Qt (`PySide6`).

## Installation & Running

### Option 1: Linux (`.deb` package)

1. Download `mastermind-npg_0.1.0_amd64.deb` from the [GitHub Releases](https://github.com/Adi0916/Mastermind-NPG/releases) page.
2. Install the package using `apt`:
   ```bash
   sudo apt install ./mastermind-npg_0.1.0_amd64.deb
   ```
3. Launch the game from your terminal:
   ```bash
   mastermind-npg
   ```

### Option 2: Windows / macOS / Linux (via `uv`)

1. Make sure you have [uv](https://docs.astral.sh/uv/) installed.
2. Clone the repository (or download and extract the source archive from Releases):
   ```bash
   git clone https://github.com/Adi0916/Mastermind-NPG.git
   cd Mastermind-NPG
   ```
3. Install dependencies and create the virtual environment:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run src/mastermind_npg/__init__.py
   ```

## How to Play

1. Launch the application.
2. *(Optional)* Open **Menu** to configure the difficulty level (number of slots and attempts), toggle **Hardcore Mode**, or view your win/loss **Statistics**.
3. Click on each colored box to cycle through the 6 available colors (*Red, Blue, Green, Yellow, Purple, Orange*).
4. Click **Zatwierdź** (Submit) to check your guess:
   - **W dobrym miejscu (In the right spot):** Right color in the exact right position.
   - **W złym miejscu (In the wrong spot):** Right color, but in a different position.
5. Guess the entire secret code before running out of attempts to win.

## Project Structure

```text
Mastermind-NPG/
├── pyproject.toml                  # Project configuration and dependencies (PySide6)
├── uv.lock                         # Locked dependency versions for uv
└── src/
    ├── mastermind_npg/
    │   └── __init__.py             # Application entry point (initializes QApplication)
    ├── gui/
    │   ├── interfejs.py            # Main game window, board layout, game loop, and stats I/O
    │   ├── boxy_kolorowe.py        # ColorBox widget handling color cycling and styling
    │   └── menu.py                 # OptionsDialog (difficulty settings, Hardcore Mode, stats)
    └── rand/
        ├── losowanie_kolorów.py    # Secret code generator (Kolor) and guess checker (sprawdz_kod)
        └── statystyki.txt          # Plain-text win/loss counter (line 1: wins, line 2: losses)
```

## Contributors

- M. Skowron
- K. Salamon
- J. Siuzdak
- M. Sakłak