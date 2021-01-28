zeke_tags = []


def tag_checker(tags):
    if len(tags) == len(set(tags)):
        return True
    else:
        return False


print(tag_checker(zeke_tags))
