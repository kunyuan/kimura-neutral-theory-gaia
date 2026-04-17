# Module: s2_rate_calculation

### mammalian_generation_time

**QID:** `github:kimura_neutral_theory::mammalian_generation_time`
**Type:** setting
**Role:** setting
**Content:** For mammals, the average length of one generation varies by body size: roughly 1-2 years for small mammals (mice, rabbits) and up to 20-30 years for large mammals (humans, elephants). Kimura uses an order-of-magnitude figure of a few years for the illustrative calculation comparing molecular rates with Haldane's cost limit.

### normalized_aa_rate

**QID:** `github:kimura_neutral_theory::normalized_aa_rate`
**Type:** claim
**Role:** derived
**Content:** Averaging figures for haemoglobin, cytochrome c, and triosephosphate dehydrogenase gives an evolutionary rate of approximately one amino-acid substitution in $28 \times 10^6$ years (i.e., $2.8 \times 10^7$ years) for a polypeptide chain of 100 amino acids.
**Belief:** 1.00
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::haemoglobin_rate`
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::cytochrome_c_rate`
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::triosephosphate_rate`
**Derived from:** induction
**Premises:** `github:kimura_neutral_theory::haemoglobin_rate`, `github:kimura_neutral_theory::cytochrome_c_rate`
**Derived from:** induction
**Premises:** `github:kimura_neutral_theory::haemoglobin_rate`, `github:kimura_neutral_theory::cytochrome_c_rate`, `github:kimura_neutral_theory::triosephosphate_rate`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['cytochrome_c_rate', 'haemoglobin_rate', 'triosephosphate_rate']}}
**Referenced by:** support -> `github:kimura_neutral_theory::genome_substitution_rate`

### genome_substitution_rate

**QID:** `github:kimura_neutral_theory::genome_substitution_rate`
**Type:** claim
**Role:** derived
**Content:** Extrapolating from the averaged amino-acid substitution rate to the whole genome, and noting that a polypeptide of 100 amino acids is coded by 300 nucleotide pairs, the rate of nucleotide substitution per genome per year is estimated as:

$$k = \frac{1}{2.8 \times 10^7} \times \frac{4 \times 10^9}{3 \times 10^2} \approx \frac{1}{2}$$

That is, approximately one nucleotide pair substitution in the population every 2 years, or equivalently about one substitution every 1.8 years across the entire mammalian genome.
**Belief:** 1.00
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::normalized_aa_rate`
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::neutral_theory_hypothesis`, `github:kimura_neutral_theory::neutral_substitution_formula`
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::selectionist_view`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['genome_substitution_rate', 'neutral_substitution_formula', 'neutral_theory_hypothesis', 'normalized_aa_rate', 'selectionist_view']}}
**Referenced by:** support -> `github:kimura_neutral_theory::selection_cannot_explain_rate`; compare -> `github:kimura_neutral_theory::_anon_002`; abduction -> `github:kimura_neutral_theory::_anon_002`

### selection_cannot_explain_rate

**QID:** `github:kimura_neutral_theory::selection_cannot_explain_rate`
**Type:** claim
**Role:** derived
**Content:** The observed rate of nucleotide substitution (approximately one per two years per mammalian genome) is so high that it cannot be accounted for by natural selection alone. Haldane (1957) showed that the cost of natural selection limits the rate of gene substitution by positive selection to roughly one every 300 generations. For mammals with generation times of a few years, 300 generations corresponds to hundreds to thousands of years. The observed molecular substitution rate is therefore 100-1,000 times higher than this limit, meaning most nucleotide substitutions in evolution must not have been driven by positive natural selection.
**Belief:** 0.95
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::genome_substitution_rate`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['genome_substitution_rate']}}

### github:kimura_neutral_theory::_anon_000

**QID:** `github:kimura_neutral_theory::_anon_000`
**Type:** claim
**Role:** orphaned
**Content:** Are observations independent? Do they support the same law?
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** Haemoglobin and cytochrome c are independent protein families.

### github:kimura_neutral_theory::_anon_001

**QID:** `github:kimura_neutral_theory::_anon_001`
**Type:** claim
**Role:** orphaned
**Content:** Are observations independent? Do they support the same law?
**Belief:** 0.50
**helper_kind:** composition_validity
**generated:** True
**warrant:** Triosephosphate dehydrogenase is independent of haemoglobin and cytochrome c.
