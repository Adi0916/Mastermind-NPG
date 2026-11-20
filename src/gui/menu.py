#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import (
    QSizePolicy, QSpacerItem, QLabel, QDialog,
    QPushButton, QSpinBox, QVBoxLayout, QMessageBox, QDialogButtonBox
)
from PySide6.QtGui import Qt


class OptionsDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu")
        self.setFixedSize(200, 250)

        # Pobierz aktualne wartości z głównego okna, jeśli istnieje
        self.ilość_boxów = getattr(parent, "ilość_boxów", 3)
        self.max_attempts = getattr(parent, "max_attempts", 10)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        label = QLabel("Wybierz opcję:")
        layout.addWidget(label, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.hardcore_button = QPushButton("Tryb Hardcore")
        layout.addWidget(self.hardcore_button)
        self.hardcore_button.clicked.connect(self.przelacz_tryb_hardcore)

        self.statystyki_button = QPushButton("Statystyki")
        self.statystyki_button.clicked.connect(self.pokaz_statystyki)
        layout.addWidget(self.statystyki_button)

        self.poziom_trud_button = QPushButton("Poziom trudności")
        layout.addWidget(self.poziom_trud_button)
        self.poziom_trud_button.clicked.connect(self.wybierz_trudnosc)

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)
        self.setLayout(layout)

    def przelacz_tryb_hardcore(self):
        parent = self.parent()
        if parent:
            parent.hardcore_mode = not parent.hardcore_mode  # type: ignore

            if parent.hardcore_mode:  # type: ignore
                parent.ilość_boxów = 3  # type: ignore
                parent.max_attempts = 10  # type: ignore

            parent.reset_game()  # type: ignore
            self.accept()

    def wybierz_trudnosc(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Ustawienia poziomu trudności")
        dialog.setModal(True)
        dialog.setFixedSize(300, 200)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Maksymalna liczba prób:"))
        attempts_spinbox = QSpinBox()
        attempts_spinbox.setRange(5, 20)
        attempts_spinbox.setValue(self.max_attempts)
        layout.addWidget(attempts_spinbox)

        layout.addWidget(QLabel("Ilość pól do zgadnięcia:"))
        difficulty_spinbox = QSpinBox()
        difficulty_spinbox.setRange(3, 6)
        difficulty_spinbox.setValue(self.ilość_boxów)
        layout.addWidget(difficulty_spinbox)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)  # type: ignore
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:  # type: ignore
            self.max_attempts = attempts_spinbox.value()
            self.ilość_boxów = difficulty_spinbox.value()
            if self.parent() is not None:
                self.parent().hardcore_mode = False  # type: ignore
            self.accept()

    def pokaz_statystyki(self):
            dialog = QDialog(self)
            dialog.setWindowTitle("Statystyki gry")
            dialog.setFixedSize(220, 150)

            layout = QVBoxLayout(dialog)

            label = QLabel(
                f"Wygrane: {self.parent().wygrane}\nPrzegrane: {self.parent().przegrane}"  # type: ignore
            )
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

            ok_button = QPushButton("OK", dialog)
            ok_button.clicked.connect(dialog.accept)
            layout.addWidget(ok_button)

            dialog.exec()