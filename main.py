from player import Player
from game import Game
from jobs import do_job
from endings import check_endings
from save import save_game, load_game
from achievements import (
    unlock_achievement,
    check_achievements,
    register_ending,
    show_achievements
)


game = load_game()

if game is None:
    player = Player("Larry")
    game = Game(player)
    print("Neues Spiel gestartet.")
else:
    player = game.player
    print("Spielstand geladen.")


while True:
    print("\n=== DUM-DUM: GUM-GUM ===")
    print(f"Geld: ${player.money}")
    print(f"Gum-Gum: {player.gum_gum}")
    print(f"Lebende Moai: {game.alive_moai_count()}")
    print(f"Weltkontrolle: {game.world_control}%")
    print(f"Moai-Gebiet: {game.get_region()}")

    print("\nWas möchtest du tun?")
    print("1. Arbeiten")
    print("2. Gum-Gum kaufen")
    print("3. Dum-Dum füttern")
    print("4. Moai zerstören")
    print("5. Speichern")
    print("6. Laden")
    print("7. Achievements")
    print("8. Beenden")

    choice = input("> ")

    if choice == "1":
        print("\nJobs:")
        print("1. Museum putzen (+$3)")
        print("2. Kisten tragen (+$5)")
        print("3. Nachtschicht (+$8)")

        job_choice = input("> ")

        if job_choice == "1":
            if do_job(player, "museum"):
                game.jobs_done += 1

        elif job_choice == "2":
            if do_job(player, "kisten"):
                game.jobs_done += 1

        elif job_choice == "3":
            if do_job(player, "nacht"):
                game.jobs_done += 1
        else:
            print("Ungültiger Job.")

    elif choice == "2":
        price = game.get_gum_price()

        print(f"\nGum-Gum kostet ${price} pro Stück.")
        amount = int(input("Wie viele? "))

        if player.buy_gum_gum(amount, price):
            game.gum_gum_bought += amount

            print(f"{amount} Gum-Gum gekauft.")

            unlock_achievement("first_gum")

            if amount >= 100:
                unlock_achievement("bulk_buyer")

            if player.money == 0:
                unlock_achievement("bad_investment")

            check_achievements(game)
        else:
            print("Nicht genug Geld.")
    
    elif choice == "3":
        if game.feed_moai():
            print("Dum-Dum bekommt Gum-Gum. 🗿")
            unlock_achievement("first_moai")
            check_achievements(game)
        else:
            print("Du hast kein Gum-Gum.")

    elif choice == "4":
        moai_id = int(input("Welchen Moai zerstören? "))

        if game.destroy_moai(moai_id):
            game.moai_destroyed += 1

            print(f"Moai #{moai_id} wurde zerstört.")
            
            unlock_achievement("first_destruction")
            check_achievements(game)
        else:
            print("Dieser Moai existiert nicht oder ist bereits zerstört.")

    elif choice == "5":
        game.saves += 1
        save_game(game)
        check_achievements(game)
        print("Spiel gespeichert!")

    elif choice == "6":
        loaded_game = load_game()

        if loaded_game is None:
            print("Kein Spielstand gefunden.")
        else:
            game = loaded_game
            player = game.player
            print("Spielstand geladen!")

    elif choice == "7":
        show_achievements()

    elif choice == "8":
        print("DUM-DUM REMAINS.")
        break

    ending = check_endings(game)

    if ending:
        register_ending(ending)

        print()
        print("=== ENDING ===")
        print(ending)
        break
