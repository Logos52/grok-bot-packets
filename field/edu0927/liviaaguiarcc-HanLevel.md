# HanLevel (no README — fetched analyzer.py + description)
Desc: Know if a Korean text is right for your level — and understand why.

## turns the linguistic labels into numbers
## calculates HanLevel's difficulty scores

from kiwipiepy import Kiwi
from krdict import lookup_word

kiwi = Kiwi()

GRADE_SCORES  = {
    "초급": 0,
    "중급": 50,
    "고급": 100
}

# Kiwi POS → Korean Learners' Dictionary POS code
KIWI_TO_KRDICT_POS = {
    "NNG": 1,   # common noun → 명사
    "NNB": 11,  # dependent noun → 의존 명사
    "NP": 2,    # pronoun → 대명사
    "NR": 3,    # numeral → 수사

    "VV": 5,    # verb → 동사
    "VA": 6,    # adjective → 형용사

    "MM": 7,    # determiner → 관형사
    "MAG": 8,   # adverb → 부사
    "MAJ": 8,   # conjunctive adverb → 부사
    "IC": 9,    # interjection → 감탄사
}

# Convert Kiwi output into kr dictionary citation forms.
def normalize_lemma(form, tag):
    if tag in {"VV", "VA"}:
        return form + "다"

    return form

# Extract lexical vocabulary from Korean text.
# Grammar markers, particles and endings are excluded because     they will belong to HanLevel's grammar component.
def extract_vocabulary(text):
    tokens = kiwi.tokenize(text)
    vocabulary = []

    for token in tokens:
        tag = token.tag

        if tag == "NNP":
            continue
        if tag not in KIWI_TO_KRDICT_POS:
            continue

        lemma = normalize_lemma(token.form, tag)

        vocabulary.append(
            {
                "lemma": lemma,
                "kiwi_pos":tag,
                "krdict_pos": KIWI_TO_KRDICT_POS[tag],
            }
        )

    return vocabulary

# Choose a grade when the dictionary return one or more entries.
def choose_grade(results):
    grades = [
        result["grade"]
        for result in results
        if result["grade"] in GRADE_SCORES
    ]

    if not grades:
        return None

    return min(
        grades,
        key=lambda grade: GRADE_SCORES[grade]
    )


