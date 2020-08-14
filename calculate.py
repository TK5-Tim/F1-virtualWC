def get_points(player_id, race):
    results = race.groupby('driver_id')['race_position']
    times = race.groupby('driver_id')['fastest_round']
    points = []
    pattern = r"(\d):(\d{2})\.(\d{3})"
    for time in times.first():
        print(time)
