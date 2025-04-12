import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for i in range(min(8, len(books))):

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        star_rating_tag = book.find("p", class_="star-rating")
        rating = star_rating_tag["class"][1]



        print(f"Назва: {title}")
        print(f"Ціна: {price}")
        print(f"Рейтинг: {rating} зірки")
        print("-" * 30)

else:
    print(f"Помилка: Не вдалося отримати сторінку. Код статусу: {response.status_code}")
