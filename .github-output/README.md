# kimura-neutral-theory-gaia

Add your description here

<!-- badges:start -->
<!-- badges:end -->

## Overview

> [!TIP]
> **Reasoning graph information gain: `0.2 bits`**
>
> Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    haemoglobin_rate["Haemoglobin amino-acid substitution rate\n(0.50 → 0.38)"]:::premise
    cytochrome_c_rate["Cytochrome c substitution rate\n(0.50 → 0.38)"]:::premise
    triosephosphate_rate["Triosephosphate dehydrogenase substitution rate\n(0.50 → 0.38)"]:::premise
    selection_cannot_explain_rate["★ Selection alone cannot explain the observed substitution rate\n(0.50 → 0.30)"]:::exported
    neutral_theory_hypothesis["★ Neutral theory: most molecular substitutions are selectively neutral\n(0.50 → 0.22)"]:::exported
    neutral_fixation_probability["Fixation probability of a neutral allele is 1/(2Ne)\n(0.50 → 0.45)"]:::premise
    watson_mutation_rate["Watson's estimate of nucleotide misincorporation rate\n(0.50 → 0.43)"]:::premise
    cell_divisions_to_gamete["~50 cell divisions from zygote to gamete in humans\n(0.50 → 0.43)"]:::premise
    genetic_drift_importance["★ Random genetic drift must be recognized as important\n(0.50 → 0.39)"]:::exported
    not_both_views["not_both_views\n(0.95 → 1.00)"]:::premise
    selectionist_view["Selectionist view: substitutions driven by positive selection\n(0.50 → 0.39)"]:::premise
    strat_0(["infer\n0.04 bits"]):::weak
    cell_divisions_to_gamete --> strat_0
    neutral_fixation_probability --> strat_0
    neutral_theory_hypothesis --> strat_0
    watson_mutation_rate --> strat_0
    strat_0 --> genetic_drift_importance
    strat_1(["infer\n0.00 bits"]):::weak
    cytochrome_c_rate --> strat_1
    haemoglobin_rate --> strat_1
    triosephosphate_rate --> strat_1
    strat_1 --> selection_cannot_explain_rate
    strat_2(["infer\n0.18 bits"]):::weak
    selection_cannot_explain_rate --> strat_2
    strat_2 --> neutral_theory_hypothesis
    oper_0{{"⊗"}}:::contra
    neutral_theory_hypothesis --- oper_0
    selectionist_view --- oper_0
    oper_0 --- not_both_views

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| genetic_drift_importance | If the main conclusion is correct (that neutral or nearly neutral mutations a... | 0.50 | 0.39 |
| neutral_theory_hypothesis | Most mutations produced by nucleotide replacement are almost neutral in natur... | 0.50 | 0.22 |
| selection_cannot_explain_rate | The observed rate of nucleotide substitution (approximately one per two years... | 0.50 | 0.30 |

<!-- content:start -->
<!-- content:end -->
