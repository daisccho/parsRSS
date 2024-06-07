import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Загрузка данных
file_path = 'classified_tenders.csv'
df = pd.read_csv(file_path)

# Предварительный анализ данных
print(df.head())
print(df.info())

# Анализ наиболее активных отраслей
industry_counts = df['classification'].value_counts()
print(industry_counts)

# Визуализация распределения тендеров по отраслям
plt.figure(figsize=(10, 6))
sns.barplot(x=industry_counts.index, y=industry_counts.values)
plt.title('Распределение тендеров по отраслям')
plt.xlabel('Отрасль')
plt.ylabel('Количество тендеров')
plt.show()

# Анализ динамики изменений (по дате)
# Преобразование столбца с датами в формат datetime
df['razm'] = pd.to_datetime(df['razm'], format='%d.%m.%Y')

# Группировка данных по месяцам и классификации
monthly_trends = df.groupby([df['razm'].dt.to_period('M'), 'classification']).size().unstack().fillna(0)
print(monthly_trends)

# Визуализация динамики изменений
monthly_trends.plot(kind='line', figsize=(12, 8))
plt.title('Динамика изменений количества тендеров по отраслям')
plt.xlabel('Месяц')
plt.ylabel('Количество тендеров')
plt.show()

# Прогнозирование будущих возможностей (простое прогнозирование на основе трендов)
future_months = 12
predictions = {}

for column in monthly_trends.columns:
    model = ExponentialSmoothing(monthly_trends[column], trend='add', seasonal=None)  # seasonal=None убирает сезонность
    fit = model.fit()
    pred = fit.forecast(future_months)
    predictions[column] = pred

# Преобразование прогнозов в DataFrame
predictions_df = pd.DataFrame(predictions)
print(predictions_df)

# Визуализация прогнозов
predictions_df.plot(kind='line', figsize=(12, 8))
plt.title('Прогноз количества тендеров по отраслям на ближайшие месяцы')
plt.xlabel('Месяц')
plt.ylabel('Количество тендеров')
plt.show()

# Сохранение результатов
predictions_df.to_csv('predicted_trends.csv', index_label='Месяц')

print(predictions_df)
