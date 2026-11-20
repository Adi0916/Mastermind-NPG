#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get("XDG_SESSION_TYPE") == "wayland" and "QT_QPA_PLATFORM" not in os.environ:
    os.environ["QT_QPA_PLATFORM"] = "xcb"

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

