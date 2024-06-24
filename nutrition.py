def calculate_nutritional_needs(age_group, trimester):
    nutritional_standards = {
        1: {"Kelompok Umur": "16 - 18 Tahun", "Berat Badan": 52, "Tinggi Badan": 159, "Energi": 2100, "Protein": 65, "Lemak": 70, "Karbohidrat": 300, "Serat": 29, "Air": 2150},
        2: {"Kelompok Umur": "19 - 29 tahun", "Berat Badan": 55, "Tinggi Badan": 159, "Energi": 2250, "Protein": 60, "Lemak": 65, "Karbohidrat": 360, "Serat": 32, "Air": 2350},
        3: {"Kelompok Umur": "30 - 49 tahun", "Berat Badan": 56, "Tinggi Badan": 158, "Energi": 2150, "Protein": 60, "Lemak": 60, "Karbohidrat": 340, "Serat": 30, "Air": 2350},
    }
    
    trimester_additions = {
        1: {"Trimester": "Trimester 1", "Energi": 180, "Protein": 1, "Lemak": 2.3, "Karbohidrat": 25, "Serat": 3, "Air": 300},
        2: {"Trimester": "Trimester 2", "Energi": 300, "Protein": 10, "Lemak": 2.3, "Karbohidrat": 40, "Serat": 4, "Air": 300},
        3: {"Trimester": "Trimester 3", "Energi": 300, "Protein": 30, "Lemak": 2.3, "Karbohidrat": 40, "Serat": 4, "Air": 300},
    }
    
    standard_nutrition = nutritional_standards[age_group]
    additional_nutrition = trimester_additions[trimester]
    
    total_nutrition = {key: standard_nutrition[key] + additional_nutrition[key] for key in standard_nutrition if key in additional_nutrition}
    
    return standard_nutrition["Kelompok Umur"], additional_nutrition["Trimester"], total_nutrition

def input_user_data():
    print("Pilih kelompok umur:")
    print("1. 16 - 18 Tahun")
    print("2. 19 - 29 tahun")
    print("3. 30 - 49 tahun")
    
    age_group = int(input("Masukkan nomor yang sesuai dengan kelompok umur: "))
    
    print("Pilih trimester kehamilan:")
    print("1. Trimester 1")
    print("2. Trimester 2")
    print("3. Trimester 3")
    
    trimester = int(input("Masukkan nomor yang sesuai dengan trimester kehamilan: "))
    
    return age_group, trimester

def add_food():
    from database import get_nutritional_info

    foods = []
    while True:
        food_name = input("\nMasukkan nama makanan (atau ketik 'selesai' untuk mengakhiri): ").strip().capitalize()
        if food_name.lower() == 'selesai':
            break
        nutrition_info = get_nutritional_info(food_name)
        if nutrition_info:
            nutrition_info = list(nutrition_info)  # Ubah tuple menjadi list agar dapat diubah
            nutrition_info[2] = float(nutrition_info[2])  # Water(g)
            nutrition_info[3] = float(nutrition_info[3])  # Energy(g)
            nutrition_info[4] = float(nutrition_info[4])  # Protein(g)
            nutrition_info[5] = float(nutrition_info[5])  # Fat(g)
            nutrition_info[6] = float(nutrition_info[6])  # Carbohydrate(mg)
            nutrition_info[7] = float(nutrition_info[7])  # Fiber(mg)
            
            foods.append(nutrition_info)
            print(f"\nNilai gizi untuk {food_name} ditambahkan.")
        else:
            print(f"Makanan '{food_name}' tidak ditemukan di database.")
    
    return foods
