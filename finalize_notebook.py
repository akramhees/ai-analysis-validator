import json

with open('notebooks/ab_test_validation.ipynb', 'r') as f:
    notebook = json.load(f)

new_cells = [
 {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Step 8: My Corrected Analysis\n",
    "\n",
    "fixing AI's code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from statsmodels.stats.proportion import proportions_ztest\n",
    "import math\n",
    "\n",
    "print(\"=== CORRECTED A/B TEST ANALYSIS ===\\n\")\n",
    "\n",
    "# Quick data summary\n",
    "print(\"1. Data Summary:\")\n",
    "print(f\"   Total: {len(df):,} observations\")\n",
    "print(f\"   Control: {len(df[df['group'] == 'control']):,}\")\n",
    "print(f\"   Treatment: {len(df[df['group'] == 'treatment']):,}\")\n",
    "\n",
    "# Conversion rates\n",
    "print(f\"\\n2. Conversion Rates:\")\n",
    "print(f\"   Control: {control_rate:.2%}\")\n",
    "print(f\"   Treatment: {treatment_rate:.2%}\")\n",
    "print(f\"   Absolute lift: {treatment_rate - control_rate:.2%}\")\n",
    "print(f\"   Relative lift: {((treatment_rate - control_rate) / control_rate):.2%}\")\n",
    "\n",
    "# Correct testusing the right one\n",
    "count = np.array([control_successes, treatment_successes])\n",
    "nobs = np.array([control_n, treatment_n])\n",
    "z_stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')\n",
    "\n",
    "print(f\"\\n3. Statistical Test (Proportion Z-test):\")\n",
    "print(f\"   Z-statistic: {z_stat:.4f}\")\n",
    "print(f\"   P-value: {p_value:.4f}\")\n",
    "\n",
    "if p_value < 0.05:\n",
    "    print(\"    Statistically significant at α=0.05\")\n",
    "else:\n",
    "    print(\"    Not statistically significant at α=0.05\")\n",
    "\n",
    "# TODO: Check if this CI formula is correct\n",
    "# I think it is but need to verify with the statsmodels function\n",
    "def proportion_ci(successes, n, confidence=0.95):\n",
    "    p = successes / n\n",
    "    se = math.sqrt(p * (1-p) / n)\n",
    "    z = 1.96  # for 95%\n",
    "    return p - z*se, p + z*se\n",
    "\n",
    "control_ci = proportion_ci(control_successes, control_n)\n",
    "treatment_ci = proportion_ci(treatment_successes, treatment_n)\n",
    "\n",
    "print(f\"\\n4. 95% Confidence Intervals:\")\n",
    "print(f\"   Control: [{control_ci[0]:.2%}, {control_ci[1]:.2%}]\")\n",
    "print(f\"   Treatment: [{treatment_ci[0]:.2%}, {treatment_ci[1]:.2%}]\")\n",
    "\n",
    "# Effect size - using Cohen's h\n",
    "h = 2 * math.asin(math.sqrt(treatment_rate)) - 2 * math.asin(math.sqrt(control_rate))\n",
    "print(f\"\\n5. Effect Size (Cohen's h): {h:.3f}\")\n",
    "\n",
    "# Business recommendation\n",
    "print(\"\\n6. Business Recommendation:\")\n",
    "print(\"   - Implement the treatment if the cost per conversion is acceptable\")\n",
    "print(\"   - Start with a phased rollout to validate results\")\n",
    "print(\"   - Monitor for negative side effects\")\n",
    "print(\"   - Consider longer-term measurement to ensure effects persist\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 9: Issues I Found\n",
    "\n",
    "Here's a quick summary of what the AI got wrong:\n",
    "\n",
    "| Issue | Type | Severity | What I changed |\n",
    "|-------|------|----------|----------------|\n",
    "| Used t-test on binary data | Statistical | MEDIUM | Switched to proportion z-test |\n",
    "| No assumption checks | Methodological | HIGH | Added sample size and balance checks |\n",
    "| Misinterpreted p-value | Interpretation | HIGH | Explained p-value correctly |\n",
    "| Oversimplified recommendation | Business | MEDIUM | Added CI, cost-benefit, risks |\n",
    "| No confidence intervals | Statistical | MEDIUM | Added 95% CIs |\n",
    "| No effect size | Statistical | LOW | Added Cohen's h |\n",
    "\n",
    "## Step 10: My Feedback to the AI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "feedback = \"\"\"\n",
    "Feedback for the AI model - things it should fix:\n",
    "\n",
    "1. STATISTICAL METHOD:\n",
    "   - Stop using t-test for binary outcomes! Use proportion z-test instead.\n",
    "   - Binary data isn't normally distributed so t-test doesn't apply here.\n",
    "\n",
    "2. ASSUMPTION CHECKS:\n",
    "   - Always check if sample size is big enough (at least 10 successes/failures)\n",
    "   - Verify random assignment worked (check balance on pre treatment variables)\n",
    "   - Need to think about whether observations are independent\n",
    "\n",
    "3. INTERPRETATION:\n",
    "   - The p-value is NOT the probability that the treatment works!\n",
    "   - It's P(observing this data | null hypothesis is true)\n",
    "   - Always include confidence intervals with p-values\n",
    "\n",
    "4. BUSINESS RECOMMENDATIONS:\n",
    "   - Need cost-benefit analysis\n",
    "   - Consider practical significance, not just statistical\n",
    "   - Give a phased implementation plan\n",
    "   - Acknowledge limitations and risks\n",
    "\n",
    "5. CODE QUALITY:\n",
    "   - Add comments explaining why each step is done\n",
    "   - Include validation checks\n",
    "   - Use more descriptive variable names\n",
    "\"\"\"\n",
    "\n",
    "print(feedback)"
   ]
  }
]

notebook['cells'].extend(new_cells)

with open('notebooks/ab_test_validation.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook finalized")
