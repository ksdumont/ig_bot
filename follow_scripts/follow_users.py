from selenium import webdriver
from util.login import *
import csv
from datetime import date


def follow_users(browser, path_to_file):
    sleepy_time = 5
    users_to_follow = []

    file = open(path_to_file)
    reader = csv.reader(file)
    data = list(reader)
    print(len(data), data)

    for line in data[0:1]:  # only processing 20 users at a time per ig limits... 1 row...
        users_to_follow.extend(line)
    print(len(users_to_follow), users_to_follow)
    file.close()

    # write the existing data without {users_to_follow} back to file
    new_data = data[1:]
    print(len(new_data), new_data)

    with open(path_to_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for line in new_data:
            writer.writerow(line)

    # if user is followed, store in list to write them to csv file after...
    users_followed = []
    skipped = []
    already_follow = []

    for user in users_to_follow:
        try:
            browser.get(f"https://www.instagram.com/{user}")
            time.sleep(sleepy_time)
        except:
            print(f"Couldn't get 'https://www.instagram.com/{user}', skipping...")
            skipped.append(user)
            continue

        if "This Account is Private" in browser.page_source:
            print(f"{user} has a private account, skipping...")
            skipped.append(user)
            continue
        try:
            follow_button = browser.find_element_by_css_selector('button')
        except:
            print("Can not locate follow button, skipping...")
            skipped.append(user)
            continue

        if follow_button.text == 'Follow':
            follow_button.click()
            users_followed.append(user)
            time.sleep(sleepy_time)
        else:
            already_follow.append(user)
            print(f"You are already following {user}, or they are following you...")

    print("Skipped: ", len(skipped), skipped)
    print('Already Follow: ', len(already_follow), already_follow)
    print("Followed: ", len(users_followed), users_followed)

    # changed file path when running from master script
    with open(f'./csv_files/followed.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(users_followed)

    print(f"Done. You Followed {len(users_followed)} Users and stored them in 'followed.csv' ")

    return users_followed


def main():
    browser = webdriver.Chrome()
    login(browser)

    follow_users(browser, '../csv_files/yogapractice_followers.csv')

    print("I'm going to sleep for 30 minutes...")
    time.sleep(1800)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
