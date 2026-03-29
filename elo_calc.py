def expected_score(player_rating, opponent_rating):
    return 1 / (1 + 10 ** ((opponent_rating - player_rating) / 400))


def update_elo(player_rating, opponent_rating, actual_score, k_factor=32):
    expected = expected_score(player_rating, opponent_rating)
    new_rating = player_rating + k_factor * (actual_score - expected)
    return round(new_rating, 2), expected


def get_rating(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_result_score(player1_name):
    while True:
        result = input(
            f"\nWhat was the result for {player1_name}? "
            "(type: win / draw / lose): "
        ).strip().lower()

        if result == "win":
            return 1.0, 0.0, "Win"
        elif result == "draw":
            return 0.5, 0.5, "Draw"
        elif result == "lose":
            return 0.0, 1.0, "Loss"
        else:
            print("Invalid input. Please type: win, draw, or lose.")


def main():
    print("=" * 42)
    print("           Elo Rating Calculator")
    print("=" * 42)

    player1 = input("\nEnter first player's name: ").strip()
    while not player1:
        print("Name cannot be empty.")
        player1 = input("Enter first player's name: ").strip()

    player2 = input("Enter second player's name: ").strip()
    while not player2:
        print("Name cannot be empty.")
        player2 = input("Enter second player's name: ").strip()

    rating1 = get_rating(f"\nEnter {player1}'s Elo rating: ")
    rating2 = get_rating(f"Enter {player2}'s Elo rating: ")

    score1, score2, result_text = get_result_score(player1)

    k_factor = 32

    new_rating1, expected1 = update_elo(rating1, rating2, score1, k_factor)
    new_rating2, expected2 = update_elo(rating2, rating1, score2, k_factor)

    change1 = round(new_rating1 - rating1, 2)
    change2 = round(new_rating2 - rating2, 2)

    print("\n" + "=" * 42)
    print("               Match Summary")
    print("=" * 42)
    print(f"Players: {player1} vs {player2}")
    print(f"Result for {player1}: {result_text}")
    print(f"K-factor: {k_factor}")

    print("\nExpected scores:")
    print(f"  {player1}: {expected1:.3f}")
    print(f"  {player2}: {expected2:.3f}")

    print("\nUpdated ratings:")
    print(f"  {player1}: {rating1:.2f} -> {new_rating1:.2f} ({change1:+.2f})")
    print(f"  {player2}: {rating2:.2f} -> {new_rating2:.2f} ({change2:+.2f})")
    print("=" * 42)


if __name__ == "__main__":
    main()