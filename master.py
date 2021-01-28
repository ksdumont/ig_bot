from selenium import webdriver
from util.login import *
from util.tags import *
from follow_scripts.follow_users import follow_users
from follow_scripts.unfollow_users import unfollow_users
from like_comment_scripts.like_by_tags import visit_tag
from datetime import datetime
import random


def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = zeke_tags
    random.shuffle(tags)

    start = 0
    end = 5

    iteration_count = 1

    script_running = True

    users_followed = 0
    unfollowed = 0
    total_likes = 0

    s1 = random.randint(200, 300)
    s2 = random.randint(200, 300)
    s3 = random.randint(200, 300)

    start_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print("STARTING AT:      ", start_time)

    while script_running:
        curr_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print("Iteration: ", iteration_count)
        print(curr_time)

        users_followed += len(follow_users(browser, './csv_files/yogapractice_followers.csv'))

        print(f"sleeping for {s1} seconds...")
        time.sleep(s1)

        for tag in tags[start:end]:
            print("V I S I T I N G       #" + tag)
            total_likes += visit_tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
            print(f"You have liked {total_likes} photos so far...")
            time.sleep(12)

        print(f"sleeping for {s2} seconds...")
        time.sleep(s2)

        unfollowed += len(unfollow_users(browser, './csv_files/followed.csv'))

        start += 5
        end += 5

        if end > len(tags):
            script_running = False

        print(f"sleeping for {s3} seconds...")
        time.sleep(s3)
        iteration_count += 1

    end_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    print("STARTED AT:      ", start_time)
    print("ENDING AT:      ", end_time)
    print(f"You have followed {users_followed} users today...")
    print(f"You have unfollowed {unfollowed} users today...")
    print(f"You have liked {total_likes} photos today...")
    print("- - - - - - - - - - - - - - - - - - - - - - - - -")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

