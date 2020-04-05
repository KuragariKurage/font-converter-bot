import json

CAPITAL_A = 65  # \u0041
SMALL_A = 97  # \u0061


def gen_font_map(cap_a_ord, sm_a_ord):
    d = {chr(CAPITAL_A + i): chr(cap_a_ord + i) for i in range(26)}
    for i in range(26):
        s = SMALL_A + i
        d[chr(s)] = chr(sm_a_ord + i)

    return d


MATHEMATICAL_BOLD = gen_font_map(119808, 119834)
MATHEMATICAL_ITALIC = gen_font_map(119860, 119886)
MATHEMATICAL_ITALIC["h"] = "\u210E"
MATHEMATICAL_BOLD_ITALIC = gen_font_map(119912, ord("\U0001D482"))
SCRIPT_SYMBOLS = gen_font_map(119964, 119990)
SCRIPT_SYMBOLS["B"] = "\u212C"
SCRIPT_SYMBOLS["E"] = "\u2130"
SCRIPT_SYMBOLS["F"] = "\u2131"
SCRIPT_SYMBOLS["H"] = "\u210b"
SCRIPT_SYMBOLS["I"] = "\u2110"
SCRIPT_SYMBOLS["L"] = "\u2112"
SCRIPT_SYMBOLS["M"] = "\u2133"
SCRIPT_SYMBOLS["R"] = "\u211b"
SCRIPT_SYMBOLS["e"] = "\u212f"
SCRIPT_SYMBOLS["g"] = "\u210a"
SCRIPT_SYMBOLS["o"] = "\u2134"
# MATHEMATICAL_SCRIPT = []

with open("fonts/script.json", "w") as f:
    json.dump(SCRIPT_SYMBOLS, f)
