# Text Preprocessing Demo

A small, dependency-free Python script that turns raw English text into a list of normalized index terms. It does tokenization, punctuation cleanup, stop word removal and rule-based suffix stemming, then prints precision and recall for the result.

Author: Amirkasra Zarvandi

## What it does

For each word in the input, the script:

1. Splits the text on whitespace.
2. Strips `, . ; ! ?` from the ends of the word and removes any remaining periods (so `U.S.A.` becomes `usa`).
3. Lowercases the word.
4. Removes a trailing possessive `'s` or `’s` (`John's` becomes `john`).
5. Drops the word if it is in the stop word list.
6. Stems what is left by removing one suffix.

### Stemming rules

The stemmer checks suffixes in this order and removes the first one that matches:

```
ization, izes, ized, ize, ing, ed, ly, es, s
```

Two guards apply:

- A suffix is only removed if at least 3 characters remain.
- Hyphenated words such as `state-of-the-art` are left untouched.

### Stop words

The list is small and hard-coded in `STOP_WORDS`: `a, an, and, are, as, at, be, but, by, for, he, in, is, it, me, my, of, on, or, she, that, the, this, to, was, with, your`.

## Requirements

Python 3.6 or newer. No third-party packages.

## Usage

```bash
python AmirkasraZarvandi.py
```

At the prompt, enter `1`, `2` or `3` to use a built-in sample, or type any text of your own:

```
Enter 1, 2 or 3 for a sample text, or type your own text:
```

### Built-in samples

| Key | Text |
|-----|------|
| 1 | Friends, Romans, countrymen, lend me your ears; |
| 2 | John's new U.S.A. laptop is a state-of-the-art device. The price is high, but the quality is amazing! |
| 3 | The authorization for this authorized project is pending. He authorizes the payments regularly. |

### Example

Input: `2`

```
Text: John's new U.S.A. laptop is a state-of-the-art device. The price is high, but the quality is amazing!
Output: ['john', 'new', 'usa', 'laptop', 'state-of-the-art', 'device', 'price', 'high', 'quality', 'amaz']
Gold: ['john', 'new', 'usa', 'laptop', 'state-of-the-art', 'device', 'price', 'high', 'quality', 'amaz']
Precision: 1.0
Recall: 1.0
Extra: set()
Missed: set()
```

## Output fields

| Field | Meaning |
|-------|---------|
| Text | The input that was processed |
| Output | The list of processed terms, in original order |
| Gold | The reference term list the output is compared against |
| Precision | Share of output terms that also appear in the gold set |
| Recall | Share of gold terms that also appear in the output set |
| Extra | Terms in the output but not in the gold set |
| Missed | Terms in the gold set but not in the output |

## Known limitations

- **The evaluation is circular.** `gold` is produced by calling `preprocess(text)`, the same function that produces `output`, so precision and recall are always `1.0` for non-empty input. To get a meaningful score, replace `gold` with a hand-written reference list.
- **The stemmer is crude.** It strips suffixes without a dictionary, so it makes errors. For example, `amazing` becomes `amaz`, and `authorization` loses `ization` but other forms of the same word may stem differently.
- **Punctuation handling is minimal.** Only `, . ; ! ?` are stripped. Quotes, parentheses, colons and similar characters stay attached to words.
- **English only.** The stop words and suffix rules assume English text.
- **Scores use sets.** Duplicate terms and term order are ignored when computing precision and recall.

## Customizing

- Add or remove entries in `STOP_WORDS` to change what gets filtered.
- Edit `SUFFIXES` to change stemming. Keep longer suffixes before shorter ones so they match first.
- Add your own sample texts to the `TEXTS` dictionary.
