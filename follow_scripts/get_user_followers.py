import itertools
from selenium import webdriver
from util.login import *
import csv


def get_user_followers(browser, url, amount, user):
    sleepy_time = 3
    followers = []

    browser.get(url)
    time.sleep(sleepy_time)

    followers_button = browser.find_element_by_xpath("//a[contains(@href,'/followers')]")
    followers_button.click()
    time.sleep(sleepy_time)

    followers_list = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
    followers_list.click()
    time.sleep(sleepy_time)

    follower_css_selector = "ul div li:nth-child({}) a.notranslate"

    for group in itertools.count(start=1, step=12):
        if group > amount:
            break

        time.sleep(sleepy_time)

        for follower_index in range(group, group + 12):
            follower = browser.find_element_by_css_selector(follower_css_selector.format(follower_index)).text
            followers.append(follower)

        last_follower = browser.find_element_by_css_selector(follower_css_selector.format(follower_index))
        browser.execute_script("arguments[0].scrollIntoView();", last_follower)

    print(len(followers), ": ", followers)

    # write rows of 20 followers
    start = 0
    end = 20

    with open(f'../csv_files/{user}_followers.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        while start <= len(followers):
            writer.writerow(followers[start:end])
            start += 20
            end += 20
    print(f"Created '{user}_followers.csv' and stored {len(followers)} of {user}'s followers...")
    return followers


def main():
    browser = webdriver.Chrome()
    login(browser)

    # user = input("Select a user, who's followers you'd like to follow: ")
    # amount = input(f"How many followers would you like to get from {user}? ")
    user = "yogapractice"
    amount = 5000

    print(f"Heading to {user}'s page...")

    followers = get_user_followers(browser, f"https://www.instagram.com/{user}", amount, user)

    print(f"You have collected {len(followers)} of {user}'s followers!")
    print("I'm going to sleep for an hour...")
    time.sleep(3600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
