def calculate_worst_hole_handicap(scores, par):
    worst_hole_score = max(scores)
    worst_hole_index = scores.index(worst_hole_score)
    adjusted_scores = scores[:worst_hole_index] + scores[worst_hole_index + 1:]
    adjusted_total = sum(adjusted_scores)
    return max(0, (adjusted_total - par + 2) // 2)

def calculate_worst_hole_score(raw_scores, par, handicap):
    worst_hole_score = max(raw_scores)
    worst_hole_index = raw_scores.index(worst_hole_score)
    adjusted_scores = raw_scores[:worst_hole_index] + raw_scores[worst_hole_index + 1:]
    adjusted_total = sum(adjusted_scores)
    return adjusted_total - handicap

def main():
    try:
        num_players = int(input("Enter the number of players: "))
        num_holes = int(input("Enter the number of holes: "))
        par_per_hole = [int(input(f"Enter par for hole {i+1}: ")) for i in range(num_holes)]
        
        raw_scores = []
        for i in range(num_players):
            print(f"Enter raw scores for player {i+1}:")
            player_scores = [int(input(f"Hole {j+1}: ")) for j in range(num_holes)]
            raw_scores.append(player_scores)
        
        callaway_scores = []
        for player_scores in raw_scores:
            handicap = calculate_worst_hole_handicap(player_scores, sum(par_per_hole))
            callaway_score = calculate_worst_hole_score(player_scores, sum(par_per_hole), handicap)
            callaway_scores.append(callaway_score)
        
        print("\nCallaway Scores:")
        for i, score in enumerate(callaway_scores):
            print(f"Player {i+1}: {score}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
