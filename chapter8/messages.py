def send_messages(messages, sent_messages):
    for message in messages:
        print(f"{message}")
        sent_messages.append(message)


# Use variable number of arguments.

def sandwiches(*items):
    for item in items:
        print(f"Ordering {item} Sandwich")

def user_profile(first, last, **user_info):
    user_info["first"] = first
    user_info["last"] = last
    return user_info

def make_car(manufacutrer, model, **features ):
    features["manufacutrer"] = manufacutrer
    features["model"] = model
    return features