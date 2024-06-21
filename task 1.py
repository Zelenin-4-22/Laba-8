import random

def ask_question(player):
    # Список вопросов
    questions = [
        "Какой ваш любимый цвет?",
        "Какую страну вы хотите посетить?",
        "Какое ваше любимый актер?",
        "Какую музыку предпочитаете слушать?",
        "Какой ваш любимый фильм?"
    ]
    # Выбор случайного вопроса из списка
    question = random.choice(questions)
    # Вывод вопроса и ожидание ответа
    print(f"{player}, вопрос: {question}")
    input(f"{player}, ваш ответ: ")

def catch_ball():
    # Вероятность поймать мяч: 70%
    return random.random() < 0.7

def play_turn(current_player, next_player):
    print(f"\n{current_player} бросает мяч {next_player}.")
    if catch_ball():
        print(f"{next_player} поймал мяч!")
        ask_question(next_player)
    else:
        print(f"{next_player} не поймал мяч!")
        ask_question(current_player)

def main():
    # Список игроков
    players = ["Компьютер", "Вы"]
    turn = 0  # Индекс текущего игрока (0 - Компьютер, 1 - Вы)

    while True:
        current_player = players[turn]
        next_player = players[(turn + 1) % 2]
        play_turn(current_player, next_player)
        turn = (turn + 1) % 2  # Переключение хода
        # Спрашиваем, хочет ли игрок продолжить игру
        if input("\nХотите продолжить? (да/нет): ").lower() != "да":
            break

if __name__ == "__main__":
    main()
