from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import random
from util.tags import *
from util.comments import *
from util.login import *

total_likes = 0
total_comments = 0


def visit_tag(browser, url):
    sleepy_time = 5

    global total_likes
    global total_comments

    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")

    print("Picture Length: " + str(len(pictures)))

    if len(pictures) >= 20:

        for picture in pictures[9:]:
            picture.click()
            time.sleep(sleepy_time)

            try:
                heart = browser.find_element_by_class_name("fr66n")
                time.sleep(sleepy_time)
                heart.click()
                total_likes += 1
                print(f"{total_likes} Likes...")
            except:
                time.sleep(sleepy_time)

            time.sleep(sleepy_time)

            try:
                text_box = browser.find_element_by_class_name("Ypffh")
                time.sleep(sleepy_time)
                text_box.click()
                text_box = browser.find_element_by_class_name("Ypffh")
                time.sleep(sleepy_time)
                text_box.send_keys(random.choice(potential_comments))
                time.sleep(sleepy_time)
                text_box.send_keys(Keys.ENTER)
                total_comments += 1
                print(f"{total_comments} Comments...")

                time.sleep(sleepy_time)

            except:
                time.sleep(sleepy_time)

            finally:
                close = browser.find_element_by_css_selector("[aria-label='Close']")
                close.click()

                time.sleep(sleepy_time)


def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = primary_yoga_tags

    start_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("STARTING AT:     ", start_time)

    for tag in tags:
        print(f"You have liked {total_likes} photos so far...")
        print(f"You have left {total_comments} comments so far...")
        print('V I S I T I N G      #' + tag)
        visit_tag(browser, f"https://www.instagram.com/explore/tags/{tag}")

    end_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("STARTED AT:      ", start_time)
    print("ENDING AT:     ", end_time)
    print(f"You have liked {total_likes} photos today...")
    print(f"You have left {total_comments} comments today...")
    print("I'm going to sleep for an hour...")
    time.sleep(3600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
