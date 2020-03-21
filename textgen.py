def transform(text, ch_type):
    symbols = getattr(__import__("fonts"), ch_type)
    return "".join([symbols[t]
                    if t in symbols.keys() else t for t in text])


if __name__ == "__main__":
    print(transform("Test", "MATHEMATICAL_BOLD"))
    print(transform("Test", "MATHEMATICAL_ITALIC"))
    print(transform("Test test TEst", "MATHEMATICAL_BOLD"))
    print(transform("This is the Test, right?", "MATHEMATICAL_BOLD"))
    print(transform("おまえらfuckin goodだぜ", "MATHEMATICAL_BOLD_ITALIC"))

    print(transform("ABCabc", "MATHEMATICAL_BOLD"))
    print(transform("ABCabc", "MATHEMATICAL_ITALIC"))
    print(transform("ABCabc", "MATHEMATICAL_BOLD_ITALIC"))
