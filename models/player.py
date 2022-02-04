def unserialized(serialized_player):
    surname = serialized_player["Nom"]
    forename = serialized_player["Prenom"]
    date_of_birth = serialized_player["Date de naissance"]
    gender = serialized_player["Sexe"]
    ranking = serialized_player["Classement"]
    tournament_score = serialized_player["Score"]
    player_id = serialized_player["Id du joueur"]
    return Player(surname,
                  forename,
                  date_of_birth,
                  gender,
                  ranking,
                  tournament_score,
                  player_id
                  )


class Player:

    def __init__(self, surname=None,
                 forename=None,
                 date_of_birth=None,
                 gender=None,
                 ranking=None,
                 tournament_score=0,
                 player_id=0
                 ):
        self.surname = surname
        self.forename = forename
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.tournament_score = tournament_score
        self.player_id = player_id

    def serialized(self):
        player_infos = {'Nom': self.surname, 'Prénom': self.forename, 'Date de naissance': self.date_of_birth,
                        'Sexe': self.gender, 'Classement': self.ranking, 'Score': self.tournament_score,
                        'Id du joueur': self.player_id}
        return player_infos

    def __str__(self):
        return f"{self.surname} {self.forename}"

    def __repr__(self):
        return f"{self.surname} {self.forename}, classement : {self.ranking}"
