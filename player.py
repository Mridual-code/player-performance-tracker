import matplotlib.pyplot as plt

# Player class
class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def total_contribution(self):
        return self.goals + self.assists

# Save players to a text file
def save_players(players):
    try:
        with open("players_data.txt", "w") as f:
            for player in players:
                f.write(f"{player.name},{player.team},{player.goals},{player.assists}\n")
    except:
        print("Error saving player data!")

# Load players from a text file
def load_players():
    players = []
    try:
        with open("players_data.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                name = parts[0]
                team = parts[1]
                goals = int(parts[2])
                assists = int(parts[3])
                players.append(Player(name, team, goals, assists))
    except:
        pass
    return players

# Show report
def show_report(players):
    print("\n--- Player Report ---")
    for player in players:
        print(f"Name: {player.name}, Team: {player.team}, Goals: {player.goals}, Assists: {player.assists}, Total Contribution: {player.total_contribution()}")

# Visualize goals
def visualize_goals(players):
    names = [player.name for player in players]
    goals = [player.goals for player in players]

    plt.bar(names, goals, color='orange')
    plt.xlabel("Players")
    plt.ylabel("Goals Scored")
    plt.title("Goals by Players")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main program
def main():
    players = load_players()

    while True:
        print("\n1. Add Player")
        print("2. Show Report")
        print("3. Show Goals")
        print("4. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter player name: ")
            team = input("Enter team name: ")
            goals = int(input("Enter number of goals: "))
            assists = int(input("Enter number of assists: "))
            players.append(Player(name, team, goals, assists))

        elif choice == '2':
            show_report(players)

        elif choice == '3':
            visualize_goals(players)

        elif choice == '4':
            save_players(players)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
