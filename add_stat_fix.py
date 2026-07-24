import json

with open('notebooks/ab_test_validation.ipynb', 'r') as f:
    notebook = json.load(f)

new_cells = [
 {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Step 4: Critical Issue #1 - Statistical Method\n",
    "\n",
    "### The Problem\n",
    "The AI used a t-test for a binary outcome (converted = 0 or 1).\n",
    "\n",
    "**Why this is wrong:**\n",
    "- T-test assumes normally distributed data\n",
    "- Binary data is not normally distributed\n",
    "- For proportions, we should use a proportion test (z-test or chi-square)\n",
    "\n",
    "**Severity:** MEDIUM - The conclusion may still be valid howeevr methodology is technically incorrect."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "control_successes = df[df['group'] == 'control']['converted'].sum()\n",
    "treatment_successes = df[df['group'] == 'treatment']['converted'].sum()\n",
    "control_n = len(df[df['group'] == 'control'])\n",
    "treatment_n = len(df[df['group'] == 'treatment'])\n",
    "\n",
    "print(\"=== CORRECT STATISTICAL TEST: PROPORTION Z-TEST ===\")\n",
    "print(f\"Control: {control_successes} conversions out of {control_n}\")\n",
    "print(f\"Treatment: {treatment_successes} conversions out of {treatment_n}\")\n",
    "\n",
    "count = np.array([control_successes, treatment_successes])\n",
    "nobs = np.array([control_n, treatment_n])\n",
    "z_stat, p_value_correct = proportions_ztest(count, nobs, alternative='two-sided')\n",
    "\n",
    "print(f\"\\nZ-statistic: {z_stat:.4f}\")\n",
    "print(f\"P-value (proportion test): {p_value_correct:.4f}\")\n",
    "print(f\"\\nAI's t-test p-value: {p_value:.4f}\")\n",
    "print(f\"Difference: {abs(p_value - p_value_correct):.4f}\")\n",
    "\n",
    "if p_value_correct < 0.05:\n",
    "    print(\"\\n✓ Correct test also shows significance\")\n",
    "    print(\"  → AI's conclusion was right but method was wrong\")\n",
    "else:\n",
    "    print(\"\\n⚠ AI's conclusion may be wrong\")\n",
    "    print(\"  → This is dangerous because incorrect method could lead to false positives\")"
   ]
  }
]

notebook['cells'].extend(new_cells)

with open('notebooks/ab_test_validation.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Statistical fix added")
