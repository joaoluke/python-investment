def weighted_probability(s, alpha=0.8):
    """
    Calculate the weighted probability based on the given success metrics.

    :param s: A list of success metrics. (s[0] is the most recent event)
    :param alpha: A constant representing the decay factor.
    :return: The weighted probability.
    """
    
    # Calculate weights
    N = len(s)
    w = [alpha * ((1 - alpha) ** i) for i in range(N)]

    weighted_s_sum = sum([w[i] * s[i] for i in range(N)])

    w_sum = sum(w)

    prob_weighted = weighted_s_sum / w_sum

    percentage = prob_weighted * 100


    return percentage