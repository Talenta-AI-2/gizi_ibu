from registration import register_user, login_user
from nutrition import calculate_nutritional_needs
from database import create_user_table
from user import input_user_data, add_food

def main():
    # Create the user table if it doesn't exist
    create_user_table()

    # Prompt user to login or register
    print("Welcome! Please choose an option:")
    print("1. Register")
    print("2. Login")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_user()
    elif choice == 2:
        user = None
        while not user:
            user = login_user()
    else:
        print("Invalid choice. Exiting...")
        return
    
    # Add food items
    foods = add_food()

    if not foods:
        print("Tidak ada makanan yang ditambahkan. Program berhenti.")
        return

    total_nutrition = {
        "Air": sum(food[2] for food in foods),
        "Energi": sum(food[3] for food in foods),
        "Protein": sum(food[4] for food in foods),
        "Lemak": sum(food[5] for food in foods),
        "Karbohidrat": sum(food[6] for food in foods),
        "Serat": sum(food[7] for food in foods)
    }

    age_group, trimester = input_user_data()
    age_group_str, trimester_str, needs = calculate_nutritional_needs(age_group, trimester)

    print("\nKebutuhan gizi ibu hamil berdasarkan input:")
    print(f"Kelompok Umur: {age_group_str}")
    print(f"Trimester Kehamilan: {trimester_str}")
    for nutrient, value in needs.items():
        print(f"{nutrient}: {value}")

    print("\nTotal nilai gizi dari makanan yang ditambahkan:")
    for nutrient, value in total_nutrition.items():
        print(f"{nutrient}: {value}")

    # Hitung selisih kekurangan gizi
    selisih_gizi = {
        "Energi": needs["Energi"] - total_nutrition["Energi"],
        "Protein": needs["Protein"] - total_nutrition["Protein"],
        "Lemak": needs["Lemak"] - total_nutrition["Lemak"],
        "Karbohidrat": needs["Karbohidrat"] - total_nutrition["Karbohidrat"],
        "Serat": needs["Serat"] - total_nutrition["Serat"],
        "Air": needs["Air"] - total_nutrition["Air"]
    }

    print("\nSelisih kekurangan gizi berdasarkan makanan yang dimasukkan:")
    for nutrient, value in selisih_gizi.items():
        print(f"{nutrient}: {value}")

if __name__ == "__main__":
    main()
