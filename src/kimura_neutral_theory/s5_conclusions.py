"""Conclusions: Implications for Genetic Drift and Population Genetics"""

from gaia.lang import claim, support

from .s3_neutral_theory import neutral_theory_hypothesis
from .s4_mutation_rates import neutral_rate_consistency


# === Conclusions ===

genetic_drift_importance = claim(
    "If the main conclusion is correct (that neutral or nearly neutral mutations are "
    "being produced in each generation at a much higher rate than has been considered "
    "before), then we must recognize the great importance of random genetic drift due "
    "to finite population number in forming the genetic structure of biological "
    "populations. The significance of random genetic drift has been depreciated during "
    "the past decade, influenced by the opinion that almost no mutations are neutral "
    "and that population sizes are usually so large that random sampling of gametes "
    "should be negligible.",
    title="Random genetic drift must be recognized as important",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)

founder_principle_inadequate = claim(
    "To emphasize the founder principle but deny the importance of random genetic drift "
    "due to finite population number is, in Kimura's opinion, rather similar to "
    "assuming a great flood to explain the formation of deep valleys but rejecting "
    "a gradual but long lasting process of erosion by water as insufficient to produce "
    "such a result.",
    title="Denying drift while accepting founder effect is inconsistent",
    metadata={"source": "artifacts/paper.pdf, p.626"},
)


# === Strategies ===

strat_drift_importance = support(
    [neutral_theory_hypothesis, neutral_rate_consistency],
    genetic_drift_importance,
    reason=(
        "If the neutral theory (@neutral_theory_hypothesis) is correct, then neutral "
        "mutations are produced at a much higher rate than previously assumed "
        "(@neutral_rate_consistency shows 200-2,000 mutations per generation, 100-1,000x "
        "above Haldane's limit). Since these neutral mutations fix by random drift, not "
        "selection, random genetic drift must be the dominant force shaping molecular "
        "evolution and maintaining polymorphism in populations. This contradicts the "
        "prevailing view that drift is negligible due to large population sizes."
    ),
    prior=0.85,
)

strat_founder_inconsistency = support(
    [genetic_drift_importance],
    founder_principle_inadequate,
    reason=(
        "If random genetic drift is important for ongoing molecular evolution "
        "(@genetic_drift_importance), then it is logically inconsistent to accept "
        "the founder principle (which invokes drift in small founding populations) "
        "while simultaneously denying the importance of drift in normal populations "
        "of finite size. Both phenomena arise from the same stochastic sampling process."
    ),
    prior=0.9,
)
