
# Final Summary

## Overview of the Dataset and Research Question

This analysis used the Palmer Penguins dataset to investigate
whether mean flipper length differs among Adelie, Chinstrap, and
Gentoo penguins. Species was the categorical independent variable,
and flipper length measured in millimeters was the numeric dependent
variable.

The group means were:

- **Adelie:** 189.95 mm (n = 151)
- **Chinstrap:** 195.82 mm (n = 68)
- **Gentoo:** 217.19 mm (n = 123)

The research question was: **Does mean flipper length differ
significantly among Adelie, Chinstrap, and Gentoo penguins?**

## Methodology and AI Support

An AI tool assisted with selecting an appropriate dataset, identifying
the independent and dependent variables, developing the research
question, and determining the assumptions that should be evaluated.
The AI recommended using histograms, boxplots, Q-Q plots, Shapiro-Wilk
tests, and Levene's test before conducting the one-way ANOVA.

The null hypothesis stated that all three population means were equal.
The alternative hypothesis stated that at least one species mean was
different. The significance level was set at 0.05.

## Assumption Checks

The Shapiro-Wilk tests suggested departures from normality for Gentoo. However, the histograms and Q-Q plots were also reviewed because formal normality tests can be sensitive to sample size.

Levene's test was not statistically significant (p = 0.7188), so the equality-of-variances assumption was considered reasonable.

Independence was considered reasonable because each row represented
a separate penguin observation.

## ANOVA Results and Interpretation

The one-way ANOVA was statistically significant, F(2, 339) = 594.80, p = 1.352e-111. The null hypothesis was rejected. Mean flipper length differs among at least two of the three penguin species.

The eta-squared value was **0.7782**, indicating a
**large** effect. This represents the proportion
of total variation in flipper length associated with penguin species.

## Post-Hoc Findings

Chinstrap penguins have a significantly higher mean flipper length than Adelie penguins (adjusted p-value = 0.000000). Gentoo penguins have a significantly higher mean flipper length than Adelie penguins (adjusted p-value = 0.000000). Gentoo penguins have a significantly higher mean flipper length than Chinstrap penguins (adjusted p-value = 0.000000).

## Conclusion

The analysis demonstrates how one-way ANOVA can compare the means of
a numeric measurement across three or more independent groups. The
boxplot, group mean plot, confidence intervals, ANOVA results, and
Tukey comparisons provide complementary evidence for understanding
how penguin flipper lengths vary among species.
