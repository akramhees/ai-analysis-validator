import json

with open('notebooks/ab_test_validation.ipynb', 'r') as f:
    notebook = json.load(f)

# Add Step 2: Initial Validation
new_cells = [
 {
  "cell_type": "markdown",
  "metadata": {},
  "source": [
    "## Step 2: Initial Validation/what Looks Good?\n",
    "\n",
    "**First impressions:**\n",
    "- ✓ Code runs without errors\n",
    "- ✓ Calculates basic metrics (conversion rates, lift)\n",
    "- ✓ Uses appropriate test for binary outcome comparison\n",
    "- ✓ Prints clear output\n",
    "\n",
    "**Must find if its correct**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: My Validation - Identifying Issues\n",
    "\n",
    "Ill run the code and systematically check for errors in three areas:\n",
    "1. **Statistical methodology** (wrong test, assumption violations)\n",
    "2. **Code correctness** (bugs, logical errors)\n",
    "3. **Interpretation** (misunderstanding results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from statsmodels.stats.proportion import proportions_ztest\n",
    "\n",
    "sns.set_style(\"whitegrid\")\n",
    "plt.rcParams['figure.figsize'] = (12, 6)\n",
    "\n",
    "df = pd.read_csv('../data/ab_test_data.csv')\n",
    "\n",
    "print(\"=== DATA SUMMARY ===\")\n",
    "print(f\"Total observations: {len(df):,}\")\n",
    "print(f\"Control group: {len(df[df['group'] == 'control']):,}\")\n",
    "print(f\"Treatment group: {len(df[df['group'] == 'treatment']):,}\")\n",
    "print(f\"\\nSample characteristics:\")\n",
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "control_rate = df[df['group'] == 'control']['converted'].mean()\n",
    "treatment_rate = df[df['group'] == 'treatment']['converted'].mean()\n",
    "\n",
    "print(\"=== AI'S RESULTS (EXECUTED) ===\")\n",
    "print(f\"Control conversion rate: {control_rate:.2%}\")\n",
    "print(f\"Treatment conversion rate: {treatment_rate:.2%}\")\n",
    "print(f\"Lift: {((treatment_rate - control_rate) / control_rate):.2%}\")\n",
    "\n",
    "control_converted = df[df['group'] == 'control']['converted']\n",
    "treatment_converted = df[df['group'] == 'treatment']['converted']\n",
    "\n",
    "t_stat, p_value = stats.ttest_ind(control_converted, treatment_converted)\n",
    "\n",
    "print(f\"\\nT-statistic: {t_stat:.4f}\")\n",
    "print(f\"P-value: {p_value:.4f}\")\n",
    "\n",
    "if p_value < 0.05:\n",
    "    print(\"\\n✓ AI says: Result is statstically significant\")\n",
    "    print(\"✓ AI says: Treatment is better than control\")\n",
    "else:\n",
    "    print(\"\\n✗ Result is not statistically significant\")"
   ]
  }
]

notebook['cells'].extend(new_cells)

with open('notebooks/ab_test_validation.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Validation cells added")
