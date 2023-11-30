from scipy.stats import binomtest


def crit_value(trials, null_prob=0.5, alpha=0.05, alternative='greater'):
    """
    Print table of p values for each possible number of successes

    Input:
        trials: number of trials
        null_prob (default 0.5):
            probability of success for null hypothesis
        alpha (default 0.05): significance level for test
        alternative (default 'greater'):
            must be 'two-sided', 'less' or 'greater'

    Returns: None

    """
    crit_found = False

    print(f"For {trials} trials")
    print("accurate\tp_value")

    for i in range(trials + 1):

        current_pvalue = binomtest(
            k=i,
            n=trials,
            p=null_prob,
            alternative=alternative).pvalue

        print(i, "\t\t", current_pvalue)

        if (alternative == 'greater'
            and crit_found is False
                and current_pvalue < alpha):

            print(f"Critical value: {i}")
            print(f"\tMuriel must accurately identify at least {i} cups\n"
                  f"\tin order to demonstrate significance.")
            crit_found = True
            continue

    return None


if __name__ == "__main__":

    crit_value(
        trials=8,
        # alternative='two-sided'
    )
