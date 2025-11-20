from recorder import record_audio
from transcriber import transcribe_audio
from saver import save_transcription

def main():
    audio_file = "recorded_audio.wav"
    text_file = "transcription.txt"

    record_audio(audio_file)
    transcription = transcribe_audio(audio_file)
    print("文字起こし結果:")
    print(transcription)
    save_transcription(transcription, text_file)

if __name__ == "__main__":
    main()