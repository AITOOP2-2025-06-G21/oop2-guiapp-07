import sys
from PySide6.QtWidgets import QApplication

from src.interface import VoiceController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = VoiceController()
    controller.run()
    sys.exit(app.exec())