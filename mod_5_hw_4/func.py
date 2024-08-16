# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)      
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User not found."
        except IndexError:
            return "Enter user name."
    return inner


# Функція розділення: команда, значення
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція для додавання нового контакта
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для заміни номера за вказаним ім'ям вже існуючого контакта
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts.update({name: phone})
    return "Contact changed."

# Функція для виводу номера за вказаним ім'ям
@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"

# Функція для виводу всіх записаних контактів
@input_error
def show_all(contacts):
    if len(contacts) > 0:
        result = []
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    else:
        return "List is empty."

