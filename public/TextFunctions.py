# STL Imports
from typing import List, Tuple
from re import search

# PIP Imports
from unidecode import unidecode

# Local Imports
from variables import allowed_letters, allowed_chars, max_word_count, max_word_len


def format_text(text: str, reduce_punct: bool) -> str:
    text = unidecode(text).upper()

    if reduce_punct:
        text = text.lstrip("!&,-.:;?")
        text = text.rstrip("&,-.:;")

    return text


def text_is_blank(text: str, words: List[str]) -> bool:
    return text.isspace() or not words


def text_has_no_words(text: str, valid_chars: str) -> bool:
    pattern = "[%s]{2}" % valid_chars
    return search(pattern, text) is None


def text_exceeds_max_word_count(words: List[str], maximum: int) -> bool:
    return len(words) > maximum


def text_exceeds_max_word_length(words: List[str], maximum: int) -> bool:
    for w in words:
        if len(w) > maximum:
            return True
    return False


def text_has_bad_char(text: str, good_chars: str) -> bool:
    pattern = "[^%s]" % good_chars
    return search(pattern, text) is not None


def text_has_too_many_consec_letters(text: str, letters: str) -> bool:
    pattern = "([%s])\\1{2,}" % letters
    return search(pattern, text) is not None


def __check_text(text: str, words: List[str]) -> Tuple[bool, str or None]:
    if text_is_blank(text, words):
        return (False, f"Your quote is blank\nPlease try again")

    elif text_has_no_words(text, allowed_letters):
        return (False, f"Your quote has no words\nPlease try again")

    elif text_exceeds_max_word_count(words, max_word_count):
        return (
            False,
            f"Your quote exceeds the maximum word count of {max_word_count}\nPlease try again",
        )
    elif text_exceeds_max_word_length(words, max_word_len):
        return (
            False,
            f"Your quote contains a word that exceeds the maximum word length of {max_word_len}\nPlease try again",
        )
    elif text_has_bad_char(text, allowed_chars):
        return (
            False,
            f"Your quote deviates from the allowed characters of {repr(allowed_chars)}\nPlease try again",
        )
    elif text_has_too_many_consec_letters(text, allowed_letters):
        return (
            False,
            f"Your quote contains too many consecutive matching letters\nPlease try again",
        )
    return True, None


def check_text(text: str, reduce_punct: bool) -> Tuple[bool, str or None]:
    text = format_text(text, reduce_punct)
    return __check_text(text, text.split())


def possible_max_line_lengths(text: str, words: List[str]) -> List[int]:
    """
    Returns a list of natural numbers ranging from 1 to the
    length of the given string. A dynamic jump variable keeps
    lists for longer strings reasonably short.
    """
    jump = int(len(words) / 15) + 1
    return [i for i in range(1, len(text), jump)]


def wrap(words: List[str], max_line_len: int) -> str:
    """
    To create a wrapped text string with the given list of words,
    joins groups of words into lines with spaces until lines
    reach lengths exceeding the given maximum line length integer,
    in which case, new lines are started at the next word boundary.
    """
    char_count = 0
    result = ""
    for w in words:
        char_count += len(w)
        if char_count > max_line_len:
            result += "\n" + w
            char_count = len(w)
        else:
            result += " " + w

    return result.strip()


def squareness_offset(string: str, lines: List[str]) -> float:
    """
    Returns a number representing the given wrapped string's offset
    from having a perfectly square shape.

    Return values = 0 indicate perfectly square wrapped strings.
    Return values > 0 indicate less perfectly square wrapped strings.
    """
    real_width = len(max(lines, key=len))
    target_width = len(lines) * 3
    width_offset = abs(real_width - target_width)

    real_height = len(lines)
    target_height = int((len(string) / 2) ** 0.5) + 1
    height_offset = abs(real_height - target_height)

    total_offset = width_offset + height_offset
    return total_offset


def avg_line_len_diff(lines: List[str]) -> int or float:
    """
    With the given list of lines, returns a number which is the
    result of dividing the sum of all line length differences
    by the total number of lines.

    Return values = 0 indicate perfectly length-uniform lines.
    Return values > 0 indicate less perfectly length-uniform lines.
    """
    diff = 0
    for line in lines:
        diff += sum(
            [abs(len(line) - len(other)) for other in [x for x in lines if x != line]]
        )
    return diff / len(lines)


def best_shaped_candidate(candidates: List[dict]) -> str:
    """
    Returns the candidate string in the given list of candidate
    dictionaries that has the most perfectly square and uniform text shape.
    """
    ratings = list()  # index-corresponding preference ratings per candidate
    for c in candidates:
        rating = 0
        rating -= squareness_offset(c["candidate"], c["lines"]) * len(c["candidate"])
        rating -= avg_line_len_diff(c["lines"]) * len(c["candidate"]) / 5
        ratings.append(rating)

    return candidates[ratings.index(max(ratings))][
        "candidate"
    ]  # highest rating = best candidate


def square_uniform_wrap(text: str, words: List[str]) -> str:
    """
    Attempts to create a beautiful, square, and uniform
    text shape with the given string and list of words.
    """
    if len(words) < 3:
        return "\n".join(words)

    candidates = set()
    for max_line_len in possible_max_line_lengths(text, words):
        candidates.add(wrap(words, max_line_len))

    candidate_items = list()
    for c in candidates:
        candidate_items.append(
            {"text": text, "words": words, "candidate": c, "lines": c.split("\n")}
        )

    return best_shaped_candidate(candidate_items)
