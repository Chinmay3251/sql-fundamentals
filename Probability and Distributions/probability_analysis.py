import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import comb

# ==========================================
# 1. BASIC PROBABILITY
# ==========================================

print("========== BASIC PROBABILITY ==========")

# Contingency table
data = pd.DataFrame(
    {
        "Purchased": [30, 20],
        "Not Purchased": [10, 40]
    },
    index=["Male", "Female"]
)

print("\nContingency Table:")
print(data)

total = data.values.sum()

# Event A = Customer purchased
p_A = data["Purchased"].sum() / total

# Event B = Customer is Male
p_B = data.loc["Male"].sum() / total

# A intersection B = Male and Purchased
p_A_intersection_B = data.loc["Male", "Purchased"] / total

# P(A | B) = P(A intersection B) / P(B)
p_A_given_B = p_A_intersection_B / p_B

print("\nP(A) - Probability of Purchase:", p_A)
print("P(B) - Probability of Male:", p_B)
print("P(A ∩ B) - Male and Purchased:", p_A_intersection_B)
print("P(A | B) - Purchase given Male:", p_A_given_B)


# ==========================================
# 2. NORMAL DISTRIBUTION
# ==========================================

print("\n========== NORMAL DISTRIBUTION ==========")

mean = 100
std = 15

x = np.linspace(mean - 4 * std, mean + 4 * std, 1000)

normal_distribution = (
    1 / (std * np.sqrt(2 * np.pi))
) * np.exp(
    -0.5 * ((x - mean) / std) ** 2
)

plt.figure(figsize=(9, 5))
plt.plot(x, normal_distribution)
plt.axvline(mean, linestyle="--", label="Mean")
plt.axvline(mean - std, linestyle="--", label="-1 SD")
plt.axvline(mean + std, linestyle="--", label="+1 SD")
plt.axvline(mean - 2 * std, linestyle=":", label="-2 SD")
plt.axvline(mean + 2 * std, linestyle=":", label="+2 SD")
plt.axvline(mean - 3 * std, linestyle=":", label="-3 SD")
plt.axvline(mean + 3 * std, linestyle=":", label="+3 SD")

plt.title("Normal Distribution - 68-95-99.7 Rule")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.savefig("normal_distribution.png")
plt.show()

print("68% of observations are approximately within ±1 standard deviation.")
print("95% of observations are approximately within ±2 standard deviations.")
print("99.7% of observations are approximately within ±3 standard deviations.")


# ==========================================
# 3. BINOMIAL DISTRIBUTION
# ==========================================

print("\n========== BINOMIAL DISTRIBUTION ==========")

trials = 10
probability_success = 0.5

successes = np.arange(0, trials + 1)

binomial_probabilities = np.array([
    comb(trials, k)
    * (probability_success ** k)
    * ((1 - probability_success) ** (trials - k))
    for k in successes
])

print("Number of trials:", trials)
print("Probability of success:", probability_success)

for success, probability in zip(
    successes,
    binomial_probabilities
):
    print(
        f"Successes = {success}: "
        f"Probability = {probability:.4f}"
    )

plt.figure(figsize=(9, 5))

plt.bar(
    successes,
    binomial_probabilities
)

plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.xticks(successes)

plt.tight_layout()
plt.savefig("binomial_distribution.png")
plt.show()


# ==========================================
# 4. CENTRAL LIMIT THEOREM
# ==========================================

print("\n========== CENTRAL LIMIT THEOREM ==========")

np.random.seed(42)

population = np.random.exponential(
    scale=50,
    size=10000
)

sample_size = 30
number_of_samples = 1000

sample_means = []

for i in range(number_of_samples):
    sample = np.random.choice(
        population,
        size=sample_size,
        replace=True
    )

    sample_means.append(sample.mean())

sample_means = np.array(sample_means)

print("Population mean:", population.mean())
print("Mean of sample means:", sample_means.mean())

plt.figure(figsize=(9, 5))

sns.histplot(
    sample_means,
    bins=30,
    kde=True
)

plt.title("Central Limit Theorem - Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("central_limit_theorem.png")
plt.show()

print("\nThe original population is right-skewed.")
print("After taking many samples, the distribution of sample means")
print("becomes approximately normal.")
print("This demonstrates the Central Limit Theorem.")

print("\n========================================")
print("PROBABILITY AND DISTRIBUTION ANALYSIS COMPLETED")
print("========================================")
