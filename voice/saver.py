def save_transcription(text: str, output_path: str = "transcription.txt"):
    """
    文字起こし結果をテキストファイルに保存する。
    出力されるファイルは、デフォルトで"transcription.txt"である。
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"文字起こし結果を {output_path} に保存しました。")