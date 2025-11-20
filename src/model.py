import sys
from pathlib import Path

# プロジェクトルートを sys.path に追加
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from voice.recorder import record_audio
from voice.transcriber import transcribe_audio
from voice.saver import save_transcription
import os


class VoiceModel:
    """
    音声録音・文字起こしアプリのビジネスロジックを担当するクラス
    """
    def __init__(self):
        # データを保持する変数（状態）
        self.audio_filename = "recorded_audio.wav"
        self.text_filename = "transcription.txt"
        self.transcribed_text = "" # 文字起こし結果をここに保存する

    def record(self, duration=10):
        """
        録音を行うメソッド
        :param duration: 録音時間（秒）
        """
        print(f"Model: {duration}秒間の録音を開始します...")
        # 既存のrecorder機能を使用
        record_audio(self.audio_filename, duration)
        print("Model: 録音が完了しました。")

    def transcribe(self):
        """
        録音した音声の文字起こしを行うメソッド
        :return: 文字起こしされたテキスト
        """
        if not os.path.exists(self.audio_filename):
            print("エラー: 録音ファイルが見つかりません。先に録音してください。")
            return "エラー: 録音ファイルなし"

        print("Model: 文字起こし処理を実行中...")
        # 既存のtranscriber機能を使用
        # 結果をインスタンス変数(self.transcribed_text)に保存しておく
        self.transcribed_text = transcribe_audio(self.audio_filename)
        
        print("Model: 文字起こし完了")
        return self.transcribed_text

    def save(self):
        """
        現在の文字起こし結果をファイルに保存するメソッド
        """
        if not self.transcribed_text:
            print("警告: 保存するテキストがありません。")
            return

        # 既存のsaver機能を使用
        save_transcription(self.transcribed_text, self.text_filename)
        print(f"Model: 結果を {self.text_filename} に保存しました。")

    def get_current_text(self):
        """
        現在保持しているテキストデータを返す（GUI表示用）
        """
        return self.transcribed_text

