# Змейка

Простая игра "Змейка", реализованная на Python с использованием библиотеки tkinter для GUI и PIL для работы с изображениями.

## Описание игры

Игра "Змейка" представляет собой классическую аркадную игру, где игрок управляет змейкой, управляя её направлением с помощью кнопок стрелок. Цель игры - собрать как можно больше пищи, представленной в виде красного овала, увеличивая при этом длину змейки. Игра заканчивается, если змейка сталкивается со стеной или сама с собой.

## Особенности

- Используется tkinter для создания графического интерфейса.
- Игровое поле размером 400x400 пикселей, разделенное на клетки размером 10x10 пикселей.
- Управление змейкой осуществляется с помощью кнопок с изображениями стрелок.
- При съедании пищи змейка увеличивает свою длину, а игрок получает очки.
- Игра заканчивается при столкновении змейки со стеной или самой с собой.

## Управление

Используйте кнопки управления с изображениями стрелок для движения змейки:
- Вверх
- Вниз
- Влево
- Вправо

## Запуск игры

Чтобы запустить игру, выполните скрипт `snake.py`. Убедитесь, что у вас установлены библиотеки PIL (`Pillow`) и tkinter.

```bash
python snake.py
