from tkinter import *
import random


def main():

    def drag_start(event):
        '''
        Функция, начинающая перемещение виджета при его нажатии левой кнопкой мыши
        '''

        # Получаем ссылку на виджет, который вызвал событие
        widget = event.widget
        # Сохраняем начальные координаты мыши при нажатии
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(event):
        '''
        Функция, отвечающая за перемещение виджета в процессе его перетаскивания
        '''

        # Получаем ссылку на виджет, который вызвал событие
        widget = event.widget
        # Рассчитываем новые координаты для перемещаемого виджета
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        # Перемещаем виджет на новые координаты
        widget.place(x=x, y=y)
        # Проверяем столкновения после перемещения виджета
        check_collisions(widget)

    def check_collisions(moving_widget):
        '''
        Функция, проверяющая столкновения виджетов между собой
        '''

        # Проверяем столкновения перемещаемого виджета с другими виджетами
        for widget in [label, label2] + additional_labels:
            if widget != moving_widget:
                # Получаем координаты перемещаемого и текущего виджетов
                x1, y1, x2, y2 = moving_widget.winfo_x(), moving_widget.winfo_y(), moving_widget.winfo_x() + moving_widget.winfo_width(), moving_widget.winfo_y() + moving_widget.winfo_height()
                x3, y3, x4, y4 = widget.winfo_x(), widget.winfo_y(), widget.winfo_x() + widget.winfo_width(), widget.winfo_y() + widget.winfo_height()
                # Если виджеты пересекаются, вызываем функцию отталкивания
                if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
                    repel(widget, moving_widget)

    def repel(widget1, widget2):
        '''
        Функция, отталкивающая виджеты друг от друга при столкновени
        '''

        # Плавно отталкиваем виджеты друг от друга
        x1, y1 = widget1.winfo_x(), widget1.winfo_y()
        x2, y2 = widget2.winfo_x(), widget2.winfo_y()
        diff_x = x1 - x2
        diff_y = y1 - y2
        dist = (diff_x ** 2 + diff_y ** 2) ** 0.5
        if dist < 1:
            dist = 1
        move_x = diff_x / dist
        move_y = diff_y / dist
        new_x1 = x1 + move_x
        new_y1 = y1 + move_y
        new_x2 = x2 - move_x
        new_y2 = y2 - move_y
        # Перемещаем виджеты на новые координаты
        widget1.place(x=new_x1, y=new_y1)
        widget2.place(x=new_x2, y=new_y2)

    def generate_square():
        '''
        Функция для генерации нового квадрата
        '''

        # Создаем новый квадрат с случайным цветом и располагаем его на случайной позиции
        new_label = Label(windows, bg=random.choice(colors), width=10, height=5, relief="raised")
        new_label.place(x=random.randint(50, 300), y=random.randint(50, 300))
        # Привязываем обработчики событий для нового квадрата
        new_label.bind("<Button-1>", drag_start)
        new_label.bind("<B1-Motion>", drag_motion)
        # Добавляем новый квадрат в список дополнительных квадратов
        additional_labels.append(new_label)

    # Создание основного окна
    windows = Tk()

    # Определение цветов для квадратов
    colors = ["red", "blue", "green", "yellow", "orange"]

    # Создание и размещение первых двух квадратов
    label = Label(windows, bg="red", width=10, height=5, relief="raised")
    label.place(x=20, y=20)

    label2 = Label(windows, bg="blue", width=10, height=5, relief="raised")
    label2.place(x=120, y=120)

    # Создание пустого списка для хранения дополнительных квадратов
    additional_labels = []

    # Создание кнопки для генерации новых квадратов
    generate_button = Button(windows, text="Generate Square", command=generate_square, bg="#4CAF50", fg="white", relief="raised")
    generate_button.place(x=20, y=250)

    # Привязка функций для перемещения квадратов к событиям мыши
    label.bind("<Button-1>", drag_start)
    label.bind("<B1-Motion>", drag_motion)

    label2.bind("<Button-1>", drag_start)
    label2.bind("<B1-Motion>", drag_motion)

    # Запуск главного цикла обработки событий
    windows.mainloop()


if __name__ == "__main__":
    main()
