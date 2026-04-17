"""Introduction: Observed Rates of Molecular Evolution"""

from gaia.lang import claim, setting, question


# === Settings: Established background facts ===

mammalian_genome_size = setting(
    "The haploid genome of mammals contains approximately $4 \\times 10^9$ nucleotide pairs.",
    title="Mammalian haploid genome size",
)

genetic_code_triplet = setting(
    "Each amino acid is encoded by a triplet of three nucleotides (a codon) in the genetic code.",
    title="Triplet genetic code",
)

haldane_cost_principle = setting(
    "Haldane (1957) showed that natural selection imposes a 'cost' on a population undergoing "
    "gene substitution: each substitution by natural selection requires a certain number of "
    "selective deaths (genetic deaths). This limits the rate at which gene substitutions can "
    "occur by natural selection to roughly one substitution every 300 generations.",
    title="Haldane's cost of natural selection",
)


# === Research question ===

research_question = question(
    "Can the observed rate of molecular evolution (nucleotide substitutions) be explained "
    "by natural selection alone, or must most substitutions be selectively neutral?",
    title="Core question: selection vs neutrality",
)


# === Claims: Empirical observations of substitution rates ===

haemoglobin_rate = claim(
    "Comparative studies of haemoglobin molecules among different groups of mammals suggest "
    "that amino-acid substitution has taken place roughly at the rate of one amino-acid change "
    "in $10^7$ years for a chain consisting of about 140 amino acids. For example, by comparing "
    "the $\\alpha$ and $\\beta$ chains of man with those of horse, pig, cattle and rabbit, the "
    "figure of one amino-acid change in $7 \\times 10^6$ years was obtained (Zuckerkandl and "
    "Pauling, 1965).",
    title="Haemoglobin amino-acid substitution rate",
    metadata={"source": "artifacts/paper.pdf, p.624"},
)

cytochrome_c_rate = claim(
    "The rate of amino-acid substitution estimated by comparing gorilla and human "
    "cytochrome c (a chain of about 100 amino acids) turned out to be approximately one "
    "replacement in $4.5 \\times 10^7$ years.",
    title="Cytochrome c substitution rate",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

triosephosphate_rate = claim(
    "Comparing triosephosphate dehydrogenase of rabbit with that of other species yields "
    "a figure of at least one amino-acid substitution for every $2.5 \\times 10^7$ years "
    "for chains of about 1,110 amino acids. This figure is roughly equivalent to the rate "
    "of one amino-acid substitution in $2.8 \\times 10^7$ years for a chain consisting of "
    "100 amino acids.",
    title="Triosephosphate dehydrogenase substitution rate",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

dna_content_coding_fraction = claim(
    "Kimura estimated that the DNA content in terms of nucleotide pairs is at most a few "
    "per cent of the total for higher organisms. Taking the equivalent of about $10^7$ "
    "nucleotide pairs as coding for amino acids (a polypeptide chain of 100 amino acids "
    "corresponds to 300 nucleotide pairs), the evolutionary rate for the coding region "
    "appears to be very low for cytochrome c, but amounts to a very high rate for the "
    "entire genome when extrapolated.",
    title="DNA coding fraction estimate",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)
