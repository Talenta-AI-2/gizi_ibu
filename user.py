from database import get_nutritional_info

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
    foods = []
    while True:
        food_name = input("Masukkan nama makanan (atau ketik 'selesai' untuk mengakhiri): ").strip().capitalize()
        if food_name.lower() == 'selesai':
            break
        nutrition_info = get_nutritional_info(food_name)
        if nutrition_info:
            # Convert nutritional values to float
            nutrition_info = (nutrition_info[0], nutrition_info[1], float(nutrition_info[2]), float(nutrition_info[3]), 
                              float(nutrition_info[4]), float(nutrition_info[5]), float(nutrition_info[6]), float(nutrition_info[7]))
            foods.append(nutrition_info)
        else:
            print("Makanan tidak ditemukan di database.")
    return foods
