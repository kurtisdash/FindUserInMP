def get_player_input():
    mp = int(input("Enter the match ID you want to start at (NUMBER ONLY):\n"))
    player_id = input("\nEnter player ID you want to find (NUMBER ONLY):\n")
    return mp, player_id

def check_player_in_match(players, player_id):
    for player in players:
        if player == player_id:
            return True
    return False
