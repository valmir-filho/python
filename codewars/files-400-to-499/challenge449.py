"""
Task: You are given a dictionary-like object (implementation may vary by language) containing languages as
keys and your corresponding test results as values. Return the list of languages where your score is at least 60, in descending order of the scores.

Note: the scores will always be unique (so no duplicate values).
"""


def my_languages(results):
    return [
        language
        for language, score in sorted(results.items(), key=lambda x: x[1], reverse=True)
        if score >= 60
    ]
