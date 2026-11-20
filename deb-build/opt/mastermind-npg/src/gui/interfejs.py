#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QLabel, QDialog, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PySide6.QtGui import Qt

from rand.losowanie_kolorów import Kolor, sprawdz_kod
from gui.menu import OptionsDialog
from gui.boxy_kolorowe import ColorBox


class MyApp(QWidget):

    def show_options_dialog(self):
        dialog = OptionsDialog(self)
        if dialog.exec() == QDialog.Accepted:  # type: ignore
            old_max_attempts = self.max_attempts
            old_ilość_boxów = self.ilość_boxów

            self.max_attempts = dialog.max_attempts
            self.ilość_boxów = dialog.ilość_boxów

            if old_max_attempts != self.max_attempts or old_ilość_boxów != self.ilość_boxów:
                self.reset_game()

    def restart_game_button(self):
        self.reset_game()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gra mastermind")

        self.boxes = []
        self.history_entries = []

        self.ilość_boxów = 3
        self.max_attempts = 10
        self.current_attempt = 0

        self.hardcore_mode = False

        self.statystyki_plik = "src/rand/statystyki.txt"
        self.wygrane = 0
        self.przegrane = 0
        self.wczytaj_statystyki()

        self.submit_button = QPushButton("Zatwierdź", self)
        self.submit_button.setFixedSize(100, 40)
        self.submit_button.clicked.connect(self.sprawdz)

        self.attempts_label = QLabel(f"Pozostało prób: {self.max_attempts}", self)
        self.attempts_label.move(10, 10)
        self.attempts_label.setStyleSheet("font-size: 16px;")
        self.attempts_label.adjustSize()

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)  # type: ignore
        self.result_label.setStyleSheet("font-size: 24px;")

        self.history_scroll = QScrollArea(self)
        self.history_scroll.setWidgetResizable(True)

        self.history_widget = QWidget()
        self.history_layout = QVBoxLayout(self.history_widget)
        self.history_scroll.setWidget(self.history_widget)

        self.menu_button = QPushButton("Menu", self)
        self.menu_button.setFixedSize(80, 25)
        self.menu_button.clicked.connect(self.show_options_dialog)

        self.restart_button = QPushButton("Restart", self)
        self.restart_button.setFixedSize(80, 25)
        self.restart_button.clicked.connect(self.restart_game_button)

        self.hardcore_label = QLabel("TRYB HARDCORE", self)
        self.hardcore_label.setStyleSheet("color: red; font-size: 20px; font-weight: bold;")
        self.hardcore_label.hide()

        self.reset_game()

    def wczytaj_statystyki(self):
        try:
            with open(self.statystyki_plik, "r") as f:
                linie = f.readlines()
                self.wygrane = int(linie[0].strip())
                self.przegrane = int(linie[1].strip())
        except (FileNotFoundError, IndexError, ValueError):
            self.wygrane = 0
            self.przegrane = 0

    def zapisz_statystyki(self):
        with open(self.statystyki_plik, "w") as f:
            f.write(f"{self.wygrane}\n{self.przegrane}")

    def tajny_kod_na_emoji(self):
        emoji = {
            1: "🟥",
            2: "🟦",
            3: "🟩",
            4: "🟨",
            5: "🟪",
            6: "🟧"
        }

        self.kod_emoji = []
        for liczba in self.secret_code:
            self.kod_emoji += emoji[liczba]
        return ''.join(self.kod_emoji)

    def ustawienie_wielkości_interfejsu(self):
        box_width = 100
        spacing = 20
        side_margin = 40  # 20px z lewej i 20px z prawej

        total_boxes_width = self.ilość_boxów * box_width + (self.ilość_boxów - 1) * spacing
        window_width = max(440, total_boxes_width + side_margin * 2)
        window_height = 800

        self.setFixedSize(window_width, window_height)
        self.history_scroll.setGeometry(20, 300, window_width - 40, 480)

        self.menu_button.move(self.width() - 95, 10)

        self.restart_button.move(self.width() - 180, 10)


        wspolrzedna_x = (self.width() - self.submit_button.width()) // 2
        wspolrzedna_y = 200
        self.submit_button.move(wspolrzedna_x, wspolrzedna_y)

        self.result_label.setFixedWidth(self.width() - 40)
        self.result_label.move((self.width() - self.result_label.width()) // 2, 250)

        # Wycentrowanie istniejących boxów po zmianie rozmiaru okna
        if self.boxes:
            start_x = (self.width() - total_boxes_width) // 2
            for i, box in enumerate(self.boxes):
                box.move(start_x + i * (box_width + spacing), 50)

    def reset_game(self):
        for box in getattr(self, 'boxes', []):
            box.deleteLater()

        if self.hardcore_mode:
            self.ilość_boxów = 3
            self.max_attempts = 10

        self.secret_code = [Kolor().get_liczba() for _ in range(self.ilość_boxów)]

        self.ustawienie_wielkości_interfejsu()

        box_width = 100
        spacing = 20
        total_boxes_width = self.ilość_boxów * box_width + (self.ilość_boxów - 1) * spacing
        start_x = (self.width() - total_boxes_width) // 2

        self.boxes = []
        for i in range(self.ilość_boxów):
            box = ColorBox(start_x + i * (box_width + spacing), 50, self)
            box.show()
            self.boxes.append(box)

        for entry in self.history_entries:
            entry.deleteLater()
        self.history_entries.clear()

        self.current_attempt = 0
        self.pozostalo = self.max_attempts
        self.attempts_label.setText(f"Pozostało prób: {self.pozostalo}")
        self.attempts_label.adjustSize()

        self.result_label.setText("")
        self.submit_button.setEnabled(True)

        self.hardcore_label.adjustSize()
        x = self.attempts_label.x() + self.attempts_label.width() + 10
        y = self.attempts_label.y()
        self.hardcore_label.move(x, y)

        if self.hardcore_mode:
            self.hardcore_label.show()
        else:
            self.hardcore_label.hide()

    def sprawdz(self):
        if not self.submit_button.isEnabled():
            return

        propozycja = [box.get_value() for box in self.boxes]
        wynik = sprawdz_kod(propozycja, self.secret_code, self.ilość_boxów)

        czarna = wynik.count('czarna')  # type: ignore
        biała = wynik.count('biała')  # type: ignore

        self.current_attempt += 1
        self.pozostalo = self.max_attempts - self.current_attempt
        self.attempts_label.setText(f"Pozostało prób: {self.pozostalo}")
        self.attempts_label.adjustSize()

        self.hardcore_label.adjustSize()
        x = self.attempts_label.x() + self.attempts_label.width() + 10
        y = self.attempts_label.y()
        self.hardcore_label.move(x, y)

        if not self.hardcore_mode:
            history_label = QLabel(
                f"{len(self.history_entries) + 1}. W dobrym miejscu: {czarna}    W złym miejscu: {biała}")
            history_label.setStyleSheet("font-size: 18px; margin: 5px;")
            self.history_layout.addWidget(history_label)
            self.history_entries.append(history_label)

            self.history_scroll.verticalScrollBar().setValue(
                self.history_scroll.verticalScrollBar().maximum()
            )

        if czarna == self.ilość_boxów:
            self.result_label.setText("😁Wygrałeś😁")
            self.submit_button.setEnabled(False)
            self.wygrane += 1
            self.zapisz_statystyki()
        elif self.current_attempt >= self.max_attempts:
            self.result_label.setText(f"😭Przegrałeś😭 Kod: {self.tajny_kod_na_emoji()}")
            self.submit_button.setEnabled(False)
            self.przegrane += 1
            self.zapisz_statystyki()

