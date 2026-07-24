import json

with open('notebooks/ab_test_validation.ipynb', 'r') as f:
    notebook = json.load(f)

new_cells = [
 {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Step 7: Critical Issue #4 - Business Recommendations\n",
    "\n",
    "### The Problem\n",
    "The AI's recommendation was too simplistic and missing:\n",
    "- Cost-benefit analysis\n",
    "- Confidence intervals\n",
    "- Implementation complexity\n",
    "- Practical significance\n",
    "\n",
    "**Severity:** MEDIUM - The recommendation might be fine but it lacks nuance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"=== BUSINESS RECOMMENDATION ANALYSIS ===\\n\")\n",
    "\n",
    "def proportion_ci(successes, n, confidence=0.95):\n",
    "    p = successes / n\n",
    "    se = math.sqrt(p * (1-p) / n)\n",
    "    z = 1.96\n",
    "    return p - z*se, p + z*se\n",
    "\n",
    "control_ci = proportion_ci(control_successes, control_n)\n",
    "treatment_ci = proportion_ci(treatment_successes, treatment_n)\n",
    "\n",
    "print(\"95% Confidence Intervals:\")\n",
    "print(f\"  Control: [{control_ci[0]:.2%}, {control_ci[1]:.2%}]\")\n",
    "print(f\"  Treatment: [{treatment_ci[0]:.2%}, {treatment_ci[1]:.2%}]\")\n",
    "\n",
    "difference = treatment_rate - control_rate\n",
    "total_users = len(df)\n",
    "expected_extra_conversions = difference * total_users\n",
    "\n",
    "print(f\"\\nEstimated additional conversions if rolled out to all users:\")\n",
    "print(f\"  {expected_extra_conversions:.0f} extra conversions\")\n",
    "\n",
    "print(\"\\nWhat a good recommendation would include:\")\n",
    "print(\"  1. Statistical findings (with CI)\")\n",
    "print(\"  2. Cost-benefit analysis\")\n",
    "print(\"  3. Implementation considerations\")\n",
    "print(\"  4. Potential risks\")\n",
    "print(\"  5. Next steps (e.g., holdout validation)\")"
   ]
  }
]

notebook['cells'].extend(new_cells)

with open('notebooks/ab_test_validation.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Business recommendations added")
