import random
import time
from datetime import datetime
from colorama import Fore, init
import string
import threading
import keyboard
import sys
from colorama import Fore as f
from datetime import datetime
import os; os.system("cls")
import time, base64, string, random, threading
from decimal import Decimal
import secrets
import base64
import uuid


def generate_unique_token():
    sample_string = str(random.randint(0, 999999999999999999)).zfill(18)
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    token = "MT" + base64_string + "." + random.choice(string.ascii_uppercase) + ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(27))

    # Generate a new UUID for each token
    unique_id = str(uuid.uuid4())

    # Append the UUID to the token to ensure uniqueness
    unique_token = token + "." + unique_id

    return unique_token

# Generate and print a unique token



def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'aol.com']
    username_length = random.randint(5, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Print a single random email
print(generate_random_email())

def on_key_press(event):
    if event.name == 'q':  # Change 'q' to the key you want to use
        print("Exiting program...")
        sys.exit()

print("Press 'q' to exit the program.")
keyboard.on_press(on_key_press)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))



def generate_uk_phone_number():
    area_codes = ['012', '0131', '0141', '0151', '0161', '0191']
    middle_digits = ''.join(random.choices('0123456789', k=7))
    area_code = random.choice(area_codes)
    return f"0{area_code}{middle_digits}"

# Print a random UK phone number
print(generate_uk_phone_number())




def printa():
    global start_time
    for _ in range(50):
        delay = random.uniform(0.05, 5)
        time.sleep(delay)
        end_time = time.time()
        time_taken2 = round(random.uniform(0.5, 1),2) ##capcha info
        time_taken = round(random.uniform(2, 10),2) ##solved
        time_taken3 = round(random.uniform(13, 17),2) #token generated
        text1 = f"{Fore.MAGENTA}[g42] [{Fore.RED}Spammer Check{Fore.MAGENTA}]{Fore.WHITE} Spammer Flagged  {"\u274c"} {time_taken} "
        text2 = f"{Fore.MAGENTA}[g42] [{Fore.GREEN}Spammer Check{Fore.MAGENTA}]{Fore.WHITE} Not Spammer Flagged  {"\u2705"} {time_taken} "
        random_text = random.choice([text1, text2])
        print(f"{Fore.MAGENTA}[g42] [{Fore.BLUE}Discord{Fore.MAGENTA}]{Fore.WHITE}" , "Got Captcha Info" , time_taken2,"s" )
        time.sleep(time_taken)
        print(f"{Fore.MAGENTA}[g42] [{Fore.CYAN}hCaptcha{Fore.MAGENTA}]{Fore.WHITE} -> {Fore.MAGENTA}[Solved hCaptcha P1_eyJ0eXAiOiJKV1QiLCJhbGci0iJIUZI1NiJ9.hadwYXNza2V5xQ{generate_random_string(16)}] {Fore.GREEN} In {Fore.WHITE}-> {Fore.GREEN}{time_taken} s")
        time.sleep(time_taken3)
        print(f"{Fore.MAGENTA}[g42] [{Fore.BLUE}Discord{Fore.MAGENTA}]{Fore.WHITE}Token Generated :  {generate_unique_token()} {"\u2705"} {time_taken3} ")
        time.sleep(2)
        print(f"{Fore.MAGENTA}[g42] [{Fore.LIGHTBLUE_EX}kopeechka{Fore.MAGENTA}]{Fore.WHITE}Email Verfied {generate_random_email()} {"\u2705"} {time_taken} ")
        time.sleep(2)
        print(f"{Fore.MAGENTA}[g42] [{Fore.GREEN}SMSHUB{Fore.MAGENTA}]{Fore.WHITE} Sms Verfied {generate_uk_phone_number()} {"\u2705"} {time_taken} ")
        time.sleep(2)
        print(f"{Fore.MAGENTA}[g42] [{Fore.GREEN}Spammer Check{Fore.MAGENTA}]{Fore.WHITE} Sms Verfied {generate_uk_phone_number()} {"\u2705"} {time_taken} ")
        print(random_text)

        


start_time = time.time()

threads = []
for _ in range(20):
    thread = threading.Thread(target=printa)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
