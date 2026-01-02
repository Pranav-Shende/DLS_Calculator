from dls import (
    dls_mid_first_innings,
    dls_mid_second_innings,
    dls_pre_first_innings,
    dls_pre_second_innings
)

def show_menu():
    print("\n=== DLS Calculator ===")
    print("1. Pre-1st Innings DLS")
    print("2. Mid-1st Innings DLS")
    print("3. Pre-2nd Innings DLS")
    print("4. Mid-2nd Innings DLS")
    print("5. Exit")


def pre_first_innings():
    fmt = input("Format (odi/t20): ").lower()
    delay = int(input("Delay in minutes: "))

    result = dls_pre_first_innings(fmt, delay)

    print("\n--- DLS Result ---")
    print(f"Match reduced to: {result['new_overs']} overs")


def mid_first_innings():
    fmt = input("Format (odi/t20): ").lower()
    overs_bowled = float(input("Overs bowled: "))
    wickets = int(input("Wickets lost: "))
    delay = int(input("Delay in minutes: "))

    result = dls_mid_first_innings(fmt, overs_bowled, wickets, delay)

    print("\n--- DLS Status ---")
    print(f"Revised total overs: {result['revised_total_overs']}")
    print(f"Overs remaining: {result['overs_remaining']}")


def pre_second_innings():
    fmt = input("Format (odi/t20): ").lower()
    team1_score = int(input("Team 1 final score: "))
    delay = int(input("Delay in minutes before chase: "))

    result = dls_pre_second_innings(fmt, team1_score, delay)

    print("\n--- DLS Target ---")
    print(f"Overs available: {result['new_total_overs']}")
    print(f"Revised target: {result['revised_target']}")
    print(f"Required run rate: {result['required_run_rate']}")


def mid_second_innings():
    fmt = input("Format (odi/t20): ").lower()
    team1_score = int(input("Team 1 final score: "))
    team2_score = int(input("Team 2 current score: "))
    overs_bowled = float(input("Overs bowled: "))
    wickets = int(input("Wickets lost: "))
    delay = int(input("Delay in minutes: "))

    result = dls_mid_second_innings(
        fmt, team1_score, team2_score, overs_bowled, wickets, delay
    )

    print("\n--- DLS Status ---")
    print(f"Revised target: {result['revised_target']}")
    print(f"Par score now: {result['par_score']}")

    if result["runs_needed"] <= 0:
        print(f"Team 2 ahead by {-result['runs_needed']} runs (DLS)")
    else:
        print(f"Runs needed: {result['runs_needed']} off {result['overs_remaining']} overs")
        print(f"Required run rate: {result['required_run_rate']}")


def main():
    while True:
        show_menu()
        choice = input("Choose DLS option (1-5): ").strip()

        if choice == "1":
            pre_first_innings()
        elif choice == "2":
            mid_first_innings()
        elif choice == "3":
            pre_second_innings()
        elif choice == "4":
            mid_second_innings()
        elif choice == "5":
            print("Exiting DLS Calculator.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()




