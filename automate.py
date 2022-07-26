import os
import pyautogui
import time
from playsound import playsound
import datetime
import pyttsx3
voice_assistant = pyttsx3.init()
voice_assistant.setProperty("rate", 125)
list_of_time_questions = ["What time is it?", "Show me the time", "Time", "What is the current time?",
                          "What time is it?", "show me the time", "time", "what is the current time?"]


class AutomateStuff:
    def play_music(self):
        music_folder = r"D:\Music"
        music_folder = os.path.realpath(music_folder)

        with os.scandir(music_folder) as folders_names:
            for folders in folders_names:
                if folders.is_dir():
                    print(folders.name)

        ask_folder = input("Which folder do you wish to select?\n")
        x_music_folder = music_folder + "/" + ask_folder
        # The previous variable contain the full path of the folder selected by the user.
        os.startfile(x_music_folder)

        for new_music_temp_folder in os.listdir(x_music_folder):
            if os.path.isfile(os.path.join(x_music_folder, new_music_temp_folder)):
                print(new_music_temp_folder)

        play_all_songs = ["all", "All", "ALL", "play the whole list", "play all the songs", "the entire folder"]
        ask_what_music_play = input("Which song do you want to play?\n")

        if ask_what_music_play in play_all_songs:
            pyautogui.click(277, 1045, duration=2)
            with pyautogui.hold(["ctrl"]):
                pyautogui.press(["a", "enter"])
        elif ask_what_music_play not in play_all_songs:
            playsound(x_music_folder + "/" + ask_what_music_play)
        # The elif statement is suppose to open just one song, the problem is that it does not
        # play audios that are too long, i don´t know exactly the max length possible.

# -----------------------------------------------------------------------------------------------------------------

    def gmail_automate(self):
        while True:
            try:
                voice_assistant.say("How many emails do you want to mark as read?")
                voice_assistant.runAndWait()
                emails_to_read = input("")
                how_many_emails_read = int(emails_to_read)
            except ValueError:
                print("You have not write an number, please try again!!!\n")
            else:
                print("Executing!!!")
                break

        time.sleep(4)
        max_gmail_read_length = 15
        pyautogui.click(1744, 318, 1)

        if how_many_emails_read < max_gmail_read_length:
            for i in range(how_many_emails_read):
                pyautogui.move(0, 50)
                pyautogui.click()
            print("Done it!!!")

        elif how_many_emails_read >= max_gmail_read_length:
            for i in range(14):
                pyautogui.move(0, 50)
                pyautogui.click()

            while True:
                pyautogui.scroll(-700)
                pyautogui.moveTo(1748, 289, 0.5)
                voice_assistant.say("How many emails are left to mark as read?")
                voice_assistant.runAndWait()
                emails_left_read = int(input(""))
                print("Executing!!!")
                time.sleep(7)

                for i in range(emails_left_read):
                    pyautogui.click()
                    pyautogui.move(0, 50)

                voice_assistant.say("Want to mark more emails as read?")
                voice_assistant.runAndWait()
                ask_continuing_reading_emails = input("")
                if ask_continuing_reading_emails == "yes" or ask_continuing_reading_emails == "y":
                    time.sleep(7)
                    pass
                elif ask_continuing_reading_emails == "no" or ask_continuing_reading_emails == "n":
                    break
        voice_assistant.say("Done it!!!")
        voice_assistant.runAndWait()

# -----------------------------------------------------------------------------------------------------------------

    def open_games(self):
        voice_assistant.say("Which game do you want to open?")
        voice_assistant.runAndWait()
        ask_which_game_to_open = input("")
        pyautogui.press("win")
        time.sleep(1)

        for i in range(len(ask_which_game_to_open)):
            pyautogui.press(ask_which_game_to_open[i])

        time.sleep(1)
        pyautogui.press("enter")

# -----------------------------------------------------------------------------------------------------------------

    def change_wallpaper(self):
        pyautogui.click(1919, 1052, duration=1)
        pyautogui.rightClick(x=960, y=540, duration=1)
        pyautogui.move(100, 385, duration=1)
        pyautogui.click()
        pyautogui.click(480, 686, duration=2)

# -----------------------------------------------------------------------------------------------------------------

    def play_youtube(self):
        say_something_to_print = input("What do you want to search on youtube?\n")
        time.sleep(1)
        pyautogui.moveTo(458, 1057, 2)
        time.sleep(1)
        pyautogui.move(0, -100, 1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey("ctrl", "shift", "N")
        pyautogui.click(309, 101, 2)
        time.sleep(5)
        pyautogui.click(688, 121, 1)

        for i in range(len(say_something_to_print)):
            pyautogui.press(say_something_to_print[i])

        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.click(977, 253, 1)
        voice_assistant.say("Enjoy!!!")
        voice_assistant.runAndWait()


# -----------------------------------------------------------------------------------------------------------------


class MySchedule:
    # This function waits exactly one hour, so as you can see i cannot run something else in the meantime,
    # so i think on implementing a multithreading process in the future.
    def brush_teeth_time(self):
        start_counting = input("Start counting\n")
        if start_counting:
            get_exact_hour = datetime.datetime.now().strftime("%H")
            get_exact_minutes = datetime.datetime.now().strftime("%M")
            next_exact_hour = int(get_exact_hour) + 1
            while True:
                brush_time = str(next_exact_hour) + ":" + get_exact_minutes
                if datetime.datetime.now().strftime("%H:%M") == brush_time:
                    voice_assistant.say("It´s time for you to brush your teeth.")
                    voice_assistant.runAndWait()
                    break

# -----------------------------------------------------------------------------------------------------------------

    def get_current_date(self):
        current_day = datetime.datetime.now()
        date_to_say = "today is " + str(current_day.strftime("%B ")) + str(current_day.day) \
                      + " of " + str(current_day.year)
        voice_assistant.say(date_to_say)
        voice_assistant.runAndWait()

# -----------------------------------------------------------------------------------------------------------------

    def get_current_time(self):
        current_time = datetime.datetime.now()
        time_to_say = "It is " + current_time.strftime("%H") + " hour with " + current_time.strftime("%M") + " minutes "
        voice_assistant.say(time_to_say)
        voice_assistant.runAndWait()

