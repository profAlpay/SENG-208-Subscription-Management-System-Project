import csv

def load_data_from_csv(file_path):
    """
    Verileri CSV dosyasından okur ve bir sözlük olarak döndürür.

    Args:
        file_path (str): CSV dosyasının yolu.

    Returns:
        dict: Verileri içeren bir sözlük.
    """
    data_dict = {}
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_dict[row["Abonelik"]] = float(row["Aylık Ücret"])
    return data_dict

def toplam_gider_hesapla(abonelikler):
    """
    Verilen aboneliklerin toplam giderini hesaplar.

    Args:
        abonelikler (dict): Abonelik adları ve aylık ücretleri içeren bir sözlük.

    Returns:
        float: Toplam abonelik gideri.
    """
    toplam_gider = sum(abonelikler.values())
    return toplam_gider

# Örnek CSV dosyası yolu
csv_file_path = "subscriptions.csv"

# Verileri yükle
abonelikler_dict = load_data_from_csv(csv_file_path)

# Toplam abonelik giderini hesapla
toplam_abonelik_gideri = toplam_gider_hesapla(abonelikler_dict)

print(f"Toplam abonelik gideri: ${toplam_abonelik_gideri:.2f}")
