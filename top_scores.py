

def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time

    ranking = {rank: 0 for rank in range(highest_possible_score, -1, -1)}
    for score in unsorted_scores:
        ranking[score] += 1
    sorted_scores = []
    for score in ranking:
        for users in range(ranking[score]):
            sorted_scores.append(score)
    return sorted_scores
