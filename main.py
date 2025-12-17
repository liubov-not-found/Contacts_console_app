CONTACTS_FILE = "contacts.txt"


def show_menu():
    print("\nПожалуйста, выберите действие:")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Просмотреть контакты")
    print("6. Выйти")


def load_contacts():
    contacts = []
    try:
        f = open(CONTACTS_FILE, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if line != "":
                contacts.append(line)
        f.close()
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts):
    f = open(CONTACTS_FILE, "w", encoding="utf-8")
    for contact in contacts:
        f.write(contact + "\n")
    f.close()


def input_not_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("❌ Пустая строка. Попробуйте снова.")
        else:
            return value


def input_phone():
    while True:
        phone = input("Введите телефон (12 цифр, например 380991234567): ").strip()
        if phone == "":
            print("❌ Пустая строка. Попробуйте снова.")
            continue
        if not phone.isdigit():
            print("❌ Телефон должен содержать только цифры.")
            continue
        if len(phone) != 12:
            print("❌ Телефон должен быть ровно 12 цифр.")
            continue
        return phone


def input_email():
    while True:
        email = input("Введите email: ").strip()
        if email == "":
            print("❌ Пустая строка. Попробуйте снова.")
            continue
        if "@" not in email or "." not in email:
            print("❌ Email должен содержать символы '@' и '.'.")
            continue
        return email


def add_contact(contacts):
    print("\n➕ Добавление контакта")
    name = input_not_empty("Введите имя: ")
    phone = input_phone()
    email = input_email()

    contact_line = name + "|" + phone + "|" + email
    contacts.append(contact_line)

    save_contacts(contacts)
    print("✅ Контакт успешно добавлен!")


def find_contact(contacts):
    if len(contacts) == 0:
        print("📭 Контактов нет.")
        return

    query = input_not_empty("Введите имя или телефон для поиска: ")

    found = False
    print("\n🔍 Результаты поиска:")

    for contact in contacts:
        parts = contact.split("|")
        if len(parts) != 3:
            continue

        name = parts[0]
        phone = parts[1]
        email = parts[2]

        if query.lower() == name.lower() or query == phone:
            print("—", contact)
            found = True

    if not found:
        print("❌ Контакт не найден.")


def delete_contact(contacts):
    if len(contacts) == 0:
        print("📭 Контактов нет.")
        return

    query = input_not_empty("Введите имя или телефон контакта для удаления: ")

    matches = []
    for i in range(len(contacts)):
        parts = contacts[i].split("|")
        if len(parts) != 3:
            continue
        name = parts[0]
        phone = parts[1]

        if query.lower() == name.lower() or query == phone:
            matches.append(i)

    if len(matches) == 0:
        print("❌ Контакт не найден.")
        return

    print(f"Найдено для удаления: {len(matches)}")
    for idx in matches:
        print("—", contacts[idx])

    confirm = input("Вы уверены? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Удаление отменено.")
        return

    matches.sort(reverse=True)
    for idx in matches:
        contacts.pop(idx)

    save_contacts(contacts)
    print("✅ Контакт удалён!")


def update_contact(contacts):
    if len(contacts) == 0:
        print("📭 Контактов нет.")
        return

    query = input_not_empty("Введите имя или телефон контакта для обновления: ")

    matches = []
    for i in range(len(contacts)):
        parts = contacts[i].split("|")
        if len(parts) != 3:
            continue
        name = parts[0]
        phone = parts[1]

        if query.lower() == name.lower() or query == phone:
            matches.append(i)

    if len(matches) == 0:
        print("❌ Контакт не найден.")
        return

    if len(matches) > 1:
        print("Найдено несколько контактов:")
        for n in range(len(matches)):
            print(f"{n + 1}. {contacts[matches[n]]}")

        choice = input("Введите номер контакта для обновления: ").strip()
        if not choice.isdigit():
            print("❌ Неверный выбор.")
            return

        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(matches):
            print("❌ Неверный выбор.")
            return

        index_to_update = matches[choice_num - 1]
    else:
        index_to_update = matches[0]

    print("\n✏️ Введите новые данные:")
    name = input_not_empty("Введите имя: ")
    phone = input_phone()
    email = input_email()

    contacts[index_to_update] = name + "|" + phone + "|" + email
    save_contacts(contacts)
    print("✅ Контакт обновлён!")


def view_contacts(contacts):
    if len(contacts) == 0:
        print("📭 Контактов пока нет.")
        return

    
    sorted_contacts = sorted(contacts)

    print("\n📒 Все контакты (А-Я):")
    for contact in sorted_contacts:
        print("—", contact)


def main():
    while True:
        contacts = load_contacts()  

        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            find_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            view_contacts(contacts)
        elif choice == "6":
            print("👋 Программа завершена. До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")


main()