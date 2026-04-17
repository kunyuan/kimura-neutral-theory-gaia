# Module: s2_rate_calculation

### mammalian_generation_time

**QID:** `github:kimura_neutral_theory::mammalian_generation_time`
**Type:** setting
**Role:** setting
**Content:** For mammals, the average generation time is on the order of years (e.g., roughly 1 year for small mammals, longer for large mammals). Kimura uses an approximate figure for illustrative calculation.

### normalized_aa_rate

**QID:** `github:kimura_neutral_theory::normalized_aa_rate`
**Type:** claim
**Role:** derived
**Content:** Averaging figures for haemoglobin, cytochrome c, and triosephosphate dehydrogenase gives an evolutionary rate of approximately one amino-acid substitution in $28 \times 10^6$ years (i.e., $2.8 \times 10^7$ years) for a polypeptide chain of 100 amino acids.
**Belief:** 0.70
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
**Belief:** 0.39
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::normalized_aa_rate`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['normalized_aa_rate']}}
**Referenced by:** support -> `github:kimura_neutral_theory::haldane_limit_for_mammals`; support -> `github:kimura_neutral_theory::selection_cannot_explain_rate`; compare -> `github:kimura_neutral_theory::_anon_002`; abduction -> `github:kimura_neutral_theory::_anon_002`

### haldane_limit_for_mammals

**QID:** `github:kimura_neutral_theory::haldane_limit_for_mammals`
**Type:** claim
**Role:** derived
**Content:** If we assume that the cost of natural selection per generation is about 0.1 (Haldane, 1957), and that a new allele is substituted by natural selection roughly every 300 generations, then for mammals with approximately $4 \times 10^9$ nucleotide pairs and generation times of a few years, the total number of substitutions attributable to selection would be far fewer than one per two years. Haldane's formula gives approximately one gene substitution every 300 generations. The actual rate of nucleotide substitution estimated from protein data is roughly one substitution every 2 years per genome, which is vastly higher than the selection limit.
**Belief:** 0.59
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::genome_substitution_rate`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['genome_substitution_rate']}}
**Referenced by:** support -> `github:kimura_neutral_theory::selection_cannot_explain_rate`

### selection_cannot_explain_rate

**QID:** `github:kimura_neutral_theory::selection_cannot_explain_rate`
**Type:** claim
**Role:** derived
**Content:** The observed rate of nucleotide substitution (approximately one per two years per mammalian genome) is so high that it cannot be accounted for by natural selection alone. Haldane's cost of natural selection limits the rate of gene substitution by positive selection to roughly one every 300 generations. The observed molecular substitution rate is 100-1,000 times higher than this limit. Therefore, most nucleotide substitutions in evolution must not have been driven by positive natural selection.
**Belief:** 0.30
**Derived from:** support
**Premises:** `github:kimura_neutral_theory::genome_substitution_rate`, `github:kimura_neutral_theory::haldane_limit_for_mammals`
**source:** artifacts/paper.pdf, p.625
**gaia:** {'provenance': {'referenced_claims': ['genome_substitution_rate', 'haldane_limit_for_mammals']}}
**Referenced by:** support -> `github:kimura_neutral_theory::neutral_theory_hypothesis`

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
