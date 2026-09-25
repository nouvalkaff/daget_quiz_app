from config import DIR_PATH_IDN


class BankSoalApp:
    def ambil_soal(self) -> list[str]:
        try:
            with DIR_PATH_IDN.open(encoding="utf-8") as file:
                return [baris.strip() for baris in file if self._valid(baris.strip())]
        except FileNotFoundError:
            return []

    @staticmethod
    def _valid(baris: str) -> bool:
        bagian = baris.split("|", 1)
        if len(bagian) != 2 or not bagian[0].strip():
            return False
        opsi = [pilihan.strip() for pilihan in bagian[1].split("#")]
        return len(opsi) == 4 and all(opsi) and len(set(opsi)) == 4
