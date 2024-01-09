class Media:
    def __init__(self, title, year, rating, episodes, completedEps, genres) -> None:
        self.title = title
        self.year = year
        self.rating = rating
        self.episodes = episodes
        self.completedEps = completedEps
        self.genres = genres

class User:
    def __init__(self, username, email, dateCreated) -> None:
        self.email = email
        self.username = username
        self.dateCreated = dateCreated
        