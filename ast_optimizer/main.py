import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Загрузка данных
df = pd.read_csv('data.csv')

# Создание задачи оптимизации
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Переменные: объем выпуска каждого продукта
products = df['product']
variables = {prod: LpVariable(name=f"x_{prod}", lowBound=df.loc[i, 'min_production'], upBound=df.loc[i, 'max_production']) 
             for i, prod in enumerate(products)}

# Целевая функция: максимизация прибыли
model += lpSum(variables[prod] * df.loc[i, 'profit_per_unit'] for i, prod in enumerate(products))

# Ограничения по ресурсам
# Пример: суммарное использование ресурса1 <= 1000, ресурса2 <= 800
model += lpSum(variables[prod] * df.loc[i, 'resource1_usage'] for i, prod in enumerate(products)) <= 1000
model += lpSum(variables[prod] * df.loc[i, 'resource2_usage'] for i, prod in enumerate(products)) <= 800

# Решение задачи
model.solve()

# Вывод результата
for prod in products:
    print(f"{prod}: {variables[prod].value()} единиц")

# Сохранение результата в CSV
result = pd.DataFrame({'product': products, 'optimal_production': [variables[prod].value() for prod in products]})
result.to_csv('result.csv', index=False)
