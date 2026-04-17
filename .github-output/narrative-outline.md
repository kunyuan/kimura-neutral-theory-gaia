# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Neutral theory: most molecular substitutions are selectively neutral

1. **Selectionist view: substitutions driven by positive selection** (prior: 0.50 → belief: 0.29)
   - → supports: selection_cannot_explain_rate, not_both_views

2. **Watson's estimate of nucleotide misincorporation rate** (prior: 0.80 → belief: 0.80)
   - → supports: genetic_drift_importance

3. **~50 cell divisions from zygote to gamete in humans** (prior: 0.88 → belief: 0.88)
   - → supports: genetic_drift_importance

4. **Triosephosphate dehydrogenase substitution rate** (prior: 0.85 → belief: 0.91)
   - → supports: selection_cannot_explain_rate

5. **Cytochrome c substitution rate** (prior: 0.90 → belief: 0.94)
   - → supports: selection_cannot_explain_rate

6. **Fixation probability of a neutral allele is 1/(2Ne)** (prior: 0.95 → belief: 0.96)
   - → supports: genetic_drift_importance, selection_cannot_explain_rate

7. **Haemoglobin amino-acid substitution rate** (prior: 0.92 → belief: 0.96)
   - → supports: selection_cannot_explain_rate

8. **Neutral theory: most molecular substitutions are selectively neutral ★** (prior: 0.50 → belief: 0.47)
   - → supports: genetic_drift_importance, selection_cannot_explain_rate, not_both_views

## Selection alone cannot explain the observed substitution rate

9. **not_both_views** (prior: 0.95 → belief: 1.00)

10. **Random genetic drift must be recognized as important ★** (prior: 0.50 → belief: 0.66)
   - ← infer(cell_divisions_to_gamete, neutral_fixation_probability, neutral_theory_hypothesis, watson_mutation_rate) [0.11 bits]

11. **Selection alone cannot explain the observed substitution rate ★** (prior: 0.50 → belief: 0.95)
   - ← infer(cytochrome_c_rate, haemoglobin_rate, neutral_fixation_probability, neutral_theory_hypothesis, selectionist_view, triosephosphate_rate) [0.00 bits]
