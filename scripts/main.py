import time

from detection.at_bat_detector import (
    AtBatDetector,
    get_current_batter,
    get_on_deck_batter
)

from mlb.api import get_schedule
from mlb.parser import (
    get_game_details,
    filter_games_by_teams,
    is_game_live,
    get_live_game_data
)

from notifications.discord import DiscordNotifier

from webhook import WEBHOOK
from config import TRACKED_PLAYERS


def run_tracker():
    detector = AtBatDetector(TRACKED_PLAYERS)

    notifier = DiscordNotifier(WEBHOOK)

    # extract unique teams
    tracked_teams = {
        player["team"]
        for player in TRACKED_PLAYERS
    }

    print("Starting multi-player tracker...")

    while True:
        try:
            # Get today's schedule
            schedule = get_schedule()

            # Parse games
            games = get_game_details(schedule)

            # Filter games involving tracked teams
            filtered_games = filter_games_by_teams(
                games,
                tracked_teams
            )

            # Process live games
            for game in filtered_games:

                if not is_game_live(game):
                    continue

                game_pk = game["gamePK"]

                # Get live data
                live_data = get_live_game_data(game_pk)

                # Get current batter
                batter = get_current_batter(live_data)
                on_deck = get_on_deck_batter(live_data)

                if batter is not None:
                    player = detector.process(game_pk, batter)
                    if player:
                        notifier.send(f"🔥 {player['name']} is now batting!")

                if on_deck is not None:
                    player = detector.process_on_deck(game_pk, on_deck)
                    if player:
                        notifier.send(f"👀 {player['name']} is on deck!")

        except Exception as e:
            print(f"Error occurred: {e}")

        time.sleep(5)


if __name__ == "__main__":
    run_tracker()
