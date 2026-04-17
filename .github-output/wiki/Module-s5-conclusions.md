# Module: s5_conclusions

### genetic_drift_importance

**QID:** `github:kimura_neutral_theory::genetic_drift_importance`
**Type:** claim
**Role:** derived
**Content:** If the main conclusion is correct (that neutral or nearly neutral mutations are being produced in each generation at a much higher rate than has been considered before), then we must recognize the great importance of random genetic drift due to finite population number in forming the genetic structure of biological populations. The significance of random genetic drift has been depreciated during the past decade, influenced by the opinion that almost no mutations are neutral and that population sizes are usually so large that random sampling of gametes should be negligible.
**Belief:** 0.66
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::neutral_theory_hypothesis`, `github:kimura_neutral_theory::neutral_rate_consistency`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['neutral_rate_consistency', 'neutral_theory_hypothesis']}}
**Referenced by:** support -> `github:kimura_neutral_theory::founder_principle_inadequate`

### founder_principle_inadequate

**QID:** `github:kimura_neutral_theory::founder_principle_inadequate`
**Type:** claim
**Role:** derived
**Content:** To emphasize the founder principle but deny the importance of random genetic drift due to finite population number is, in Kimura's opinion, rather similar to assuming a great flood to explain the formation of deep valleys but rejecting a gradual but long lasting process of erosion by water as insufficient to produce such a result.
**Belief:** 0.80
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::genetic_drift_importance`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['genetic_drift_importance']}}
