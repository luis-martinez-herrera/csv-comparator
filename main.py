from pandas import read_csv
from pandas.util import hash_pandas_object
from collections import defaultdict


def compare(files):
    duplicate_check = defaultdict(list)
    for f in files:
        duplicate_check[hash_pandas_object(read_csv(f), index=False).sum()].append(f)
    print(duplicate_check)


def main():
    print("Hello World!")
    compare(["File1.csv", "File2.csv"])


if __name__ == "__main__":
    main()
