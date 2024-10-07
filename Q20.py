# List of participants' scores, where each sublist contains scores for multiple games
# Format: [Game1, Game2, Game3, ...]
scores = [
    [85, 90, 78],   # Participant 1's scores
    [92, 88, 95],   # Participant 2's scores
    [76, 85, 80],   # Participant 3's scores
    [89, 91, 93]    # Participant 4's scores
]

# List of participant names for reference
participants = ["Participant 1", "Participant 2", "Participant 3", "Participant 4"]

# Function to calculate the average score of each participant
def calculate_average_scores(scores):
    average_scores = []
    for score_list in scores:
        avg = sum(score_list) / len(score_list)
        average_scores.append(avg)
    return average_scores

# Function to find the winner based on the highest average score
def find_winner(participants, average_scores):
    max_avg = max(average_scores)
    winner_index = average_scores.index(max_avg)
    return participants[winner_index], max_avg

# Calculate average scores
average_scores = calculate_average_scores(scores)

# Find the winner
winner, highest_avg = find_winner(participants, average_scores)

# Display average scores and winner
for i, avg in enumerate(average_scores):
    print(f"{participants[i]}: Average score = {avg:.2f}")

print(f"\nThe winner is {winner} with an average score of {highest_avg:.2f}")
