HELP = """ 
help - напечатать справку
add - добавить задачу
show - напечатать все задачи
random - добавить случайную задачу"""
tasks = {}
run = True
RANDOM_TASKS = "ffhgffg"
if __name__ == '__main__':
    while run:
        command = input("Введите команду: ")
        if command == "help":
            print(HELP)
        elif command == "show":
            task_date = input("Введите дату: ")
            if task_date in tasks:
                for task in tasks[task_date]:
                    print('- ', task)
            else:
                print("Такой даты нет")
        elif command == "add":
            task_date = input("Введите дату задачи: ")
            task = input("Введите задачу: ")
            if task_date in tasks:
                tasks[task_date].append(task)
            else:
                tasks[task_date] = [task]
            print("Задача добавлена")
        else:
            print("Неизвестная команда")
            # run = False
            break
    print("До свидания")