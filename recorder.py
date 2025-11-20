import ffmpeg

def record_audio(output_file: str = "recorded_audio.wav", duration: int = 10):
    """
    マイクから音声を録音し、WAVファイルとして保存する。
    ファイルの名前は、デフォルトで"recorded_audio.wav"である。
    """
    print(f"{duration}秒間、マイクから録音を開始します...")
    try:
        (
            ffmpeg
            .input(':0', format='avfoundation', t=duration)
            .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
            .run(overwrite_output=True)
        )
        print(f"録音が完了しました。ファイル: {output_file}")
    except ffmpeg.Error as e:
        print(f"FFmpegエラー: {e.stderr.decode()}")
    except Exception as e:
        print(f"予期せぬエラー: {e}")