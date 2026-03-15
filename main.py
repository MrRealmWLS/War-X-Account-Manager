import os
import requests
from colorama import Fore
from pystyle import Write, Colors, Center
import time

b = Fore.LIGHTBLACK_EX
r = Fore.RESET
g = Fore.LIGHTRED_EX

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

os.system("title War X Account Manager │ Made By Realm X Arbaz")

def log(message):
    """Centralized logging with gradient colors and centered text."""
    Write.Print(Center.XCenter(message)+"\n", Colors.blue_to_purple, interval=0.001)

def login(token):
    data = {}
    try:
        headers = {"Authorization": token}
        user_response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        if user_response.status_code == 200:
            user_data = user_response.json()
            log(f"[INFO] Logged in as {user_data['username']}#{user_data['discriminator']}")
            guilds_response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
            friends_response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
            channels_response = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)

            if guilds_response.status_code == 200:
                data['guildsID'] = [guild['id'] for guild in guilds_response.json()]
            if friends_response.status_code == 200:
                data['friendsID'] = [friend['id'] for friend in friends_response.json()]
            if channels_response.status_code == 200:
                data['channelsID'] = [channel['id'] for channel in channels_response.json()]
        else:
            log(f"[ERROR] Invalid token or unable to authenticate.")
            return None
    except Exception as e:
        log(f"[ERROR] Failed to login: {e}")
        return None
    return data


def leave_guild(session, guild_id, token):
    url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"
    while True:
        response = session.delete(url, headers={"Authorization": token})
        
        # Handle successful request
        if response.status_code in {200, 201, 204}:
            log(f"[STATUS] Left guild: {guild_id}")
            break
        
        # Handle rate limit
        elif response.status_code == 429:
            retry_after = response.json().get("retry_after", 1)
            log(f"[RATE LIMIT] Retrying after {retry_after} seconds...")
            time.sleep(retry_after)
        
        # Handle other errors
        else:
            log(f"[ERROR] Failed to leave guild {guild_id}: {response.status_code} - {response.text}")
            break



def close_dm(session, channel_id, token):
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    response = session.delete(url, headers={"Authorization": token})
    if response.status_code in {200, 201, 204}:
        log(f"[STATUS] Closed DM: {channel_id}")


def delete_friend(session, friend_id, token):
    url = f"https://discord.com/api/v9/users/@me/relationships/{friend_id}"
    response = session.delete(url, headers={"Authorization": token})
    if response.status_code in {200, 201, 204}:
        log(f"[STATUS] Removed friend: {friend_id}")


def menu():
    os.system("title War X Account Manager │ Made By Realm X Arbaz")
    title = """
██╗    ██╗ █████╗ ██████╗     ██╗  ██╗     █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
██║    ██║██╔══██╗██╔══██╗    ╚██╗██╔╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
██║ █╗ ██║███████║██████╔╝     ╚███╔╝     ███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
██║███╗██║██╔══██║██╔══██╗     ██╔██╗     ██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
╚███╔███╔╝██║  ██║██║  ██║    ██╔╝ ██╗    ██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                                                                                                                            
"""
    options = """
╔══════════════════════════╗
║ 1 : Nuke Token           ║
║ 2 : Leave Servers        ║
║ 3 : Close Dms            ║
║ 4 : Delete Friends       ║
╚══════════════════════════╝


"""
    Write.Print(Center.XCenter(title), Colors.purple_to_blue, interval=0.001)
    Write.Print(Center.XCenter(options), Colors.purple_to_blue, interval=0)


def menu_handler():
    with requests.Session() as session:
        clear()
        menu()
        while True:
            choice = Write.Input("[~] Choice: ", Colors.blue_to_purple, interval=0.001)
            token = Write.Input(Center.XCenter("Enter your token:"), Colors.blue_to_purple, interval=0.001)
            data = login(token)
            if not data:
                time.sleep(3)
                clear()
                menu()
                continue
            if choice == '1':
                os.system("title War X Account Manager │ Nuking Account")
                for friend_id in data['friendsID']:
                    delete_friend(session, friend_id, token)
                for guild_id in data['guildsID']:
                    leave_guild(session, guild_id, token)
                for channel_id in data['channelsID']:
                    close_dm(session, channel_id, token)
            elif choice == '2':
                os.system("title War X Account Manager │ Leaving All Guilds")
                for guild_id in data['guildsID']:
                    leave_guild(session, guild_id, token)
            elif choice == '3':
                os.system("title War X Account Manager │ Closing All DMs")
                for channel_id in data['channelsID']:
                    close_dm(session, channel_id, token)
            elif choice == '4':
                os.system("title War X Account Manager │ Deleting All Friends")
                for friend_id in data['friendsID']:
                    delete_friend(session, friend_id, token)
            elif choice.lower() == 'cls':
                os.system("title War X Account Manager │ Clearing Screen")
                pass
            else:
                os.system("title War X Account Manager │ Invalid Choice")
            
            time.sleep(3)
            clear()
            menu()


if __name__ == "__main__":
    menu_handler()
