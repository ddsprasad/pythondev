import re


# regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#
# pattren = re.compile(regex)
#
# my_sentence = "ddsprasad@gmail.com"
#
# # a = re.search('this',my_sentence)
# a = pattren.search(my_sentence)
#
# print(a)
# print(a.group())
# print(a.group())


def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(re.sub('[€K]', '', x,flags=re.UNICODE)) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(re.sub('[€M]', '', x,flags=re.UNICODE)) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(re.sub('[€B]', '', x,flags=re.UNICODE)) * 1000000000
    return 0.0

print(value_to_float('€1.1B'))
# print(float(20.1*1000))
