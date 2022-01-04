from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

ser = Service("C:\Program Files (x86)\chromedriver.exe")
op = webdriver.ChromeOptions()

text = input("Search Google or Type URL: ")

class GoogleBot:

	def __init__(self, text):
		self.s = webdriver.Chrome(service=ser, options=op)
		self.s.get("https://www.google.com/search?q=" + text + "&start")

GoogleBot(text)


