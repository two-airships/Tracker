def get_current_batter(live_data: dict) -> dict:
    try:
        matchup = live_data["liveData"]["plays"]["currentPlay"]["matchup"]["batter"]
        batter_name = matchup["fullName"]
        batter_id = matchup["id"]

        return {
                "id": batter_id,
                "name": batter_name
            }
    except (KeyError, TypeError, AttributeError) as e:
        return None
    
class AtBatDetector:
    def __init__(self, tracked_players: list[dict]):
        # {player_id: player_info}
        self.tracked_players = {
            player["id"]: player
            for player in tracked_players
        }

        # {gamePK: last_batter_id}
        self.last_batter_by_game = {}

    def process(self, game_pk: int, batter: dict):
        current_id = batter["id"]

        # initialize game state
        if game_pk not in self.last_batter_by_game:
            self.last_batter_by_game[game_pk] = current_id
            return None

        previous_id = self.last_batter_by_game[game_pk]

        # no batter change
        if current_id == previous_id:
            return None

        # update state
        self.last_batter_by_game[game_pk] = current_id

        # tracked player detected
        if current_id in self.tracked_players:
            return self.tracked_players[current_id]

        return None