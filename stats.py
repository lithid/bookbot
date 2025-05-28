def get_num_words(words):
    return len(words.split())


def get_num_chars(words):
    chars_dict = {}
    for i in words.lower():
        try:
            chars_dict[i] += 1
        except Exception:
            chars_dict[i] = 1

    return chars_dict


def get_sorted_chars(words_dict):
    def sort_on(dict):
        return dict["num"]

    my_list = [{"char": key, "num": value} for key, value in words_dict.items()]
    my_list.sort(reverse=True, key=sort_on)
    return my_list
