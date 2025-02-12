from gtts import gTTS

namaWisata = "Wisata Dufan Taman Impian Jaya Ancol"
# Teks dalam Bahasa Indonesia
text = f"""Selamat datang di {namaWisata}!  
Nikmati berbagai wahana dan pengalaman seru bersama kami.  
Pastikan Anda mengikuti peraturan keselamatan dan selamat bersenang-senang!  

"""

# Konversi teks ke suara dalam Bahasa Indonesia
tts = gTTS(text, lang="id")
tts.save("output_audio.mp3") 
print("✅ Teks berhasil dikonversi ke suara!")
