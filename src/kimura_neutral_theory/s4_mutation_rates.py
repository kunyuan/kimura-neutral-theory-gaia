"""Mutation Rate Estimation and Comparison with Molecular Rates"""

from gaia.lang import claim, setting, support

from .motivation import mammalian_genome_size
from .s3_neutral_theory import neutral_substitution_formula


# === Mutation rate data ===

watson_mutation_rate = claim(
    "From a consideration of the average energy of hydrogen bonds and from information on "
    "mutation of rIIA gene in phage T4, Watson (1965) obtained $10^{-8}$ to $10^{-9}$ as "
    "the average probability of error in the insertion of a new nucleotide during DNA "
    "replication.",
    title="Watson's estimate of nucleotide misincorporation rate",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

cell_divisions_to_gamete = claim(
    "In man, the number of cell divisions along the germ line from the fertilized egg "
    "to a gamete is roughly 50.",
    title="~50 cell divisions from zygote to gamete in humans",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

mammalian_mutation_rate_per_nucleotide = claim(
    "The rate of mutation resulting from base replacement is estimated as "
    "$50 \\times 10^{-8}$ to $50 \\times 10^{-9}$ per nucleotide pair per generation "
    "(i.e., $5 \\times 10^{-7}$ to $5 \\times 10^{-8}$). With approximately "
    "$4 \\times 10^9$ nucleotide pairs in the mammalian haploid genome, the total number "
    "of mutations resulting from base replacement per generation may amount to "
    "$200$ to $2{,}000$.",
    title="Total base-replacement mutations per generation: 200-2000",
    background=[mammalian_genome_size],
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

drosophila_mutation_rate = claim(
    "The mutation rate per nucleotide pair per generation in Drosophila is roughly ten "
    "times as high as in man (i.e., $u \\approx 1.5 \\times 10^{-7}$ rather than "
    "$u \\approx 1.5 \\times 10^{-8}$). Another consideration allows the supposition "
    "that $u \\approx 1.5 \\times 10^{-7}$ is probably appropriate for the neutral "
    "mutation rate of a cistron in Drosophila.",
    title="Drosophila neutral mutation rate per nucleotide",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

neutral_rate_consistency = claim(
    "The estimated total mutation rate per generation (200-2,000 base-replacement mutations) "
    "is 100-1,000 times larger than the rate of approximately 2 substitutions per generation "
    "allowed by Haldane's natural selection cost. This is consistent with the neutral theory's "
    "prediction that the mutation rate per nucleotide per generation directly determines the "
    "substitution rate ($k = u$), because neutral mutations fix at a rate equal to the "
    "mutation rate regardless of population size.",
    title="Mutation rate is 100-1000x Haldane's limit, consistent with neutral theory",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)


# === Strategies ===

strat_mutation_per_nucleotide = support(
    [watson_mutation_rate, cell_divisions_to_gamete],
    mammalian_mutation_rate_per_nucleotide,
    reason=(
        "Watson's estimate of nucleotide misincorporation rate (@watson_mutation_rate) is "
        "$10^{-8}$ to $10^{-9}$ per nucleotide per replication. With approximately 50 cell "
        "divisions from zygote to gamete (@cell_divisions_to_gamete), the per-nucleotide "
        "per-generation mutation rate is $50 \\times 10^{-8}$ to $50 \\times 10^{-9}$. "
        "Multiplying by the genome size ($4 \\times 10^9$ nucleotide pairs) yields 200-2,000 "
        "total base-replacement mutations per generation."
    ),
    prior=0.8,
    background=[mammalian_genome_size],
)

strat_drosophila_rate = support(
    [mammalian_mutation_rate_per_nucleotide],
    drosophila_mutation_rate,
    reason=(
        "The mutation rate per nucleotide pair per generation in Drosophila is estimated "
        "to be roughly ten times as high as in man (@mammalian_mutation_rate_per_nucleotide), "
        "because the mutation rate per nucleotide pair per generation in Drosophila is "
        "roughly ten times that of man. This gives $u \\approx 1.5 \\times 10^{-7}$ "
        "per nucleotide per generation for Drosophila, compared to "
        "$u \\approx 1.5 \\times 10^{-8}$ in man."
    ),
    prior=0.75,
)

strat_neutral_consistency = support(
    [mammalian_mutation_rate_per_nucleotide, neutral_substitution_formula],
    neutral_rate_consistency,
    reason=(
        "The total mutation rate of 200-2,000 per generation "
        "(@mammalian_mutation_rate_per_nucleotide) is 100-1,000 times larger than "
        "Haldane's limit of ~2 substitutions per generation by natural selection. "
        "However, under the neutral substitution formula (@neutral_substitution_formula, "
        "$k = u$), the fixation rate equals the mutation rate regardless of population "
        "size. This means the high mutation rate directly predicts a high substitution "
        "rate, consistent with the observed molecular evolutionary rate."
    ),
    prior=0.85,
)
