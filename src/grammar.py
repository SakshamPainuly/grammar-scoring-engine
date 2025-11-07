import re

def grammar_score(text: str):
    """
    Simple grammar scoring without Java or LanguageTool.
    Uses basic heuristics:
    - Detect repeated words
    - Detect missing capitalization
    - Detect very short sentences
    - Detect double spaces, punctuation issues
    """

    diagnostics = []
    errors = 0

    # 1. Capitalization check
    if text and not text[0].isupper():
        errors += 1
        diagnostics.append("Sentence should start with a capital letter.")

    # 2. Double spaces
    if "  " in text:
        errors += 1
        diagnostics.append("Contains double spaces.")

    # 3. Repeated words
    words = text.lower().split()
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            errors += 1
            diagnostics.append(f"Repeated word: '{words[i]}'.")

    # 4. Missing punctuation (very simple)
    if text and text[-1] not in ".?!":
        errors += 1
        diagnostics.append("Sentence should end with punctuation.")

    # 5. Short sentence check
    if len(words) < 3:
        errors += 1
        diagnostics.append("Sentence too short, clarity may be low.")

    # Convert errors to score
    score = max(0, 100 - errors * 10)

    return score, diagnostics
