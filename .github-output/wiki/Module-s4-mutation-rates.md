# Module: s4_mutation_rates

### watson_mutation_rate

**QID:** `github:kimura_neutral_theory::watson_mutation_rate`
**Type:** claim
**Role:** independent
**Content:** From a consideration of the average energy of hydrogen bonds and from information on mutation of rIIA gene in phage T4, Watson (1965) obtained $10^{-8}$ to $10^{-9}$ as the average probability of error in the insertion of a new nucleotide during DNA replication.
**Prior:** 0.80
**Belief:** 0.80
**source:** artifacts/paper.pdf, p.626
**prior:** 0.8
**prior_justification:** Watson (1965) estimate based on hydrogen bond energetics and phage T4 data; range spans an order of magnitude (10^-8 to 10^-9), substantial uncertainty.
**Referenced by:** support -> `github:kimura_neutral_theory::mammalian_mutation_rate_per_nucleotide`

### cell_divisions_to_gamete

**QID:** `github:kimura_neutral_theory::cell_divisions_to_gamete`
**Type:** claim
**Role:** independent
**Content:** In man, the number of cell divisions along the germ line from the fertilized egg to a gamete is roughly 50.
**Prior:** 0.88
**Belief:** 0.88
**source:** artifacts/paper.pdf, p.626
**prior:** 0.88
**prior_justification:** Well-known figure in developmental biology (~50 divisions from fertilized egg to gamete in humans); reasonable order-of-magnitude estimate.
**Referenced by:** support -> `github:kimura_neutral_theory::mammalian_mutation_rate_per_nucleotide`

### mammalian_mutation_rate_per_nucleotide

**QID:** `github:kimura_neutral_theory::mammalian_mutation_rate_per_nucleotide`
**Type:** claim
**Role:** derived
**Content:** The rate of mutation resulting from base replacement is estimated as $50 \times 10^{-8}$ to $50 \times 10^{-9}$ per nucleotide pair per generation (i.e., $5 \times 10^{-7}$ to $5 \times 10^{-8}$). With approximately $4 \times 10^9$ nucleotide pairs in the mammalian haploid genome, the total number of mutations resulting from base replacement per generation may amount to $200$ to $2{,}000$.
**Belief:** 0.78
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::watson_mutation_rate`, `github:kimura_neutral_theory::cell_divisions_to_gamete`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['cell_divisions_to_gamete', 'watson_mutation_rate']}}
**Referenced by:** support -> `github:kimura_neutral_theory::drosophila_mutation_rate`; support -> `github:kimura_neutral_theory::neutral_rate_consistency`

### drosophila_mutation_rate

**QID:** `github:kimura_neutral_theory::drosophila_mutation_rate`
**Type:** claim
**Role:** derived
**Content:** The mutation rate per nucleotide pair per generation in Drosophila is roughly ten times as high as in man (i.e., $u \approx 1.5 \times 10^{-7}$ rather than $u \approx 1.5 \times 10^{-8}$). Another consideration allows the supposition that $u \approx 1.5 \times 10^{-7}$ is probably appropriate for the neutral mutation rate of a cistron in Drosophila.
**Belief:** 0.79
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::mammalian_mutation_rate_per_nucleotide`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['mammalian_mutation_rate_per_nucleotide']}}

### neutral_rate_consistency

**QID:** `github:kimura_neutral_theory::neutral_rate_consistency`
**Type:** claim
**Role:** derived
**Content:** The estimated total mutation rate per generation (200-2,000 base-replacement mutations) is 100-1,000 times larger than the rate of approximately 2 substitutions per generation allowed by Haldane's natural selection cost. This is consistent with the neutral theory's prediction that the mutation rate per nucleotide per generation directly determines the substitution rate ($k = u$), because neutral mutations fix at a rate equal to the mutation rate regardless of population size.
**Belief:** 0.82
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::mammalian_mutation_rate_per_nucleotide`, `github:kimura_neutral_theory::neutral_substitution_formula`
**source:** artifacts/paper.pdf, p.626
**gaia:** {'provenance': {'referenced_claims': ['mammalian_mutation_rate_per_nucleotide', 'neutral_substitution_formula']}}
**Referenced by:** support -> `github:kimura_neutral_theory::genetic_drift_importance`
