def get_num_words(words):
    return len(words.split())


def count_letter_occurrences(text):
    occurrences = {}
    for char in text:
        lowered = char.lower()
        if lowered in occurrences:
            occurrences[lowered] += 1
        else:
            occurrences[lowered] = 1
    return occurrences


def sort_letter_count_record(record):
    unsorted = []
    for key in record:
        unsorted.append({"char": key, "num": record[key]})
    unsorted.sort(reverse=True, key=lambda item: item["num"])
    return unsorted
