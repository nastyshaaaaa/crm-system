from user_manager import UserManager
from client_manager import ClientManager
from order_manager import OrderManager

def main():
    um = UserManager()
    cm = ClientManager()
    om = OrderManager()

    # ---------- Регистрация ----------
    print("=== Регистрация ===")
    name = input("Имя пользователя: ")
    email = input("Email: ")
    pwd = input("Пароль: ")
    try:
        um.register(name, email, pwd)
        print("Регистрация успешна!\n")
    except Exception as e:
        print("Ошибка:", e, "\n")

    # ---------- Вход ----------
    print("=== Вход ===")
    name = input("Имя пользователя: ")
    pwd = input("Пароль: ")
    user = um.authenticate(name, pwd)
    if not user:
        print("Неверные данные")
        return
    print(f"Добро пожаловать, {user.username}!\n")

    # ---------- Главное меню ----------
    print("=== Главное меню ===")
    print("1. Добавить клиента")
    print("2. Показать всех клиентов")
    print("3. Создать заказ")
    print("4. Показать мои заказы")
    print("5. Выход")

    while True:
        choice = input("\nВыберите действие: ")
        if choice == "1":
            c_name = input("Имя клиента: ")
            c_email = input("Email клиента: ")
            try:
                cm.add_client(user.username, c_name, c_email)
                print("Клиент добавлен.")
            except Exception as e:
                print("Ошибка:", e)
        elif choice == "2":
            clients = cm.get_clients_by_owner(user.username)
            if not clients:
                print("Нет клиентов.")
            else:
                for c in clients:
                    print(f"- {c.name} ({c.email})")
        elif choice == "3":
            client_name = input("Имя клиента (должен существовать): ")
            desc = input("Описание заказа: ")
            try:
                amount = float(input("Сумма: "))
                order = om.create_order(user.username, client_name, desc, amount)
                print(f"Заказ №{order.id} создан.")
            except Exception as e:
                print("Ошибка:", e)
        elif choice == "4":
            orders = om.get_orders_by_owner(user.username)
            if not orders:
                print("Нет заказов.")
            else:
                print("ID | Клиент | Описание | Сумма | Статус")
                for o in orders:
                    print(f"{o.id} | {o.client_name} | {o.description} | {o.amount} | {o.status.value}")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный пункт")

if __name__ == "__main__":
    main()
