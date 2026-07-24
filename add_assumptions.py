import json

with open('notebooks/ab_test_validation.ipynb', 'r') as f:
    notebook = json.load(f)

new_cells = [
 {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Step 5: Critical Issue #2 , Missing Assumption Checks\n",
    "\n",
    "### The Problem\n",
    "The AI didn't check any assumptions:\n",
    "1. Independence , Are observations independent?\n",
    "2. Sample size , Is it large enough for the test?\n",
    "3. Random assignment , Was it truly randomized?\n",
    "\n",
    "**Severity:** HIGH - Unchecked assumptions can invalidate the entire analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"=== ASSUMPTION CHECKS ===\\n\")\n",
    "\n",
    "print(\"1. Sample Size Adequacy:\")\n",
    "min_successes = min(control_successes, treatment_successes)\n",
    "min_failures = min(control_n - control_successes, treatment_n - treatment_successes)\n",
    "\n",
    "print(f\"   Smallest success count: {min_successes}\")\n",
    "print(f\"   Smallest failure count: {min_failures}\")\n",
    "\n",
    "if min_successes >= 10 and min_failures >= 10:\n",
    "    print(\"    Sample size is adequate (all cells >= 10)\")\n",
    "else:\n",
    "    print(\"    Sample size may be too small - consider Fisher's exact test\")\n",
    "\n",
    "print(\"\\n2. Random Assignment Check:\")\n",
    "if 'pre_test_score' in df.columns:\n",
    "    control_score = df[df['group'] == 'control']['pre_test_score'].mean()\n",
    "    treatment_score = df[df['group'] == 'treatment']['pre_test_score'].mean()\n",
    "    print(f\"   Control mean pre-test: {control_score:.2f}\")\n",
    "    print(f\"   Treatment mean pre-test: {treatment_score:.2f}\")\n",
    "    \n",
    "    _, p_balance = stats.ttest_ind(\n",
    "        df[df['group'] == 'control']['pre_test_score'],\n",
    "        df[df['group'] == 'treatment']['pre_test_score']\n",
    "    )\n",
    "    if p_balance > 0.05:\n",
    "        print(f\"    Groups appear balanced (p={p_balance:.3f})\")\n",
    "    else:\n",
    "        print(f\"    Groups may not be balanced (p={p_balance:.3f})\")\n",
    "\n",
    "print(\"\\n3. Effect Size:\")\n",
    "effect_size = treatment_rate - control_rate\n",
    "relative_lift = (treatment_rate - control_rate) / control_rate\n",
    "print(f\"   Absolute difference: {effect_size:.2%}\")\n",
    "print(f\"   Relative lift: {relative_lift:.2%}\")\n",
    "\n",
    "import math\n",
    "h = 2 * math.asin(math.sqrt(treatment_rate)) - 2 * math.asin(math.sqrt(control_rate))\n",
    "print(f\"   Cohen's h: {h:.3f}\")\n",
    "if abs(h) < 0.2:\n",
    "    print(\"   → Small effect size\")\n",
    "elif abs(h) < 0.5:\n",
    "    print(\"   → Medium effect size\")\n",
    "else:\n",
    "    print(\"   → Large effect size\")"
   ]
  }
]

notebook['cells'].extend(new_cells)

with open('notebooks/ab_test_validation.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Assumption checks added!")
