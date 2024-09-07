import speech_recognition as sr

# Buat objek recognizer
recognizer = sr.Recognizer()

# Tentukan file audio yang akan di-transkripsi
audio_file = "1.wav"  # Ganti dengan lokasi file audio Anda

# Buka file audio menggunakan SpeechRecognition
with sr.AudioFile(audio_file) as source:
    # Membaca konten audio sebagai data audio
    audio_data = recognizer.record(source)

    try:
        # Gunakan recognizer untuk mendapatkan teks dari audio
        text = recognizer.recognize_google(audio_data, language="id-ID")  # Menggunakan bahasa Indonesia
        print("Transkripsi: " + text)
    except sr.UnknownValueError:
        print("Speech Recognition tidak dapat mengenali audio")
    except sr.RequestError as e:
        print("Speech Recognition gagal; {0}".format(e))
