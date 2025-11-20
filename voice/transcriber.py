import mlx_whisper
from pydub import AudioSegment
import numpy as np

def preprocess_audio(sound: AudioSegment) -> AudioSegment:
    """
    Whisper用に音声を16kHz, 16bit, モノラルに変換。
    戻り値は、音声そのもの。
    """
    if sound.frame_rate != 16000:
        sound = sound.set_frame_rate(16000)
    if sound.sample_width != 2:
        sound = sound.set_sample_width(2)
    if sound.channels != 1:
        sound = sound.set_channels(1)
    return sound

def transcribe_audio(audio_path: str, model_path: str = "whisper-base-mlx") -> str:
    """
    音声ファイルを文字起こししてテキストを返す。
    戻り値は、str型のテキスト。
    """
    audio = AudioSegment.from_file(audio_path, format="wav")
    processed = preprocess_audio(audio)
    arr = np.array(processed.get_array_of_samples()).astype(np.float32) / 32768.0
    result = mlx_whisper.transcribe(arr, path_or_hf_repo=model_path)
    return result["text"]