from gaia.review import ReviewBundle, review_claim, review_generated_claim

from ..motivation import (
    haemoglobin_rate,
    cytochrome_c_rate,
    triosephosphate_rate,
)
from ..s3_neutral_theory import (
    neutral_theory_hypothesis,
    selectionist_view,
    neutral_fixation_probability,
    abd_neutral_vs_selectionist,
)
from ..s4_mutation_rates import (
    watson_mutation_rate,
    cell_divisions_to_gamete,
)


REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # === Independent premises (leaf claims needing priors) ===

        # Empirical observations from protein comparisons
        review_claim(
            haemoglobin_rate,
            prior=0.92,
            judgment="supporting",
            justification=(
                "Well-established comparative molecular data from Zuckerkandl and Pauling "
                "(1965), based on multiple mammalian species. The rate of ~1 amino-acid "
                "change per 7-10 million years for haemoglobin chains is a robust finding "
                "confirmed by decades of subsequent molecular evolution studies."
            ),
        ),
        review_claim(
            cytochrome_c_rate,
            prior=0.90,
            judgment="supporting",
            justification=(
                "Based on comparing gorilla and human cytochrome c sequences. "
                "Cytochrome c is highly conserved, and the rate estimate of ~1 change "
                "per 45 million years for 100 aa is consistent with later studies."
            ),
        ),
        review_claim(
            triosephosphate_rate,
            prior=0.85,
            judgment="supporting",
            justification=(
                "Based on triosephosphate dehydrogenase comparisons. Less well-characterized "
                "than haemoglobin at the time of publication, but the rate estimate is "
                "broadly consistent with later molecular clock data."
            ),
        ),

        # Population genetics theoretical result
        review_claim(
            neutral_fixation_probability,
            prior=0.95,
            judgment="supporting",
            justification=(
                "The fixation probability of 1/(2Ne) for a neutral allele is a standard "
                "result in population genetics, derived rigorously by Kimura (1962) using "
                "diffusion theory. This is a well-established mathematical result."
            ),
        ),

        # Core competing hypotheses -- uninformative priors
        review_claim(
            neutral_theory_hypothesis,
            prior=0.5,
            judgment="tentative",
            justification=(
                "This is the central hypothesis of the paper. At the time of publication "
                "(1968), it was a novel and controversial proposal. Assigning an "
                "uninformative prior of 0.5 to let the evidence (abduction, rate "
                "calculations) determine the posterior belief."
            ),
        ),
        review_claim(
            selectionist_view,
            prior=0.5,
            judgment="tentative",
            justification=(
                "The prevailing view in 1968. Given uninformative prior of 0.5, symmetric "
                "with the neutral theory hypothesis, so BP can determine which view is "
                "better supported by the molecular rate evidence."
            ),
        ),

        # Mutation rate data
        review_claim(
            watson_mutation_rate,
            prior=0.80,
            judgment="tentative",
            justification=(
                "Watson's (1965) estimate of nucleotide misincorporation rate (10^-8 to "
                "10^-9 per nucleotide per replication) was based on indirect evidence from "
                "hydrogen bond energetics and phage T4 data. The range spans an order of "
                "magnitude, reflecting substantial uncertainty. Later measurements confirmed "
                "the order of magnitude."
            ),
        ),
        review_claim(
            cell_divisions_to_gamete,
            prior=0.88,
            judgment="supporting",
            justification=(
                "The estimate of ~50 cell divisions from fertilized egg to gamete in humans "
                "is a well-known figure in developmental biology. A reasonable "
                "order-of-magnitude estimate."
            ),
        ),

        # === Abduction alternative: selectionist view's explanatory power ===
        review_generated_claim(
            abd_neutral_vs_selectionist,
            "alternative_explanation",
            prior=0.15,
            judgment="opposing",
            justification=(
                "The selectionist view predicts a substitution rate limited by Haldane's "
                "cost to ~1 per 300 generations. The observed rate is ~1 per 2 years, "
                "a discrepancy of 100-1000x. The selectionist view CANNOT explain this "
                "specific observation (the high genome-wide substitution rate) without "
                "abandoning Haldane's cost principle. Therefore pi(Alt) is very low -- "
                "not because the selectionist view is wrong in general, but because it "
                "cannot account for this specific rate observation."
            ),
        ),
    ],
)
