# Module: motivation

### mammalian_genome_size

**QID:** `github:kimura_neutral_theory::mammalian_genome_size`
**Type:** setting
**Role:** setting
**Content:** The haploid genome of mammals contains approximately $4 \times 10^9$ nucleotide pairs.

### genetic_code_triplet

**QID:** `github:kimura_neutral_theory::genetic_code_triplet`
**Type:** setting
**Role:** setting
**Content:** Each amino acid is encoded by a triplet of three nucleotides (a codon) in the genetic code.

### haldane_cost_principle

**QID:** `github:kimura_neutral_theory::haldane_cost_principle`
**Type:** setting
**Role:** setting
**Content:** Haldane (1957) showed that natural selection imposes a 'cost' on a population undergoing gene substitution: each substitution by natural selection requires a certain number of selective deaths (genetic deaths). This limits the rate at which gene substitutions can occur by natural selection to roughly one substitution every 300 generations.

### research_question

**QID:** `github:kimura_neutral_theory::research_question`
**Type:** question
**Role:** question
**Content:** Can the observed rate of molecular evolution (nucleotide substitutions) be explained by natural selection alone, or must most substitutions be selectively neutral?

### haemoglobin_rate

**QID:** `github:kimura_neutral_theory::haemoglobin_rate`
**Type:** claim
**Role:** independent
**Content:** Comparative studies of haemoglobin molecules among different groups of mammals suggest that amino-acid substitution has taken place roughly at the rate of one amino-acid change in $10^7$ years for a chain consisting of about 140 amino acids. For example, by comparing the $\alpha$ and $\beta$ chains of man with those of horse, pig, cattle and rabbit, the figure of one amino-acid change in $7 \times 10^6$ years was obtained (Zuckerkandl and Pauling, 1965).
**Belief:** 0.38
**source:** artifacts/paper.pdf, p.624
**Referenced by:** support -> `github:kimura_neutral_theory::normalized_aa_rate`; induction -> `github:kimura_neutral_theory::normalized_aa_rate`; induction -> `github:kimura_neutral_theory::normalized_aa_rate`

### cytochrome_c_rate

**QID:** `github:kimura_neutral_theory::cytochrome_c_rate`
**Type:** claim
**Role:** independent
**Content:** The rate of amino-acid substitution estimated by comparing gorilla and human cytochrome c (a chain of about 100 amino acids) turned out to be approximately one replacement in $4.5 \times 10^7$ years.
**Belief:** 0.38
**source:** artifacts/paper.pdf, p.625
**Referenced by:** support -> `github:kimura_neutral_theory::normalized_aa_rate`; induction -> `github:kimura_neutral_theory::normalized_aa_rate`; induction -> `github:kimura_neutral_theory::normalized_aa_rate`

### triosephosphate_rate

**QID:** `github:kimura_neutral_theory::triosephosphate_rate`
**Type:** claim
**Role:** independent
**Content:** Comparing triosephosphate dehydrogenase of rabbit with that of other species yields a figure of at least one amino-acid substitution for every $2.5 \times 10^7$ years for chains of about 1,110 amino acids. This figure is roughly equivalent to the rate of one amino-acid substitution in $2.8 \times 10^7$ years for a chain consisting of 100 amino acids.
**Belief:** 0.38
**source:** artifacts/paper.pdf, p.625
**Referenced by:** support -> `github:kimura_neutral_theory::normalized_aa_rate`; induction -> `github:kimura_neutral_theory::normalized_aa_rate`

### dna_content_coding_fraction

**QID:** `github:kimura_neutral_theory::dna_content_coding_fraction`
**Type:** claim
**Role:** orphaned
**Content:** Kimura estimated that the DNA content in terms of nucleotide pairs is at most a few per cent of the total for higher organisms. Taking the equivalent of about $10^7$ nucleotide pairs as coding for amino acids (a polypeptide chain of 100 amino acids corresponds to 300 nucleotide pairs), the evolutionary rate for the coding region appears to be very low for cytochrome c, but amounts to a very high rate for the entire genome when extrapolated.
**Belief:** 0.50
**source:** artifacts/paper.pdf, p.625
