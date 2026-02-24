# Lesson Helper - Негізгі файл
def main():
    print("=== Lesson Helper – Мұғалім көмекшісі ===")
    print("1. Математика")
    print("2. Информатика")
    
    choice = input("Пәнді таңдаңыз: ")
    level = int(input("Деңгейді таңдаңыз (1, 2, 3): "))
    
    if choice == '1':
        print("Математика модулі дайындалуда...")
    elif choice == '2':
        print("Информатика модулі дайындалуда...")

if __name__ == "__main__":
    main()
