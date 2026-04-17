# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Haemoglobin amino-acid substitution rate

1. **Cytochrome c substitution rate** (prior: 0.50 → belief: 0.38)
   - → supports: selection_cannot_explain_rate

2. **Triosephosphate dehydrogenase substitution rate** (prior: 0.50 → belief: 0.38)
   - → supports: selection_cannot_explain_rate

3. **Haemoglobin amino-acid substitution rate** (prior: 0.50 → belief: 0.38)
   - → supports: selection_cannot_explain_rate

## Selectionist view: substitutions driven by positive selection

4. **Selectionist view: substitutions driven by positive selection** (prior: 0.50 → belief: 0.39)
   - → supports: not_both_views

## Fixation probability of a neutral allele is 1/(2Ne)

5. **Watson's estimate of nucleotide misincorporation rate** (prior: 0.50 → belief: 0.43)
   - → supports: genetic_drift_importance

6. **~50 cell divisions from zygote to gamete in humans** (prior: 0.50 → belief: 0.43)
   - → supports: genetic_drift_importance

7. **Fixation probability of a neutral allele is 1/(2Ne)** (prior: 0.50 → belief: 0.45)
   - → supports: genetic_drift_importance

## Selection alone cannot explain the observed substitution rate

8. **Selection alone cannot explain the observed substitution rate ★** (prior: 0.50 → belief: 0.30)
   - ← infer(cytochrome_c_rate, haemoglobin_rate, triosephosphate_rate) [0.00 bits]
   - → supports: neutral_theory_hypothesis

## Neutral theory: most molecular substitutions are selectively neutral

9. **Neutral theory: most molecular substitutions are selectively neutral ★** (prior: 0.50 → belief: 0.22)
   - ← infer(selection_cannot_explain_rate) [0.18 bits]
   - → supports: genetic_drift_importance, not_both_views

## Random genetic drift must be recognized as important

10. **not_both_views** (prior: 0.95 → belief: 1.00)

11. **Random genetic drift must be recognized as important ★** (prior: 0.50 → belief: 0.39)
   - ← infer(cell_divisions_to_gamete, neutral_fixation_probability, neutral_theory_hypothesis, watson_mutation_rate) [0.04 bits]
