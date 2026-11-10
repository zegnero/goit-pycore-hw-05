def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Поверніть им'я та номер телефону"
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Введить им'я"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додадно."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Контакт оновлено."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "Контакт не збережено."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Вас вітає AsistentBot!")
    
    while True:
        user_input = input("Напишіть команду: ")
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input)

        if command in ["exit","close","закрити", "вихід"]:
            print("Гарного дня!")
            break
        elif command == ["hello","привіт"]:
            print("Чим можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()