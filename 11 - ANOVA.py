# ANOVA example between 'Honda' and 'Subaru':
# Extract data required
from scipy import stats

df_anova = auto_df[['make', 'price']]

# Group data by different makes
grouped_anova = df_anova.groupby(['make'])

# Use f_oneway() to produce results (scipy stats module)
# Results from this confirm that the prices between hondas and subarus are not significantly different ad the f-test score is less than 1 and p-value is larger than 0.05
anova_results_1 = stats.f_oneway(grouped_anova.get_group('honda')['price'], grouped_anova.get_group('subaru')['price'])

anova_results_1

# ANOVA between hondas and jaguars:
# Results from this show that the price of hondas and jaguars is significantly different as the f-score is very large
# F = 401 and the p-value is larger than 0.05
anova_results_2 = stats.f_oneway(grouped_anova.get_group('honda')['price'], grouped_anova.get_group('jaguar')['price'])

anova_results_2
