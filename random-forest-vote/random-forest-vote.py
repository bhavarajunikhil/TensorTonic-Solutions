def random_forest_vote(predictions):
    
    final_list = []
    for sample_votes in zip(*predictions):
        votes = {}
        for label in sample_votes:
            votes[label] = votes.get(label, 0) + 1
        max_votes = max(votes.values())
        winners = [label for label, count in votes.items() if count == max_votes]
        final_list.append(min(winners))
    return final_list
            