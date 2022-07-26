from web_scraping import WebScrapping
from automate import AutomateStuff
from automate import MySchedule
import pyttsx3

voice_assistant = pyttsx3.init()
voice_assistant.setProperty("rate", 125)

run_scraper_function = WebScrapping()
list_for_scraping = ["web scrapping", "scrape", "scraping"]
list_for_wikipedia = ["Wikipedia", "wikipedia", "Wiki", "wiki"]
list_for_amazon = ["Amazon", "amazon"]

run_automate_function = AutomateStuff()
list_for_automates = ["automation", "automate", "open automation", "automate something"]
list_for_music = ["song", "Song", "songs", "music", "play music", "play some song"]
list_for_gmail = ["mark some emails", "gmail", "mark"]
list_for_games = ["open a game", "game", "Game"]
list_for_wallpaper = ["change my wallpaper", "wallpaper", "Wallpaper", "open wallpaper"]
list_for_youtube = ["Youtube", "youtube", "yt", "YT"]

run_schedule_function = MySchedule()
list_for_schedule = ["open schedule", "Schedule", "schedule", "open my schedule"]
list_brush_time = ["brush time", "time to brush", "Brush", "brush"]
list_for_date = ["tell my the date", "Date", "date", "today´s date"]
list_for_time = ["what time is it?", "Time", "time", "tell me the time"]

voice_assistant.say("Which class do you want to execute?")
voice_assistant.runAndWait()
ask_to_start = input("")

if ask_to_start in list_for_scraping:
    voice_assistant.say("Pick a website between wikipedia or amazon")
    voice_assistant.runAndWait()
    ask_which_website = input("")
    if ask_which_website in list_for_wikipedia:
        run_scraper_function.wikipedia_search()
    elif ask_which_website not in list_for_wikipedia and ask_which_website in list_for_amazon:
        run_scraper_function.amazon_search()

elif ask_to_start in list_for_automates:
    voice_assistant.say("which function do you want to automate?")
    voice_assistant.runAndWait()
    ask_which_automation = input("")

    if ask_which_automation in list_for_music:
        run_automate_function.play_music()
    elif ask_which_automation in list_for_gmail:
        run_automate_function.gmail_automate()
    elif ask_which_automation in list_for_games:
        run_automate_function.open_games()
    elif ask_which_automation in list_for_wallpaper:
        run_automate_function.change_wallpaper()
    elif ask_which_automation in list_for_youtube:
        run_automate_function.play_youtube()

elif ask_to_start in list_for_schedule:
    voice_assistant.say("what do you want me to do?")
    voice_assistant.runAndWait()
    ask_what_to_do = input("")

    if ask_what_to_do in list_brush_time:
        run_schedule_function.brush_teeth_time()
    elif ask_what_to_do in list_for_date:
        run_schedule_function.get_current_date()
    elif ask_what_to_do in list_for_time:
        run_schedule_function.get_current_time()
