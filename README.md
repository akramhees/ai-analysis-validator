AI Generated A/B Test Analysis Validator

Project Overview
This project demonstrates my ability to evaluate AI generated quantitative work

I prompted an AI model to analyze A/B test data and generate a statistical report and I then systematically validated its work for
Technical accuracy(statistical methods, code correctness)
Methodological soundness(experimental design, assumption checks)
Interpretation validity(conclusions drawn from results)
Realworld applicability(business recommendations)

Key Findings
 Major Issue: AI misinterpreted p-value as "probability treatment is better" (it's actually P(data | null))
Methodological Flaw: AI failed to check normality and variance homogeneity assumptions
Code Bug: AI used one tailed test when two tailed was th appropriate choice
Recommendation: AI's conclusion was correct but for wrong reasons, this is dangerous in practice

Skills Demonstrated
Statistical validation 
Code review 
Technical writing 
Critical thinking 
Experimental design

Technologies Used
 Python 3.9+
Pandas, NumPy
SciPy 
Matplotlib, Seaborn 
Jupyter Notebook

How to Run
1. `pip install -r requirements.txt`
2. `jupyter notebook`
3. Open `notebooks/ab_test_validation.ipynb`
4. Run cells sequentially
