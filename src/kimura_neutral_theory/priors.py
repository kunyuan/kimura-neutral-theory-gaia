"""Leaf claim priors — package input interface.

Each entry maps a leaf claim (not derived by any strategy) to its
prior probability and a one-line justification.  These are injected
into claim metadata by ``gaia compile`` and read by the lowering
layer during inference.
"""

from .motivation import (
    haemoglobin_rate,
    cytochrome_c_rate,
    triosephosphate_rate,
)
from .s3_neutral_theory import (
    neutral_theory_hypothesis,
    selectionist_view,
    neutral_fixation_probability,
    neutral_predicts_rate,
    selectionist_predicts_rate,
)
from .s4_mutation_rates import (
    watson_mutation_rate,
    cell_divisions_to_gamete,
)

PRIORS: dict = {
    # === Empirical protein substitution rates ===
    haemoglobin_rate: (
        0.92,
        "Well-established comparative data from Zuckerkandl & Pauling (1965), "
        "confirmed by decades of subsequent molecular evolution studies.",
    ),
    cytochrome_c_rate: (
        0.90,
        "Gorilla-human cytochrome c comparison; highly conserved protein, "
        "rate estimate consistent with later studies.",
    ),
    triosephosphate_rate: (
        0.85,
        "Less well-characterized than haemoglobin at time of publication, "
        "but broadly consistent with later molecular clock data.",
    ),

    # === Population genetics theoretical result ===
    neutral_fixation_probability: (
        0.95,
        "Standard result in population genetics, derived rigorously by "
        "Kimura (1962) using diffusion theory.",
    ),

    # === Core competing hypotheses — uninformative priors ===
    neutral_theory_hypothesis: (
        0.5,
        "Central hypothesis of the paper; novel and controversial in 1968. "
        "Uninformative prior lets the abduction evidence determine posterior.",
    ),
    selectionist_view: (
        0.5,
        "Prevailing view in 1968. Symmetric uninformative prior with the "
        "neutral theory hypothesis.",
    ),

    # === Mutation rate data ===
    watson_mutation_rate: (
        0.80,
        "Watson (1965) estimate based on hydrogen bond energetics and phage T4 data; "
        "range spans an order of magnitude (10^-8 to 10^-9), substantial uncertainty.",
    ),
    cell_divisions_to_gamete: (
        0.88,
        "Well-known figure in developmental biology (~50 divisions from "
        "fertilized egg to gamete in humans); reasonable order-of-magnitude estimate.",
    ),

    # === Theory predictions (used in compare/abduction) ===
    neutral_predicts_rate: (
        0.90,
        "Straightforward mathematical consequence of k=u and known genome size / "
        "mutation rate. If the neutral theory holds, this prediction follows directly.",
    ),
    selectionist_predicts_rate: (
        0.85,
        "Follows from Haldane's cost calculation. The math is well-established; "
        "uncertainty is in whether Haldane's cost model fully captures selection dynamics.",
    ),
}
