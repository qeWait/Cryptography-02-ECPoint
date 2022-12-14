# Cryptography-02-ECPoint

В тесті використовується наступне еліптичне рівняння кривої: y^2 = x^3 + 3x + 4\
Звірити результат виконання можна з цим онлайн-ресурсом https://www.desmos.com/calculator/3ah3mmpiuk \
Результат виконання в моїй консолі:\
![Result](https://i.imgur.com/NKhPNhg.png)

Скрипт який виконує завдання: `tasks.py`

- [x] `BasePointGGet`
- [x] `ECPointGen` - виконується при ініціалізації класу
- [x] `IsOnCurveCheck`
- [x] `AddECPoints`
- [x] `DoubleECPoints`
- [x] `ScalarMult`
- [x] `ECPointToString`
- [x] `PrintECPoint`

Додатково реалізовані методи та класи:

- [x] `ECurve` - додатковий клас для збереження рівняння еліптичної кривої
- [x] `ValidateECurve`
- [x] `EquationToString`

Запускати скрипт `tasks.py`

Скрипт `tasks.py` виконує всі завдання зазначені в документі

- `BasePointGGet` - метод класу `ECurve`, не приймає аргументів, повертає об'єкт класу `ECPoint` згенерований на основі вхідних даних про еліптичну криву (a та b)
- `IsOnCurveCheck` - метод класу, який повертає `True` або `False`, також приймає один аргумент `curve`, який має бути об'єктом класу `ECurve`, інакше буде викликатись помилка
  - `True` в випадку коли точка належить еліптичній кривій, 
  - `False` в випадку коли точка не належить еліптичній кривій
- `AddECPoints` - метод класу `Ecurve`, який повертає об'єкт класу `ECPoint`. Обчислення виконуєтья згідно до формули з презентації
- `DoubleECPoints` - метод класу `ECPoint`, який повертає подвоєну точку, також приймає один аргумент `curve`, який має бути об'єктом класу `ECurve`, інакше буде викликатись помилка. Обчислення виконуєтья згідно до формули з презентації
- `ScalarMult` - метод класу `ECPoint`, який повертає об'єкт класу `ECPoint` нової точки. Обчислення виконуєтья згідно до формули з презентації, також є перевірка чи ми множимо на натуральне число
- `ECPointToString` - метод класу `ECPoint`, який повертає стрічку `[x, y]`, де 
  - `x` - належить осі абсцис
  - `y` - належить осі ординат
- `PrintECPoint` - метод класу `ECPoint`, який нічого не повертає, викликає функцію print() для виведення результату методу ECPointToString() класу `ECPoint`
- `ValidateECurve` - перевірити чи передані правильні дані для створення рівняння еліптичної кривої. (Не існує еліптичної кривої в випадку коли a = b = 0)
- `EquationToString` - метод класу `ECurve`, не приймає аргументів, повертає рівняння еліптичної кривої у вигляді стрічки. Дозволяє переглянути як виглядає рівняння
- `PrintEquation` - метод класу `ECurve`, який нічого не повертає та не приймає аргументи, викликає функцію print() для виведення виконання результату методу `EquationToString` класу `ECurve`

### P.S. Тестові точки для виклику функції та методів прописані одразу в tasks.py
