from src.model import VoiceModel
from src.view import VoiceView 
class VoiceController:
    def __init__(self):
        self.model = VoiceModel()
        self.view = VoiceView()

        # ボタンと処理を接続
        self.view.record_button.clicked.connect(lambda: self.model.record())
        self.view.transcribe_button.clicked.connect(self.transcribe)
        self.view.save_button.clicked.connect(lambda: self.model.save())

    def transcribe(self):
        text = self.model.transcribe()
        self.view.text_display.setPlainText(text)

    def run(self):
        self.view.show()

