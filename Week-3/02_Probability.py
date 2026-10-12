

# NAVTTC AI/ML - Week 3
# Probability Practice

# Example 1: Basic probability
favorable_outcomes = 3
total_outcomes = 6

probability = favorable_outcomes / total_outcomes
print("Basic Probability =", probability)

# Example 2: Coin toss
heads = 1
total_sides = 2
print("Probability of Heads =", heads / total_sides)

# Example 3: Joint probability for independent events
probability_a = 0.5
probability_b = 0.5

joint_probability = probability_a * probability_b
print("Joint Probability =", joint_probability)

# Example 4: Conditional probability
# P(A and B) / P(B)
probability_a_and_b = 0.2
probability_b = 0.5

conditional_probability = probability_a_and_b / probability_b
print("Conditional Probability =", conditional_probability)

# Example 5: Marginal probability
# Total probability of A across two cases
p_a_given_b = 0.6
p_b = 0.4
p_a_given_not_b = 0.2
p_not_b = 0.6

marginal_probability = (
    p_a_given_b * p_b
    + p_a_given_not_b * p_not_b
)
print("Marginal Probability =", marginal_probability)

# Example 6: Bayes' theorem
p_disease = 0.01
p_positive_given_disease = 0.90
p_positive_given_no_disease = 0.05

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * (1 - p_disease)
)

p_disease_given_positive = (
    p_positive_given_disease * p_disease / p_positive
)

print("Bayes' Theorem Result =", p_disease_given_positive)

# Example 7: Discrete probability distribution
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6

print("Dice Outcomes =", outcomes)
print("Probabilities =", probabilities)

# Example 8: Continuous uniform distribution
# Probability for a uniform distribution between 0 and 10
a = 0
b = 10
lower = 2
upper = 5

probability_interval = (upper - lower) / (b - a)
print("Uniform Interval Probability =", probability_interval)
