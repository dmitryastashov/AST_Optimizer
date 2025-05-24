# AST_Optimizer

## Описание проекта

**AST_Optimizer** — open-source инструмент для оптимизации производственного планирования. Позволяет автоматически рассчитывать оптимальный план выпуска продукции с учетом ограничений по ресурсам и максимизации прибыли.

---

## Структура проекта

AST_Optimizer/
├── ast_optimizer/ # Исходный код программы
│ ├── init.py
│ └── main.py
├── data/ # Входные и выходные данные (пример)
│ ├── data.csv # Пример входных данных
│ └── result.csv # Выходной файл (игнорируется git)
├── tests/ # Тесты (планируется)
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore

text

---

## Быстрый старт

1. **Клонируйте репозиторий:**
    ```
    git clone https://github.com/dmitryastashov/AST_Optimizer.git
    cd AST_Optimizer
    ```

2. **Создайте и активируйте виртуальное окружение (по желанию):**
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Установите зависимости:**
    ```
    pip install -r requirements.txt
    ```

4. **Положите входные данные в папку `data/` (пример ниже).**

5. **Запустите оптимизацию:**
    ```
    python ast_optimizer/main.py
    ```

---

## Пример входных данных (`data/data.csv`)

product,profit_per_unit,resource1_usage,resource2_usage,min_production,max_production
A,100,2,5,50,200
B,150,4,3,30,150

text

---

## Ожидаемый результат

- В консоли появится оптимальный объем выпуска для каждого продукта, например:
    ```
    A: 200.0 единиц
    B: 50.0 единиц
    ```
- Результат сохранится в файл `data/result.csv`:
    ```
    product,optimal_production
    A,200.0
    B,50.0
    ```

---

## Вклад

- Приветствуются pull requests и предложения по улучшению!
- Описывайте найденные ошибки и идеи в разделе Issues.

---

## Лицензия

Проект распространяется под лицензией MIT. См. файл LICENSE.