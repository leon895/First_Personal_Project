from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3
import os

current_project_dir = os.path.dirname(os.path.realpath(__file__))
path = r"C:\Program Files (x86)\chromedriver.exe"
voice_assistant = pyttsx3.init()
voice_assistant.setProperty("rate", 125)


class WebScrapping:
    # Function that search something on Wikipedia
    def wikipedia_search(self):
        driver = webdriver.Chrome(path)
        driver.get("https://www.wikipedia.org/")
        voice_assistant.say("What do you want to know from wikipedia?")
        voice_assistant.runAndWait()
        ask_what_to_wiki = input("")
        get_wiki_search_bar = driver.find_element(By.ID, "searchInput")
        get_wiki_search_bar.send_keys(ask_what_to_wiki)
        get_wiki_search_bar.send_keys(Keys.RETURN)

        get_wiki_xpath = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/ul[1]/li[1]/a")
        open_wiki_page = driver.find_element(By.LINK_TEXT, get_wiki_xpath.text)
        open_wiki_page.click()

# -----------------------------------------------------------------------------------------------------------------

    def amazon_search(self):
        driver = webdriver.Chrome(path)
        driver.get("https://www.amazon.com/")
        askSomething = input("What do you want to search?\n")
        getSearchBox = driver.find_element(By.ID, "twotabsearchtextbox")
        getSearchBox.send_keys(askSomething)
        getSearchBox.send_keys(Keys.RETURN)

        get_item = driver.find_element(By.CLASS_NAME, "a-size-medium.a-color-base.a-text-normal")
        item_name = get_item.text

        get_item_price = driver.find_element(By.CLASS_NAME, "a-price-whole")
        get_item_second_price = driver.find_element(By.CLASS_NAME, "a-price-fraction")
        total_item_price = get_item_price.text + "." + get_item_second_price.text
        print(total_item_price)

        ask_user_to_see_item = input("Do you want to see the item?,\n")
        answers_list_to_see_item = ["Yes", "yes", "YES", "y", "Y"]
        if ask_user_to_see_item in answers_list_to_see_item:
            get_item_link = driver.find_element(By.LINK_TEXT, item_name)
            get_item_link.click()
        elif ask_user_to_see_item not in answers_list_to_see_item:
            print("Okay!!!")

# -----------------------------------------------------------------------------------------------------------------

    def get_country_weather(self):
        ask_country_weather = input("Select the country?\n")
        new_driver = webdriver.Chrome(path)
        new_driver.get("https://www.google.com/")
        get_search_bar = new_driver.find_element(By.NAME, "q")
        get_search_bar.send_keys(ask_country_weather + " weather")
        get_search_bar.send_keys(Keys.RETURN)
        get_weather_number = new_driver.find_element(By.CLASS_NAME, "wob_t.q8U8x")
        voice_assistant.say("The weather in " + ask_country_weather + " is " +
                            get_weather_number.text + " centigrade.")
        voice_assistant.runAndWait()
        new_driver.quit()


# -----------------------------------------------------------------------------------------------------------------
