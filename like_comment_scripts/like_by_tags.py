from selenium import webdriver
from datetime import datetime
from util.tags import *
from util.login import *


def visit_tag(browser, url):
    sleepy_time = 5
    likes = 0

    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements_by_css_selector("div[class='_9AhH0']")
    time.sleep(sleepy_time)

    print("picture length: " + str(len(pictures)))

    if len(pictures) >= 20:

        for picture in pictures[9:20]:
            picture.click()
            time.sleep(sleepy_time)

            try:
                heart = browser.find_element_by_class_name("fr66n")
                time.sleep(sleepy_time)
                heart.click()
                likes += 1
                print(f"{likes} Likes...")
                time.sleep(sleepy_time)

            except:
                time.sleep(sleepy_time)

            finally:
                close = browser.find_element_by_css_selector("[aria-label='Close']")
                close.click()

                time.sleep(sleepy_time)

    return likes


def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = reversed(primary_yoga_tags)

    start_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("STARTING AT:      ", start_time)

    for tag in tags:
        print(f"You have liked {total_likes} photos so far...")
        print("V I S I T I N G       #" + tag)
        visit_tag(browser, f"https://www.instagram.com/explore/tags/{tag}")

    end_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("STARTED AT:      ", start_time)
    print("ENDING AT:      ", end_time)
    print(f"You have liked {total_likes} photos today...")
    print("I'm going to sleep for an hour...")
    time.sleep(3600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
