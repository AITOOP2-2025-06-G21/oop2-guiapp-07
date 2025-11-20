from src.model import VoiceModel
from src.view import AudioTranscriptionView


class VoiceController:
    def __init__(self):
        self.model = VoiceModel()
        self.view = AudioTranscriptionView()

        # 正しいインスタンス変数名で接続
        self.view.btn_record.clicked.connect(self.start_recording)
        self.view.btn_transcribe.clicked.connect(self.transcribe)
        self.view.btn_save.clicked.connect(self.model.save)

        self.view.update_status("準備完了")

    def start_recording(self):
        self.view.update_status("録音中…（10秒間）")
        self.view.set_result_text("")
        self.model.record(duration=10)  # 10秒録音
        self.view.update_status("録音完了 → 「文字起こし」ボタンを押してください")

    def transcribe(self):
        self.view.update_status("文字起こし処理中…（少し時間がかかります）")
        text = self.model.transcribe()
        self.view.set_result_text(text)
        self.view.update_status("文字起こし完了！ → 「結果を保存」で保存できます")

    def run(self):
        self.view.show()

