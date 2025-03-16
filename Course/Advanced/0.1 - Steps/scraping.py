import requests, time
from bs4 import BeautifulSoup


URL = "https://docs.python.org/3/"  # link itself
print("Wait 3 seconds")
time.sleep(3)  # wait 3s

response = requests.get(URL)  # link
soup = BeautifulSoup(response.content, "html.parser")  # response parser
page_text = soup.get_text()  # raw text


words = page_text.split()
wrls = []
for word in words:
    if word.lower() == "python":
        wrls.append(word)

print(f"Woord python komt {len(wrls)} aantal keer voor ")

# print(soup.find_all('p')) # element
# print(soup.find_all(class_='linkdescr')) # class
