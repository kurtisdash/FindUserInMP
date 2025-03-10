import time
from config import API_KEY
from api import fetch_match_data
from utils import get_player_input, check_player_in_match

OSU_DEFAULT_MP_URL = 'https://osu.ppy.sh/community/matches/'
api_url = "https://osu.ppy.sh/api/get_match"
mp, player_id = get_player_input()

def make_api_request():
    global mp
    global player_id

    print(f"\nChecking the last 1000 MPs from {OSU_DEFAULT_MP_URL}{mp} to {OSU_DEFAULT_MP_URL}{mp-1000}."
          f"\nPlease be patient. Checking all 1000 previous matches takes around 22 minutes."
          f"\nIf the player is found before that, the process will stop early.")

    for _ in range(1000):
        players = set()  # Clear the set after each match
        match_data = fetch_match_data(api_url, mp, API_KEY)

        if match_data:
            for game in match_data.get('games', []):
                for item in game.get('scores', []):
                    players.add(item.get('user_id'))  # Add user id of each player to set

            if check_player_in_match(players, player_id):
                print(f"\nPlayer found in match {OSU_DEFAULT_MP_URL}{mp}")
                return

        mp -= 1  
        time.sleep(1.3)  # Prevent rate limiting

    print(f'\nPlayer not found in the last 1000 matches. Last MP link checked: {OSU_DEFAULT_MP_URL}{mp}')

    repeat = input('Would you like to try the next 1000? (y/n): ')
    if repeat.lower() == 'y':
        make_api_request()  

if __name__ == "__main__":
    make_api_request()
