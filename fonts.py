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
# MATHEMATICAL_SCRIPT = []

# with open("fonts/mathematical_bold_italic.json", "w") as f:
#     json.dump(MATHEMATICAL_BOLD_ITALIC, f)
