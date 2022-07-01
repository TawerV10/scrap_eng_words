import requests
from bs4 import BeautifulSoup

url = "https://speak.tatar/en/language/20000-most-common-words-in-english/?p="

def get_data():
    words = []
    count = 1
    for i in range(1, 201):
        r = requests.get(url + str(i))
        soup = BeautifulSoup(r.content, 'lxml')

        data_in_table = soup.find(class_='table table-striped').find('tbody').find_all('tr')

        for item in data_in_table:
            words.append(item.find('td').find('a').text)
            print(f"{count}: {item.find('td').find('a').text} - was appended!")
            count += 1

    with open('20000_eng_words.txt', 'w', encoding='utf-8') as file:
        for item in words:
            file.write(f"{item}\n")

def sort_words():
    with open('20000_eng_words.txt', encoding='utf-8') as file:
        words = file.readlines()

    with open('20000_arranged_eng_words.txt', 'w', encoding='utf-8') as file:
        for item in sorted(words):
            file.write(f"{item.strip()}\n")

if __name__ == '__main__':
    get_data()
    sort_words()