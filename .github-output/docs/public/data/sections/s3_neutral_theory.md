# Module: s3_neutral_theory

### neutral_theory_hypothesis

**QID:** `github:kimura_neutral_theory::neutral_theory_hypothesis`
**Type:** claim
**Role:** derived
**Content:** Most mutations produced by nucleotide replacement are almost neutral in natural selection, meaning they have so little effect on the fitness of the organism that their fate in the population is determined primarily by random genetic drift rather than by selection. The very high rate of nucleotide substitution observed at the molecular level can be explained if most substitutions are the result of random fixation of selectively neutral or nearly neutral mutations.
**Belief:** 0.22
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::selection_cannot_explain_rate`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['selection_cannot_explain_rate']}}
**Referenced by:** support -> `github:kimura_neutral_theory::heterozygosity_formula`; support -> `github:kimura_neutral_theory::neutral_predicts_rate`; abduction -> `github:kimura_neutral_theory::_anon_002`; support -> `github:kimura_neutral_theory::genetic_drift_importance`; unknown -> `github:kimura_neutral_theory::not_both_views`

### selectionist_view

**QID:** `github:kimura_neutral_theory::selectionist_view`
**Type:** claim
**Role:** independent
**Content:** The conventional (selectionist) view holds that most molecular evolution is driven by positive natural selection: each amino-acid or nucleotide substitution that becomes fixed in a population does so because it confers a selective advantage. Under this view, the substitution rate is limited by Haldane's cost of natural selection.
**Belief:** 0.39
**Referenced by:** support -> `github:kimura_neutral_theory::selectionist_predicts_rate`; abduction -> `github:kimura_neutral_theory::_anon_002`; unknown -> `github:kimura_neutral_theory::not_both_views`

### not_both_views

**QID:** `github:kimura_neutral_theory::not_both_views`
**Type:** claim
**Role:** structural
**Content:** not_both_true(A, B)
**Prior:** 0.95
**Belief:** 1.00
**helper_kind:** contradiction_result
**prior:** 0.95

### neutral_substitution_formula

**QID:** `github:kimura_neutral_theory::neutral_substitution_formula`
**Type:** claim
**Role:** derived
**Content:** For neutral mutations, the rate of mutant substitution in the population (the rate at which new alleles become fixed) is:

$$k = u$$

where $u$ is the mutation rate per gamete per generation. This result holds because the probability that a new neutral mutation eventually becomes fixed in a population of effective size $N_e$ is $1/(2N_e)$, and the number of new neutral mutations appearing each generation is $2N_e u$. Multiplying these: $k = 2N_e u \times \frac{1}{2N_e} = u$. This is independent of population size.
**Belief:** 0.67
**Derived from:** deduction
**Premises:** `github:kimura_neutral_theory::neutral_fixation_probability`
**source:** artifacts/paper.pdf, p.625, formula (1)
**gaia:** {'provenance': {'referenced_claims': ['neutral_fixation_probability']}}
**Referenced by:** support -> `github:kimura_neutral_theory::neutral_predicts_rate`; abduction -> `github:kimura_neutral_theory::_anon_002`; support -> `github:kimura_neutral_theory::neutral_rate_consistency`

### neutral_fixation_probability

**QID:** `github:kimura_neutral_theory::neutral_fixation_probability`
**Type:** claim
**Role:** independent
**Content:** For a selectively neutral mutation in a diploid population of effective size $N_e$, the probability of eventual fixation is $p = 1/(2N_e)$, which equals the initial frequency of the new allele if it appears as a single copy.
**Belief:** 0.45
**source:** artifacts/paper.pdf, p.625
**Referenced by:** deduction -> `github:kimura_neutral_theory::neutral_substitution_formula`

### heterozygosity_formula

**QID:** `github:kimura_neutral_theory::heterozygosity_formula`
**Type:** claim
**Role:** derived
**Content:** Kimura and Crow (1964) showed that for neutral mutations, the probability that a randomly chosen individual is homozygous at a locus is $1/(4N_e u + 1)$, where $N_e$ is the effective population number and $u$ is the mutation rate per locus per generation. Therefore, the expected heterozygosity is:

$$H_e = \frac{4 N_e u}{4 N_e u + 1}$$

To attain a heterozygosity of at least $H_e = 0.12$, it is necessary that $N_e \geq 2{,}300$. For a higher heterozygosity such as $H_e = 0.35$, $N_e$ must be about $8{,}000$.
**Belief:** 0.47
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::neutral_theory_hypothesis`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['neutral_theory_hypothesis']}}
**Referenced by:** support -> `github:kimura_neutral_theory::drosophila_heterozygosity`

### drosophila_heterozygosity

**QID:** `github:kimura_neutral_theory::drosophila_heterozygosity`
**Type:** claim
**Role:** derived
**Content:** For Drosophila, with migration between subgroups, heterozygosity of 35 per cent may be attained even if the effective population size $N_e$ is much smaller for each subgroup. This is consistent with the neutral theory's prediction that heterozygosity is maintained by the balance between neutral mutation and random genetic drift.
**Belief:** 0.64
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::heterozygosity_formula`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['heterozygosity_formula']}}

### neutral_predicts_rate

**QID:** `github:kimura_neutral_theory::neutral_predicts_rate`
**Type:** claim
**Role:** derived
**Content:** Under the neutral theory, the substitution rate equals the mutation rate ($k = u$), which for mammals with ~$4 \times 10^9$ nucleotide pairs and error rates of $10^{-8}$ to $10^{-9}$ per nucleotide per replication, predicts a genome-wide substitution rate on the order of one per few years. This matches the observed rate of ~1 substitution per 2 years.
**Belief:** 0.39
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::neutral_theory_hypothesis`, `github:kimura_neutral_theory::neutral_substitution_formula`
**gaia:** {'provenance': {'referenced_claims': ['neutral_substitution_formula', 'neutral_theory_hypothesis']}}
**Referenced by:** compare -> `github:kimura_neutral_theory::_anon_002`; abduction -> `github:kimura_neutral_theory::_anon_002`

### selectionist_predicts_rate

**QID:** `github:kimura_neutral_theory::selectionist_predicts_rate`
**Type:** claim
**Role:** derived
**Content:** Under the selectionist view, the substitution rate is limited by Haldane's cost of natural selection to roughly one gene substitution every 300 generations. For mammals, this predicts a far lower rate than the observed ~1 substitution per 2 years, a discrepancy of 2-3 orders of magnitude.
**Belief:** 0.39
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::selectionist_view`
**gaia:** {'provenance': {'referenced_claims': ['selectionist_view']}}
**Referenced by:** compare -> `github:kimura_neutral_theory::_anon_002`; abduction -> `github:kimura_neutral_theory::_anon_002`

### github:kimura_neutral_theory::_anon_002

**QID:** `github:kimura_neutral_theory::_anon_002`
**Type:** claim
**Role:** derived
**Content:** compare(Under the neutral theory, the substitution rate equals the mutation rate ($k = u$), which for mammals with ~$4 \times 10^9$ nucleotide pairs and error rates of $10^{-8}$ to $10^{-9}$ per nucleotide per replication, predicts a genome-wide substitution rate on the order of one per few years. This matches the observed rate of ~1 substitution per 2 years., Under the selectionist view, the substitution rate is limited by Haldane's cost of natural selection to roughly one gene substitution every 300 generations. For mammals, this predicts a far lower rate than the observed ~1 substitution per 2 years, a discrepancy of 2-3 orders of magnitude., Extrapolating from the averaged amino-acid substitution rate to the whole genome, and noting that a polypeptide of 100 amino acids is coded by 300 nucleotide pairs, the rate of nucleotide substitution per genome per year is estimated as:

$$k = \frac{1}{2.8 \times 10^7} \times \frac{4 \times 10^9}{3 \times 10^2} \approx \frac{1}{2}$$

That is, approximately one nucleotide pair substitution in the population every 2 years, or equivalently about one substitution every 1.8 years across the entire mammalian genome.)
**Belief:** 1.00
**Derived from:** compare
**Premises:** `github:kimura_neutral_theory::neutral_predicts_rate`, `github:kimura_neutral_theory::selectionist_predicts_rate`, `github:kimura_neutral_theory::genome_substitution_rate`
**Derived from:** abduction
**Premises:** `github:kimura_neutral_theory::neutral_theory_hypothesis`, `github:kimura_neutral_theory::neutral_substitution_formula`, `github:kimura_neutral_theory::selectionist_view`, `github:kimura_neutral_theory::neutral_predicts_rate`, `github:kimura_neutral_theory::selectionist_predicts_rate`, `github:kimura_neutral_theory::genome_substitution_rate`
**helper_kind:** comparison_claim
**generated:** True
**gaia:** {'provenance': {'referenced_claims': ['genome_substitution_rate', 'neutral_predicts_rate', 'selectionist_predicts_rate']}}

### github:kimura_neutral_theory::_anon_003

**QID:** `github:kimura_neutral_theory::_anon_003`
**Type:** claim
**Role:** orphaned
**Content:** abduction_validity(support, support, compare)
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** Both the neutral theory and the selectionist view attempt to explain the observed genome-wide nucleotide substitution rate. The neutral theory correctly predicts the high rate via $k = u$, while the selectionist view predicts a rate orders of magnitude too low due to Haldane's cost constraint.
