Скрипт Manual_speed
===================

Скрипт Manual_speed служит для....

Разбор скрипта
--------------

1. Импортируем необходимые библиотеки и определяем их назначение:

  - | **Pioneer_sdk** – библиотека для управления квадрокоптером;
    | Описание библиотеки Pioneer_sdk - https://pioneer-doc.readthedocs.io/ru/master/programming/python/pioneer-sdk-methods.html;

  - | **time** – библиотека для работы со временем;
    | Описание библиотеки time - https://docs.python.org/3/library/time.html.

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import time

2. Выводим строку('start'). Вызываем функцию 'pioneer_mini.arm()' для запуска моторов. Вызываем функцию 'pioneer_mini.takeoff()' для взлёта. Объявляем переменную 't' и присваиваем ей значение возвращаемое функцией time.time(). 

  .. code-block:: python

    from pioneer_sdk import Pioneer
    import time


    if __name__ == '__main__':
        print('start')
        pioneer_mini = Pioneer()
        pioneer_mini.arm()
        pioneer_mini.takeoff()
        t = time.time() # время старта
        while True: # 20 раз в сек отправляем команду полёта
            pioneer_mini.set_manual_speed(vx=0, vy=0, vz=1, yaw_rate=0)
            time.sleep(0.05)
            if time.time() - t > 2: # если прошло больше 2 секунд, выходим из цикла
                break
        time.sleep(4) # 4 секунды ничего не делаем (дрон в этот момент не должен никуда лететь)
        t = time.time() # обновляем время старта
        while True: # 20 раз в сек отправляем команду полёта
            pioneer_mini.set_manual_speed(vx=1, vy=0, vz=0, yaw_rate=0)
            time.sleep(0.05)
            if time.time() - t > 3: # если прошло больше 3 секунд, выходим из цикла
                break
        time.sleep(4) # 4 секунды ничего не делаем
        pioneer_mini.land()