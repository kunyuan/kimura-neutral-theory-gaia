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
    "For mammals, the average generation time is on the order of years (e.g., roughly "
    "1 year for small mammals, longer for large mammals). Kimura uses an approximate figure "
    "for illustrative calculation.",
    title="Mammalian generation time",
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

haldane_limit_for_mammals = claim(
    "If we assume that the cost of natural selection per generation is about 0.1 "
    "(Haldane, 1957), and that a new allele is substituted by natural selection roughly "
    "every 300 generations, then for mammals with approximately $4 \\times 10^9$ nucleotide "
    "pairs and generation times of a few years, the total number of substitutions attributable "
    "to selection would be far fewer than one per two years. "
    "Haldane's formula gives approximately one gene substitution every 300 generations. "
    "The actual rate of nucleotide substitution estimated from protein data is roughly "
    "one substitution every 2 years per genome, which is vastly higher than the selection limit.",
    title="Haldane's cost limits substitution rate far below observed rate",
    background=[haldane_cost_principle, mammalian_generation_time],
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

selection_cannot_explain_rate = claim(
    "The observed rate of nucleotide substitution (approximately one per two years per "
    "mammalian genome) is so high that it cannot be accounted for by natural selection "
    "alone. Haldane's cost of natural selection limits the rate of gene substitution by "
    "positive selection to roughly one every 300 generations. The observed molecular "
    "substitution rate is 100-1,000 times higher than this limit. Therefore, most "
    "nucleotide substitutions in evolution must not have been driven by positive natural "
    "selection.",
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

strat_haldane_limit = support(
    [genome_substitution_rate],
    haldane_limit_for_mammals,
    reason=(
        "The observed genome-wide substitution rate from @genome_substitution_rate "
        "(~1 substitution per 2 years) is compared with Haldane's theoretical limit "
        "of ~1 gene substitution per 300 generations. For mammals with generation times "
        "of a few years, 300 generations corresponds to hundreds of years. The observed "
        "molecular rate is therefore 100-1,000 times higher than what natural selection "
        "can sustain according to Haldane's cost argument."
    ),
    prior=0.9,
    background=[haldane_cost_principle, mammalian_generation_time],
)

strat_selection_fails = support(
    [genome_substitution_rate, haldane_limit_for_mammals],
    selection_cannot_explain_rate,
    reason=(
        "The genome-wide substitution rate (@genome_substitution_rate) of ~1 per 2 years "
        "vastly exceeds the limit imposed by the cost of natural selection "
        "(@haldane_limit_for_mammals). Since Haldane's argument sets an upper bound on how "
        "many substitutions natural selection can drive per generation, and the observed "
        "molecular rate exceeds that bound by 2-3 orders of magnitude, it follows that "
        "natural selection alone cannot account for the observed rate of molecular evolution."
    ),
    prior=0.9,
)
