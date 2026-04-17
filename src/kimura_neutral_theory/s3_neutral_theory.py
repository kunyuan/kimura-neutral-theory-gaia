"""The Neutral Theory: Hypothesis and Population Genetics"""

from gaia.lang import claim, setting, contradiction, support, deduction, compare, abduction

from .motivation import mammalian_genome_size
from .s2_rate_calculation import selection_cannot_explain_rate, genome_substitution_rate


# === The Core Hypothesis ===

neutral_theory_hypothesis = claim(
    "Most mutations produced by nucleotide replacement are almost neutral in natural "
    "selection, meaning they have so little effect on the fitness of the organism that "
    "their fate in the population is determined primarily by random genetic drift rather "
    "than by selection. The very high rate of nucleotide substitution observed at the "
    "molecular level can be explained if most substitutions are the result of random "
    "fixation of selectively neutral or nearly neutral mutations.",
    title="Neutral theory: most molecular substitutions are selectively neutral",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)

selectionist_view = claim(
    "The conventional (selectionist) view holds that most molecular evolution is driven "
    "by positive natural selection: each amino-acid or nucleotide substitution that "
    "becomes fixed in a population does so because it confers a selective advantage. "
    "Under this view, the substitution rate is limited by Haldane's cost of natural "
    "selection.",
    title="Selectionist view: substitutions driven by positive selection",
)

not_both_views = contradiction(
    neutral_theory_hypothesis,
    selectionist_view,
    reason=(
        "If most substitutions are selectively neutral (neutral theory), then most "
        "substitutions are NOT driven by positive natural selection (selectionist view), "
        "and vice versa. These two explanations for the dominant mode of molecular "
        "evolution are mutually exclusive."
    ),
    prior=0.95,
)


# === Neutral substitution rate formula ===

neutral_substitution_formula = claim(
    "For neutral mutations, the rate of mutant substitution in the population (the rate at "
    "which new alleles become fixed) is:\n\n"
    "$$k = u$$\n\n"
    "where $u$ is the mutation rate per gamete per generation. This result holds because "
    "the probability that a new neutral mutation eventually becomes fixed in a population "
    "of effective size $N_e$ is $1/(2N_e)$, and the number of new neutral mutations appearing "
    "each generation is $2N_e u$. Multiplying these: $k = 2N_e u \\times \\frac{1}{2N_e} = u$. "
    "This is independent of population size.",
    title="Neutral substitution rate equals mutation rate (k = u)",
    metadata={"source": "artifacts/paper.pdf, p.625, formula (1)"},
)

neutral_fixation_probability = claim(
    "For a selectively neutral mutation in a diploid population of effective size $N_e$, "
    "the probability of eventual fixation is $p = 1/(2N_e)$, which equals the initial "
    "frequency of the new allele if it appears as a single copy.",
    title="Fixation probability of a neutral allele is 1/(2Ne)",
    metadata={"source": "artifacts/paper.pdf, p.625"},
)


# === Heterozygosity and effective population size ===

heterozygosity_formula = claim(
    "Kimura and Crow (1964) showed that for neutral mutations, the probability that a "
    "randomly chosen individual is homozygous at a locus is $1/(4N_e u + 1)$, where $N_e$ "
    "is the effective population number and $u$ is the mutation rate per locus per generation. "
    "Therefore, the expected heterozygosity is:\n\n"
    "$$H_e = \\frac{4 N_e u}{4 N_e u + 1}$$\n\n"
    "To attain a heterozygosity of at least $H_e = 0.12$, it is necessary that "
    "$N_e \\geq 2{,}300$. For a higher heterozygosity such as $H_e = 0.35$, $N_e$ must "
    "be about $8{,}000$.",
    title="Neutral heterozygosity depends on 4*Ne*u (Kimura-Crow 1964)",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

drosophila_heterozygosity = claim(
    "For Drosophila, with migration between subgroups, heterozygosity of 35 per cent "
    "may be attained even if the effective population size $N_e$ is much smaller for "
    "each subgroup. This is consistent with the neutral theory's prediction that "
    "heterozygosity is maintained by the balance between neutral mutation and random "
    "genetic drift.",
    title="Drosophila heterozygosity consistent with neutral prediction",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)


# === Strategies ===

# Direct support: if selection can't explain the rate, the neutral theory is supported
strat_rate_supports_neutral = support(
    [selection_cannot_explain_rate],
    neutral_theory_hypothesis,
    reason=(
        "If natural selection alone cannot account for the observed rate of molecular "
        "evolution (@selection_cannot_explain_rate), then an alternative mechanism must "
        "be responsible. The neutral theory provides this mechanism: random fixation of "
        "selectively neutral mutations at a rate equal to the mutation rate (k=u)."
    ),
    prior=0.9,
)

# The neutral substitution formula k=u is derived from the fixation probability
strat_derive_k_equals_u = deduction(
    [neutral_fixation_probability],
    neutral_substitution_formula,
    reason=(
        "Starting from @neutral_fixation_probability ($p = 1/(2N_e)$ for a neutral mutation), "
        "the substitution rate is obtained by multiplying the fixation probability by the "
        "number of new mutations per generation ($2N_e u$): "
        "$k = 2N_e u \\times 1/(2N_e) = u$. The population size cancels, "
        "yielding the result that the substitution rate equals the mutation rate."
    ),
    prior=0.99,
)

# The heterozygosity formula is a prediction of the neutral theory
strat_heterozygosity_prediction = support(
    [neutral_theory_hypothesis],
    heterozygosity_formula,
    reason=(
        "Under the neutral theory (@neutral_theory_hypothesis), most polymorphism "
        "is selectively neutral and maintained by the balance of mutation and drift. "
        "Kimura and Crow (1964) derived that for neutral alleles, expected heterozygosity "
        "is $H_e = 4N_e u / (4N_e u + 1)$, depending only on the product of effective "
        "population size and mutation rate."
    ),
    prior=0.85,
)

# Drosophila data is consistent with the heterozygosity prediction
strat_drosophila_het = support(
    [heterozygosity_formula],
    drosophila_heterozygosity,
    reason=(
        "The neutral heterozygosity formula (@heterozygosity_formula) predicts that "
        "Drosophila populations with moderate effective sizes and subdivision (migration "
        "between subgroups) can attain 35% heterozygosity. This is consistent with "
        "observed levels of protein polymorphism in Drosophila."
    ),
    prior=0.8,
)

# --- Abduction: Neutral theory vs selectionist view explaining the observed rate ---

# The neutral theory predicts that substitution rate = mutation rate (k=u),
# which naturally explains the high observed rate
neutral_predicts_rate = claim(
    "Under the neutral theory, the substitution rate equals the mutation rate ($k = u$), "
    "which for mammals with ~$4 \\times 10^9$ nucleotide pairs and error rates of "
    "$10^{-8}$ to $10^{-9}$ per nucleotide per replication, predicts a genome-wide "
    "substitution rate on the order of one per few years. This matches the observed "
    "rate of ~1 substitution per 2 years.",
    title="Neutral theory predicts the observed high substitution rate",
)

selectionist_predicts_rate = claim(
    "Under the selectionist view, the substitution rate is limited by Haldane's cost "
    "of natural selection to roughly one gene substitution every 300 generations. For "
    "mammals, this predicts a far lower rate than the observed ~1 substitution per 2 years, "
    "a discrepancy of 2-3 orders of magnitude.",
    title="Selectionist view predicts a much lower substitution rate",
)

strat_neutral_explains = support(
    [neutral_theory_hypothesis, neutral_substitution_formula],
    neutral_predicts_rate,
    reason=(
        "Under @neutral_theory_hypothesis, most substitutions are neutral. "
        "The neutral substitution formula (@neutral_substitution_formula) gives $k = u$. "
        "Since the per-nucleotide mutation rate times the genome size yields ~1 substitution "
        "per few years, the neutral theory naturally predicts the observed high rate."
    ),
    prior=0.9,
)

strat_selectionist_predicts = support(
    [selectionist_view],
    selectionist_predicts_rate,
    reason=(
        "Under @selectionist_view, substitutions require positive selection. "
        "Haldane's cost argument limits positive selection to ~1 substitution per 300 "
        "generations. For mammals this is far below the observed rate of ~1 per 2 years."
    ),
    prior=0.5,
    background=[selection_cannot_explain_rate],
)

comp_neutral_vs_selectionist = compare(
    neutral_predicts_rate,
    selectionist_predicts_rate,
    genome_substitution_rate,
    reason=(
        "The observed genome-wide substitution rate is ~1 per 2 years "
        "(@genome_substitution_rate). The neutral theory predicts a rate on this order "
        "(@neutral_predicts_rate), while the selectionist view predicts a rate 100-1,000x "
        "lower (@selectionist_predicts_rate). The neutral theory's prediction matches "
        "the observation far better."
    ),
    prior=0.9,
)

abd_neutral_vs_selectionist = abduction(
    strat_neutral_explains,
    strat_selectionist_predicts,
    comp_neutral_vs_selectionist,
    reason=(
        "Both the neutral theory and the selectionist view attempt to explain the "
        "observed genome-wide nucleotide substitution rate. The neutral theory correctly "
        "predicts the high rate via $k = u$, while the selectionist view predicts a rate "
        "orders of magnitude too low due to Haldane's cost constraint."
    ),
)
