from config import JUMLAH_SOAL


def evaluasi_nilai(jawaban_benar: int) -> str:
    if jawaban_benar == JUMLAH_SOAL:
        return "Alhamdulillah, semua jawaban benar! Ini hadiahmu:"
    if jawaban_benar == 2:
        return "Dikit lagi 😭 Nanggung amat sih, wkwk. Coba lagi!"
    if jawaban_benar == 1:
        return "Yah, baru 1 benar 😭 Belajar lagi, wkwk. Coba lagi!"
    return "Belum ada yang benar. Yuk coba lagi!"
