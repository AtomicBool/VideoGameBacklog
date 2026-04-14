from structs.VideoGame import VideoGame

def parse_game(text: str) -> VideoGame:
    parts = [x.strip() for x in text.split(",")]
    
    return VideoGame(
        title = parts[0],
        time_spent = float(parts[1]),
        priority = int(parts[2]),
        status = parts[3],
        tags = parts[4:]
    )