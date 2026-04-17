"""Substitution Rate Calculation and Haldane's Cost Argument"""

from gaia.lang import claim, setting, support, induction

from .motivation import (
    haemoglobin_rate,
    cytochrome_c_rate,
    triosephosphate_rate,
    dna_content_coding_fraction,
    mammalian_genome_size,
    genetic_code_triplet,
    haldane_cost_principle,
)


# === Settings ===

mammalian_generation_time = setting(
    "For mammals, the average length of one generation varies by body size: roughly "
    "1-2 years for small mammals (mice, rabbits) and up to 20-30 years for large mammals "
    "(humans, elephants). Kimura uses an order-of-magnitude figure of a few years for "
    "the illustrative calculation comparing molecular rates with Haldane's cost limit.",
    title="Mammalian generation time (order of years)",
)


# === Claims: Genome-wide substitution rate calculation ===

normalized_aa_rate = claim(
    "Averaging figures for haemoglobin, cytochrome c, and triosephosphate dehydrogenase "
    "gives an evolutionary rate of approximately one amino-acid substitution in $28 \\times 10^6$ "
    "years (i.e., $2.8 \\times 10^7$ years) for a polypeptide chain of 100 amino acids.",
    title="Averaged amino-acid substitution rate across proteins",
    background=[haemoglobin_rate],
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

genome_substitution_rate = claim(
    "Extrapolating from the averaged amino-acid substitution rate to the whole genome, "
    "and noting that a polypeptide of 100 amino acids is coded by 300 nucleotide pairs, "
    "the rate of nucleotide substitution per genome per year is estimated as:\n\n"
    "$$k = \\frac{1}{2.8 \\times 10^7} \\times \\frac{4 \\times 10^9}{3 \\times 10^2} "
    "\\approx \\frac{1}{2}$$\n\n"
    "That is, approximately one nucleotide pair substitution in the population every 2 years, "
    "or equivalently about one substitution every 1.8 years across the entire mammalian genome.",
    title="Genome-wide nucleotide substitution rate (~1 per 2 yr)",
    background=[mammalian_genome_size, genetic_code_triplet, dna_content_coding_fraction],
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

selection_cannot_explain_rate = claim(
    "The observed rate of nucleotide substitution (approximately one per two years per "
    "mammalian genome) is so high that it cannot be accounted for by natural selection "
    "alone. Haldane (1957) showed that the cost of natural selection limits the rate of "
    "gene substitution by positive selection to roughly one every 300 generations. For "
    "mammals with generation times of a few years, 300 generations corresponds to "
    "hundreds to thousands of years. The observed molecular substitution rate is therefore "
    "100-1,000 times higher than this limit, meaning most nucleotide substitutions in "
    "evolution must not have been driven by positive natural selection.",
    title="Selection alone cannot explain the observed substitution rate",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)


# === Strategies ===

# Each protein comparison independently supports the averaged rate (induction pattern)
strat_hb_supports_rate = support(
    [haemoglobin_rate],
    normalized_aa_rate,
    reason=(
        "@haemoglobin_rate shows ~1 amino-acid change per $7 \\times 10^6$ yr for "
        "a 140-aa chain, which normalizes to approximately one substitution per "
        "$10^7$ yr for a 100-aa chain. This is one data point supporting the "
        "averaged rate of ~1 per $2.8 \\times 10^7$ yr."
    ),
    prior=0.9,
)

strat_cyto_supports_rate = support(
    [cytochrome_c_rate],
    normalized_aa_rate,
    reason=(
        "@cytochrome_c_rate shows ~1 substitution per $4.5 \\times 10^7$ yr for "
        "a ~100-aa chain. This is a second independent protein comparison supporting "
        "the averaged rate."
    ),
    prior=0.9,
)

strat_trio_supports_rate = support(
    [triosephosphate_rate],
    normalized_aa_rate,
    reason=(
        "@triosephosphate_rate shows ~1 substitution per $2.8 \\times 10^7$ yr for "
        "100 aa. This is a third independent protein comparison supporting the "
        "averaged rate."
    ),
    prior=0.9,
)

ind_hb_cyto = induction(
    strat_hb_supports_rate,
    strat_cyto_supports_rate,
    law=normalized_aa_rate,
    reason="Haemoglobin and cytochrome c are independent protein families.",
)

ind_all_proteins = induction(
    ind_hb_cyto,
    strat_trio_supports_rate,
    law=normalized_aa_rate,
    reason="Triosephosphate dehydrogenase is independent of haemoglobin and cytochrome c.",
)

strat_extrapolate_genome = support(
    [normalized_aa_rate],
    genome_substitution_rate,
    reason=(
        "From @normalized_aa_rate (one aa substitution per $2.8 \\times 10^7$ yr per 100 aa chain), "
        "the genome-wide nucleotide substitution rate is obtained by: "
        "(1) converting amino-acid rate to nucleotide rate (each aa = 3 nucleotides), "
        "(2) scaling from the coding region of one polypeptide to the whole genome "
        "($4 \\times 10^9$ nucleotide pairs). "
        "This gives $k \\approx 1/(2.8 \\times 10^7) \\times (4 \\times 10^9)/(3 \\times 10^2) "
        "\\approx 0.5$ substitutions per year, or about one substitution every 2 years."
    ),
    prior=0.8,
    background=[mammalian_genome_size, genetic_code_triplet],
)

strat_selection_fails = support(
    [genome_substitution_rate],
    selection_cannot_explain_rate,
    reason=(
        "The genome-wide substitution rate (@genome_substitution_rate) of ~1 per 2 years "
        "vastly exceeds the limit imposed by Haldane's cost of natural selection. "
        "Haldane (1957) estimated that gene substitution by natural selection requires ~30 "
        "selective deaths per substitution, limiting the rate to ~1 gene substitution per "
        "300 generations. For mammals with generation times of a few years, this translates "
        "to at most one substitution every several hundred years. The observed rate exceeds "
        "this limit by 2-3 orders of magnitude."
    ),
    prior=0.9,
    background=[haldane_cost_principle, mammalian_generation_time],
)
