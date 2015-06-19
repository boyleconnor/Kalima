ROOT_LENGTH_CHOICES = (
    (3, 'Three'),
    (4, 'Four')
)

DEFAULT_ROOT_SPELLING = 'فعل'

FATHA = 'َ'

KASRA = 'ِ'

DAMMA = 'ُ'

SHADDA = 'ّ'

SUKUN = 'ْ'

TASHKEEL = FATHA + KASRA + DAMMA + SHADDA + SUKUN

FATHAN = 'ً'

KASRAN = 'ٍ'

DAMMAN = 'ٌ'

TANWEEN = FATHAN + KASRAN + DAMMAN

DIACRITICS = TASHKEEL + TANWEEN

ALIF = 'ا'

BAA = 'ب'

TAA = 'ت'

THAA = 'ث'

JIM = 'ج'

HHAA = 'ح'

XAA = 'خ'

DAL = 'د'

DHAL = 'ذ'

RAA = 'ر'

ZAYN = 'ز'

SIN = 'س'

SHIN = 'ش'

SAD = 'ص'

DAD = 'ض'

TTAA = 'ط'

ZZAA = 'ظ'

EIN = 'ع'

GHAIN = 'غ'

FAA = 'ف'

QAF = 'ق'

KAF = 'ك'

LAM = 'ل'

MIM = 'م'

NUN = 'ن'

HAA = 'ه'

WAW = 'و'

YAA = 'ي'

HAMZA = 'ء'

TAA_MARBUTA = 'ة'

ALIF_MAQSURA = 'ى'

VOWELS = ALIF + WAW + YAA + ALIF_MAQSURA

CONSONANTS = BAA + TAA + THAA + JIM + HHAA + XAA + DAL + DHAL + RAA + ZAYN + SIN + SHIN + SAD + DAD + TTAA + ZZAA + EIN + GHAIN + FAA + QAF + KAF + LAM + MIM + NUN + HAA + HAMZA + TAA_MARBUTA

SOUND_LETTERS = BAA + TAA + THAA + JIM + HHAA + XAA + DAL + DHAL + RAA + ZAYN + SIN + SHIN + SAD + DAD + TTAA + ZZAA + EIN + GHAIN + FAA + QAF + KAF + LAM + MIM + NUN + HAA

ABJAD = VOWELS + CONSONANTS

ARABIC_CHARACTERS = ABJAD + DIACRITICS

POS_CHOICES = (
    ('noun', 'Noun'),
    ('verb', 'Verb'),
    ('adjective', 'Adjective'),
    ('preposition', 'Preposition'),
    ('root', 'Root')
)

ALLOWED_INFLECTION_ATTRIBUTES = {
    'adjective': ('case', 'number', 'state', 'gender'),
    'noun': ('case', 'number', 'state'),
    'verb': ('gender', 'number', 'person', 'tense', 'voice'),
}

ALLOWED_INFLECTION_ATTRIBUTE_VALUES = {
    'case': (
        'nominative',
        'genitive',
        'accusative'
    ),
    'gender': (
        'masculine',
        'feminine'
    ),
    'number': (
        'singular',
        'dual',
        'plural'
    ),
    'state': (
        'construct',
        'definite',
        'indefinite',
    ),
    'person': (
        'first',
        'second',
        'third'
    ),
    'tense': (
        'perfect',
        'indicative-imperfect',
        'subjunctive-imperfect',
        'jussive-imperfect',
        'imperative'
    ),
    'voice': (
        'active',
        'passive'
    )
}

ARABIC_LANGUAGE_CODE = 'ar'

ENGLISH_LANGUAGE_CODE = 'en'

ARABIZI = {
    FATHA: 'a',
    KASRA: 'i',
    DAMMA: 'u',
    SHADDA: '-',
    SUKUN: '',
    FATHAN: 'an',
    KASRAN: 'in',
    DAMMAN: 'un',
    ALIF: '-',
    BAA: 'b',
    TAA: 't',
    THAA: 'tv',
    JIM: 'j',
    HHAA: '7',
    XAA: 'kv',
    DAL: 'd',
    DHAL: 'dv',
    RAA: 'r',
    ZAYN: 'z',
    SIN: 's',
    SHIN: 'sh',
    SAD: 'S',
    DAD: 'D',
    TTAA: 'T',
    ZZAA: 'Dv',
    EIN: '3',
    GHAIN: 'gv',
    FAA: 'f',
    QAF: 'q',
    KAF: 'k',
    LAM: 'l',
    MIM: 'm',
    NUN: 'n',
    HAA: 'h',
    WAW: 'w',
    YAA: 'y',
    HAMZA: '2',
    TAA_MARBUTA: 'h',
}