import random
import math


def pause():
    input("\nPress Enter to return to the casino menu...")


def bernoulli_coin_flip():
    print("\n🪙 COIN FLIP TABLE")
    print("The dealer flips one coin...")

    result = random.choice(["Heads", "Tails"])

    print(f"\nResult: {result}")

    probability = 0.5

    print(f"You had a {probability:.0%} chance of getting this result.")

    pause()


def binomial_coin_flips():
    print("\n🪙 MULTI-FLIP COIN GAME")

    flips = int(input("How many coin flips do you want to play? "))

    heads = 0
    tails = 0
    p = 0.5

    print("\nFlipping coins...")

    for i in range(flips):
        result = random.choice(["Heads", "Tails"])

        if result == "Heads":
            heads += 1
        else:
            tails += 1

    probability = math.comb(flips, heads) * (p ** heads) * ((1 - p) ** (flips - heads))

    print("\nFinal Results:")
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Chance of getting exactly {heads} heads in {flips} flips: {probability:.4f}")

    pause()


def hypergeometric_card_draw():
    print("\n🃏 ACE HUNT CARD GAME")
    print("Try to draw aces from a standard 52-card deck.")

    deck = ["Ace"] * 4 + ["Non-Ace"] * 48

    draws = int(input("How many cards do you want to draw? "))

    if draws > 52:
        print("You cannot draw more than 52 cards from one deck.")
        pause()
        return

    drawn_cards = random.sample(deck, draws)

    aces = drawn_cards.count("Ace")
    non_aces = drawn_cards.count("Non-Ace")

    probability = (
        math.comb(4, aces)
        * math.comb(48, draws - aces)
        / math.comb(52, draws)
    )

    print("\nYou drew your cards...")
    print(f"Aces: {aces}")
    print(f"Non-Aces: {non_aces}")

    if aces > 0:
        print("Nice! You found at least one ace.")
    else:
        print("No aces this round.")

    print(f"Chance of drawing exactly {aces} aces in {draws} cards: {probability:.4f}")

    pause()


def poisson_jackpot_simulator():
    print("\n🎰 SLOT MACHINE JACKPOT")
    print("Each spin has a small chance of hitting the jackpot.")

    spins = int(input("How many spins do you want to buy? "))

    jackpot_probability = 0.02
    jackpots = 0
    payout_per_jackpot = 100

    print("\nSpinning the slot machine...")

    for i in range(spins):
        if random.random() < jackpot_probability:
            jackpots += 1

    total_payout = jackpots * payout_per_jackpot
    lam = spins * jackpot_probability

    probability = (math.exp(-lam) * (lam ** jackpots)) / math.factorial(jackpots)

    print("\nSlot Results:")
    print(f"Total spins: {spins}")
    print(f"Jackpots won: {jackpots}")
    print(f"Total payout: ${total_payout}")

    print(f"Chance of getting exactly {jackpots} jackpots: {probability:.4f}")

    pause()


def geometric_first_win():
    print("\n🎲 FIRST WIN CHALLENGE")
    print("Keep playing until you win once.")

    win_probability = float(input("Enter your chance of winning each round, like 0.25: "))

    tries = 0

    print("\nGame started...")

    while True:
        tries += 1

        if random.random() < win_probability:
            print(f"Round {tries}: WIN")
            break
        else:
            print(f"Round {tries}: Lose")

    probability = ((1 - win_probability) ** (tries - 1)) * win_probability

    print(f"\nYou got your first win after {tries} rounds.")
    print(f"Chance of first winning on round {tries}: {probability:.4f}")

    pause()


def negative_binomial_three_wins():
    print("\n🏆 THREE WINS CHALLENGE")
    print("Keep playing until you win 3 times.")

    win_probability = float(input("Enter your chance of winning each round, like 0.25: "))

    wins_needed = 3
    wins = 0
    tries = 0

    print("\nGame started...")

    while wins < wins_needed:
        tries += 1

        if random.random() < win_probability:
            wins += 1
            print(f"Round {tries}: WIN | Total wins: {wins}")
        else:
            print(f"Round {tries}: Lose | Total wins: {wins}")

    probability = (
        math.comb(tries - 1, wins_needed - 1)
        * (win_probability ** wins_needed)
        * ((1 - win_probability) ** (tries - wins_needed))
    )

    print(f"\nYou reached 3 wins after {tries} rounds.")
    print(f"Chance of needing exactly {tries} rounds to get 3 wins: {probability:.4f}")

    pause()


def main():
    while True:
        print("\n==============================")
        print("🎲 PROBABILITY CASINO SIMULATOR")
        print("==============================")
        print("1. Coin Flip Table")
        print("2. Multi-Flip Coin Game")
        print("3. Ace Hunt Card Game")
        print("4. Slot Machine Jackpot")
        print("5. First Win Challenge")
        print("6. Three Wins Challenge")
        print("7. Leave Casino")

        choice = input("\nChoose a game from 1 to 7: ")

        if choice == "1":
            bernoulli_coin_flip()
        elif choice == "2":
            binomial_coin_flips()
        elif choice == "3":
            hypergeometric_card_draw()
        elif choice == "4":
            poisson_jackpot_simulator()
        elif choice == "5":
            geometric_first_win()
        elif choice == "6":
            negative_binomial_three_wins()
        elif choice == "7":
            print("\nThanks for playing at the Probability Casino!")
            break
        else:
            print("\nInvalid choice. Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
