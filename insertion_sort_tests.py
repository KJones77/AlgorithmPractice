from insertion_sort import Insert_Sorter as IS
unsorted6 = [999, 2, 3, 8, 1, 2, 10, 2000]
unsorted0 = [271,110,827,375,133,809,860,935,134,259,99,302,510,388,681,48,913,968,7,579]
unsorted1 = [67,65,92,75,25,27,32,68,85,26,97,26]
unsorted2 = [43,57,9,55,64,87,9,10,84,34,99,22]
unsorted3 = [121,378,413,334,33,332,362,315,185,47,354,917]
unsorted4 = [15,201,65,148,12,191,116,150,143,198,88,83]
unsorted5 = [220,209,140,44,126,73,132,88,16,228,226,114,204,81,139,70,101,15,13,185,207,212,165,197,20,225,207,217,199,9,94,36,157,201]
unsorted_group = [unsorted0, unsorted1, unsorted2, unsorted3, unsorted4, unsorted5]

in_sorter = IS()
in_sorter.asc_sort(unsorted6)
print(unsorted6)

