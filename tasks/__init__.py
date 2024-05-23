from widgets import TaskView

from functools import partial
from tasks.lab6_task1 import Lab6Task1
from tasks.lab6_task2 import Lab6Task2


labs = {
    6: [
        partial(Lab6Task1, 1),
        partial(Lab6Task2, 2)
    ]
}

lab_names = {
    6: "Проверка гипотезы о виде закона распределения по критерию согласия Пирсона"
}