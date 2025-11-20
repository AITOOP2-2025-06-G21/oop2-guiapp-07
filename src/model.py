# src/model.py
import os
import sys
from pathlib import Path

# プロジェクトルートをsys.pathに追加（必要に応じて）
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from voice.recorder import record_audio
from voice.transcriber import transcribe_audio
from voice.saver import save_transcription


class VoiceModel:
    """音声録音・文字起こしアプリのビジネスロジック"""

    def __init__(self):
        self.audio_filename = "recorded_audio.wav"
        self.text_filename = "transcription.txt"
        self.transcribed_text = ""

    def record(self, duration: int = 10):
        print(f"Model: {duration}秒間の録音を開始します...")
        record_audio(self.audio_filename, duration)
        print("Model: 録音が完了しました。")

    def transcribe(self) -> str:
        if not os.path.exists(self.audio_filename):
            error_msg = "エラー: 録音ファイルが見つかりません。先に録音してください。"
            print(error_msg)
            return error_msg

        print("Model: 文字起こし処理を実行中...")
        self.transcribed_text = transcribe_audio(self.audio_filename)
        print("Model: 文字起こし完了")
        return self.transcribed_text

    def save(self):
        if not self.transcribed_text.strip():
            print("警告: 保存するテキストがありません。")
            return

        save_transcription(self.transcribed_text, self.text_filename)
        print(f"Model: 結果を {self.text_filename} に保存しました。")

    def get_current_text(self) -> str:
        return self.transcribed_text
