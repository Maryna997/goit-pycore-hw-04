def get_cats_info(path):
    cats_list = []
    try: 
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
                    cats_list.append(cat_info)
                else:
                    print(f"Неправильний формат даних '{line.strip()}'")
    except FileNotFoundError:
        print("Файл не знайдено.")
    return cats_list

cats_info = get_cats_info("task02/cats_file.txt")
print(cats_info)
