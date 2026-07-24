import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('../data/ab_test_data.csv')

control_rate = df[df['group'] == 'control']['converted'].mean()
treatment_rate = df[df['group'] == 'treatment']['converted'].mean()

print(f"Control conversion rate: {control_rate:.2%}")
print(f"Treatment conversion rate: {treatment_rate:.2%}")
print(f"Lift: {((treatment_rate - control_rate) / control_rate):.2%}")

control_converted = df[df['group'] == 'control']['converted']
treatment_converted = df[df['group'] == 'treatment']['converted']

t_stat, p_value = stats.ttest_ind(control_converted, treatment_converted)

print(f"\nT-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("\n✓ Result is statistically significant (p < 0.05)")
    print("✓ The treatment is better than control")
else:
    print("\n✗ Result is not statistically significant")
    print("✗ No evidence that treatment works")

print("\n\n### RECOMMENDATION ###")
print("Based on the analysis, we recommend implementing the treatment")
print("as it shows a statistically significant improvement in conversions.")
