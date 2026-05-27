import requests
from config import LIVE_DATA_BASE_URL

def get_game_details(data: dict) -> list[dict]:
    info = []

    for date in data["dates"]:
        for game in date["games"]:
            teams = game["teams"]
            home = teams["home"]["team"]["name"]
            away = teams["away"]["team"]["name"]
            gamePK = game["gamePk"]
            status = game["status"]["detailedState"].replace("(", "").replace(")", "")

            info.append({
                "home": home,
                "away": away,
                "gamePK": gamePK,
                "status": status
            })
    
    return info

def filter_games_by_teams(
    games: list[dict],
    team_names: set[str]
) -> list[dict]:

    filtered_games = []

    for game in games:
        if (
            game["home"] in team_names
            or game["away"] in team_names
        ):
            filtered_games.append(game)

    return filtered_games

def is_game_live(game: dict) -> bool:
    return game["status"] == "In Progress"

def get_live_game_data(gamePK: int) -> dict:
    url = f"{LIVE_DATA_BASE_URL}/{gamePK}/feed/live"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()