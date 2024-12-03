from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
driver.get('https://www.divan.ru/sankt-peterburg/category/divany')

# Ожидание появления элементов с ценами
WebDriverWait(driver, 300).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='ui-LD-ZU KIkOH' and @data-testid='price']"))
)

# Поиск элементов с ценами
prices = driver.find_elements(By.XPATH, "//span[@class='ui-LD-ZU KIkOH' and @data-testid='price']")

# Список для хранения цен
price_list = []

# Извлечение и очистка текста цен
for price in prices:
    raw_price = price.get_attribute('textContent')  # Извлечение содержимого через textContent
    cleaned_price = raw_price.replace("руб.", "").replace(" ", "").strip()  # Удаление "руб." и пробелов
    if cleaned_price.isdigit():  # Проверка, что это число
        price_list.append(int(cleaned_price))  # Преобразование в целое число

# Запись цен в CSV
with open('task_3.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Price'])  # Заголовок
    for price in price_list:
        writer.writerow([price])  # Запись каждой цены в строку

# Закрытие браузера
driver.quit()

print("Цены сохранены в 'task_3.csv'")

# Чтение и вывод данных из файла CSV
df = pd.read_csv('task_3.csv')
print(df.head())

# Расчет средней цены
average_price = df['Price'].mean()

# Вывод средней цены
print(f"Средняя цена: {average_price:.2f} руб.")

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=10, edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Показать гистограмму
plt.show()
