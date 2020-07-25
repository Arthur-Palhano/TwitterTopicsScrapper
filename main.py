from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.headless = True

def getTopics():
    firefox = webdriver.Firefox(options=options)
    firefox.get("https://twitter.com/explore/tabs/trending")
    time.sleep(10)
    objTopics = firefox.find_elements_by_css_selector(".css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")
    topics = []
    
    for objTopic in objTopics:
        topics.append(objTopic.text)
    
    firefox.close()
    return topics

def eraseDoubledItens(topics):
    data = []
    for topic in topics:
        if topic not in data:
            data.append(topic)
        else:
            pass
    return data

def sntzText(topics):
    data = []
    for topic in topics:
        if "Momento" not in topic and "Tweets" not in topic:
            data.append(topic)
    
    topics = data
    data = []

    for topic in topics:
        try:
            float(topic)
        except ValueError:
            data.append(topic)

    del data[:data.index("·") + 1]
    del data[data.index("Saiba o que está acontecendo no mundo agora"):]

    return data

def getData():
    return sntzText(eraseDoubledItens(getTopics()))

data = getData()

for topic in data:
    print(topic)
    print(".")