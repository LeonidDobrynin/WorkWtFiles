file_names = ['1.txt', '2.txt', '3.txt']


def merge_str(file_names):
    dict_files = {}
    count_words = []
    for name in file_names:
        text = []
        with open(name, 'r', encoding='utf-8') as file_obj:
            text += file_obj.readlines()

        dict_files[name] = len(text)
        count_words.append(len(text))
    count_words.sort()
    for count in count_words:
        for name in file_names:
            if count == dict_files.get(name):
                text = ''
                with open(name, 'r', encoding='utf-8') as file_obj:
                    text = file_obj.read()

                with open("merge.txt", 'a', encoding='utf-8') as file:
                    file.write(f"{name}\n{count}\n{text}\n")

    return dict_files

print(merge_str(file_names))