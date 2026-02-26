import random

def generate_task(level):
    if level == 1:  # Жеңіл: Қосу/Азайту
        a, b = random.randint(1, 20), random.randint(1, 20)
        operator = random.choice(['+', '-'])
        question = f"{a} {operator} {b}"
        answer = eval(question)
    elif level == 2:  # Орташа: Көбейту/Бөлу
        a, b = random.randint(2, 15), random.randint(2, 10)
        question = f"{a} * {b}"
        answer = a * b
    else:  # Қиын: Қарапайым теңдеулер
        x = random.randint(1, 10)
        a = random.randint(1, 10)
        b = x * a
        question = f"x * {a} = {b}. x-ті тап"
        answer = x
    return question, answer

def main():
    print("--- Lesson Helper: Мұғалім көмекшісі ---")
    print("Деңгейді таңдаңыз: 1 (Жеңіл), 2 (Орташа), 3 (Қиын)")
    
    try:
        lvl = int(input("Деңгей: "))
        q, correct_ans = generate_task(lvl)
        
        print(f"\nТапсырма: {q}")
        user_ans = int(input("Жауабыңыз: "))
        
        if user_ans == correct_ans:
            print("✅ Дұрыс! Жарайсыз.")
        else:
            print(f"❌ Қате. Дұрыс жауап: {correct_ans}")
    except ValueError:
        print("Өтініш, тек қана сандарды енгізіңіз.")

if __name__ == "__main__":
    main()
