import pandas as pd
import numpy as np

np.random.seed(42)
n_control = 5000
n_treatment = 5000

control_converted = np.random.binomial(1, 0.10, n_control)
treatment_converted = np.random.binomial(1, 0.12, n_treatment)

df_control = pd.DataFrame({
    'group': ['control'] * n_control,
    'converted': control_converted,
    'user_id': range(n_control)
})

df_treatment = pd.DataFrame({
    'group': ['treatment'] * n_treatment,
    'converted': treatment_converted,
    'user_id': range(n_control, n_control + n_treatment)
})

df = pd.concat([df_control, df_treatment], ignore_index=True)
df['pre_test_score'] = np.random.normal(50, 10, len(df))
df['time_on_site'] = np.random.exponential(5, len(df))

df.to_csv('data/ab_test_data.csv', index=False)

print(f"Generated {len(df)} rows of A/B test data")
print(f"Control conversion rate: {df[df['group']=='control']['converted'].mean():.2%}")
print(f"Treatment conversion rate: {df[df['group']=='treatment']['converted'].mean():.2%}")
