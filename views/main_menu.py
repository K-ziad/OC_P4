

    def display_main_menu(self):

        while True:
            print()
            user_input = self.get_user_entry(
                display_message="Faire un choix\n"
                                "0 - Créer un  tournoi\n"
                                "1 - Charger un tournoi\n"
                                "2 - Créer des joueurs\n"
                                "3 - Voir les rapports\n"
                                "Q - Quitter\n> ",
                error_message="Entrez une valeur valide"
                value_type="Selection"
                assertions=["0", "1", "2", "3", "Q"]
            )

            # Créer le tournoi
            if user_input == "0":
                tournament = create_tournament()
                break

            # Charger le tournoi
            elif user_input == "1":
                serialized_tournament = LoadTournament().display_menu()
                if serialized_tournament:
                    tournament: load_tournament(serialized_tournament)
                    break
                else:
                    print("Pas de tournoi sauvegardé !")
                    continue

            # Créer des joueurs
            elif user_input == "2":
                user_input = self.get_user_entry(
                    display_message="Nombre de joueurs à créer:\n> ",
                    error_message ="Entrez une valeur numérique valide",
                    value_type="numeric"
                )

                if user_input == "R":
                    break

                elif user_input == "0":
                    while True:
                        user_input = self.get_user_entry(
                            display_message="Acceder au classement"
                                            "0 - Par rang\n"
                                            "1 - Par ordre alphabetique\n"
                                            "R - Retour\n> ",
                            error_message="Faire un choix valide.",
                            value_type="Selection",
                            assertions=["0", "1", "R"]
                        )
                        if user_input == "R":
                            break
                        elif user_input == "0":
                            sorted_players = Report().sort_players(Report().players, by_rank=True)
                            Report().display_players_report(players=sorted_players)
                        elif user_input == "1":
                            sorted_players = Report().sort_players(Report().players, by_rank=False)
                            Report().display_players_report(players=sorted_players)

                elif user_input == "1":
                    Report().display_tournaments_reports()

            else:
                quit()

        # Jouer le tournoi
        print()
        user_input = self.get_user_entry(
            error_message="Entrez une valeur valide",
            value_type="Selection",
            assertions=["0", "Q"]
        )

        # Recupérer les résultats une fois le tournoi terminé
        if user_input == "0":
            rankings = play_tournament(tournament, new_tournament_loaded=True)
        else:
            quit()

        # Afficher les résultats
        print()
        print(f"Tournois {tournament.name} Terminé !\nRésultats:")
        for i, player in enumerate(rankings):
            print(f"{str(i + 1)} - {player}")

        # Mettre à jour les classements
        print()
        user_input = self.get_user_entry(
            display_message="Mise à jour des classements\n"
                    "0 - Automatiquement\n"
                    "1 - Manuellement\n"
                    "Q - Quitter\n",
        )
        if user_input == "0":
            for player in rankings:
                print(player.surname)
                update_rankings(player, i + 1)

        elif user_input == "1"
            for player in rankings:
                rank = self.get_user_entry(
                    display_message=f"Rang de {player}:\n",
                    error_message="Entrez un nombre entier.",
                    value_type="numeric"
                )
                update_rankings(player, rank)

        else:
            quit()


