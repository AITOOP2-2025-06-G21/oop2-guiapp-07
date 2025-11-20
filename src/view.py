from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout
)
from PySide6.QtCore import Qt

class AudioTranscriptionView(QWidget):
    """
    シンプル版の音声文字起こしビュー。
    録音 → 文字起こし → 結果の表示 → 保存 の基本UI。
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("音声文字起こしアプリ")
        self.resize(480, 400)

    
        self.label_status = QLabel("準備完了")
        self.label_status.setAlignment(Qt.AlignCenter)


        self.btn_record = QPushButton("録音開始")
        self.btn_transcribe = QPushButton("文字起こし")
        self.btn_save = QPushButton("結果を保存")


        self.text_result = QTextEdit()
        self.text_result.setPlaceholderText("ここに文字起こし結果が表示されます")

        # ---- レイアウト構成 ----
        layout = QVBoxLayout()
        layout.addWidget(self.label_status)
        layout.addWidget(self.btn_record)
        layout.addWidget(self.btn_transcribe)
        layout.addWidget(self.btn_save)
        layout.addWidget(self.text_result)

        self.setLayout(layout)

    def update_status(self, text: str):
        """ステータス表示を更新する"""
        self.label_status.setText(text)

    def set_result_text(self, text: str):
        """文字起こし結果テキストを表示"""
        self.text_result.setPlainText(text)
