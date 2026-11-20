#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QApplication
import sys
from gui.interfejs import MyApp

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())

# Uruchomienie
if __name__ == "__main__":
    main()

