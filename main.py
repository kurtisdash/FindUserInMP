import time
from config import API_KEY
from api import fetch_match_data
from utils import get_player_input, check_player_in_match

def make_api_request():
    OSU_DEFAULT_MP_URL = 'https://osu.ppy.sh/community/matches/'
    api_url = "https://osu.ppy.sh/api/get_match"

    mp, player_id = get_player_input()

    print(f"\nChecking the last 100 MPs from {OSU_DEFAULT_MP_URL}{mp} to {OSU_DEFAULT_MP_URL}{mp-100}."
          f"\nPlease be patient. Checking all 100 previous matches takes about 3 and a half minutes."
          f"\nIf the player is found before that, the process will stop early.")

    for _ in range(100):
        players = set()  # clear the set after each match
        match_data = fetch_match_data(api_url, mp, API_KEY)

        if match_data:
            for game in match_data.get('games', []):
                for item in game.get('scores', []):
                    players.add(item.get('user_id'))  # add user id of each player to set

            if check_player_in_match(players, player_id):
                print(f"\nPlayer found in match {OSU_DEFAULT_MP_URL}{mp}")
                return

        mp -= 1  
        time.sleep(2)  # prevent rate limiting

    print('\nPlayer not found in the last 100 matches.')

    repeat = input('Would you like to try the next 100 matches? (y/n): ')
    if repeat.lower() == 'y':
        make_api_request()  # Restart the process for the next 100 matches

if __name__ == "__main__":
    make_api_request()
