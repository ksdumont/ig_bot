from selenium import webdriver
from util.login import *
import csv
import os


def unfollow_users(browser, path_to_file):
    sleepy_time = 5
    unfollowed = []
    not_following = []

    with open(path_to_file, newline='') as f:
        reader = csv.reader(f)
        users = list(reader)
        print(len(users), users)

    users_to_unfollow = users[0:1]
    users_to_write_back_to_file = users[1:]
    print(len(users_to_unfollow), users_to_unfollow)
    print(len(users_to_write_back_to_file), users_to_write_back_to_file)

    # grab only 12 users per ig follow limits
    twelve_users_to_unfollow = users_to_unfollow[0][0:12]
    users_left_over = users_to_unfollow[0][12:]
    print(len(twelve_users_to_unfollow), twelve_users_to_unfollow)
    print(len(users_left_over), users_left_over)

    for user in twelve_users_to_unfollow:
        browser.get(f"https://www.instagram.com/{user}")
        time.sleep(sleepy_time)
        try:
            follow_button = browser.find_element_by_css_selector("[aria-label='Following']")
            follow_button.click()
            time.sleep(sleepy_time)
            confirm_button = browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirm_button.click()
            unfollowed.append(user)
        except:
            print(f"You are not following {user}")
            not_following.append(user)
        finally:
            time.sleep(sleepy_time)

    print("Unfollowed: ", len(unfollowed), unfollowed)
    print("Not Following: ", len(not_following), not_following)

    # write users back to file
    if len(users_to_write_back_to_file) > 0 or len(users_left_over) > 0:
        with open(path_to_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            if len(users_left_over) > 0:
                writer.writerow(users_left_over)
            for row in users_to_write_back_to_file:
                if len(row) > 0:
                    writer.writerow(row)
                else:
                    continue
    # delete file
    else:
        os.remove(path_to_file)
        print(f"Deleted {path_to_file} ...")

    print(f"Done. You have unfollowed {len(unfollowed)} users today...")

    return unfollowed


def main():
    browser = webdriver.Chrome()
    login(browser)

    unfollow_users(browser, '../csv_files/followed_01_12_21.csv')

    print("I'm going to sleep for an hour...")
    time.sleep(3600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
