def total_salary(path):
    try: 
        total_salary = 0
        num_developers = 0
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try: 
                        salary = int(parts[1])
                        total_salary += salary
                        num_developers += 1
                    except ValueError:
                        print(f"Неправильний формат заробітної плати '{line.strip()}'")
                else: 
                    print(f"Неправильний формат даних '{line.strip()}'")

        if num_developers > 0:
            average_salary = total_salary / num_developers
            return total_salary, average_salary
        else:
            print(f"Немає даних про заробітні плати розробників у файлі.")
            return 0, 0
    except FileNotFoundError:
        print(f"Файл не знайдено.")
        return 0, 0
    
total, average = total_salary("task01/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
