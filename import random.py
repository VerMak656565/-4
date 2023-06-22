import random

def run_chase_game():
    print("Добро пожаловать в игру 'Догонялки'!")
    print("Цель игры - догнать цель, избегая препятствий.")
    print("Управление: используйте клавиши 'w', 'a', 's', 'd' для перемещения.")
    print("Чтобы выйти из игры, нажмите 'q'.")

    # Установка начальной позиции игрока и цели
    player = [0, 0]
    target = [random.randint(1, 9), random.randint(1, 9)]

    # Создание препятствий
    obstacles = []
    for _ in range(15):
        obstacle = [random.randint(0, 9), random.randint(0, 9)]
        if obstacle != player and obstacle != target:
            obstacles.append(obstacle)

    # Главный игровой цикл
    while True:
        # Вывод игрового поля
        for i in range(10):
            for j in range(10):
                if [i, j] == player:
                    print("P", end=" ")
                elif [i, j] == target:
                    print("T", end=" ")
                elif [i, j] in obstacles:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()

        # Проверка условия победы
        if player == target:
            print("Вы догнали цель! Поздравляю, вы выиграли!")
            break

        # Ввод действия игрока
        action = input("Введите действие (w - вверх, a - влево, s - вниз, d - вправо, q - выход): ")

        # Выход из игры
        if action == "q":
            print("Игра окончена.")
            break

        # Обновление позиции игрока
        new_player = player[:]
        if action == "w":
            new_player[0] -= 1
        elif action == "a":
            new_player[1] -= 1
        elif action == "s":
            new_player[0] += 1
        elif action == "d":
            new_player[1] += 1

        # Проверка границ для игрока
        if 0 <= new_player[0] < 10 and 0 <= new_player[1] < 10:
            # Проверка наличия препятствий
            if new_player not in obstacles:
                player = new_player

        # Перемещение цели
        target[0] += random.randint(-1, 1)
        target[1] += random.randint(-1, 1)

        # Проверка границ для цели
        if target[0] < 0:
            target[0] = 0
        elif target[0] > 9:
            target[0] = 9
        if target[1] < 0:
            target[1] = 0
        elif target[1] > 9:
            target[1] = 9

run_chase_game()
