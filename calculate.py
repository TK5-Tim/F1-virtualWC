def get_points(player_id, race):
    results = race.groupby('driver_id')['race_position'].mean()
    print(results)