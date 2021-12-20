from decimal import Decimal
import functools


def convertObject(input):
    mapped = list(map(Decimal, list(map(str, input['Sums']))))
    return {'SumResult': (sum(mapped) * Decimal(input["K"])),
            'MulResult': (functools.reduce(lambda a, b: a * b, input["Muls"])),
            'SortedInputs': (sorted(input["Sums"] + input["Muls"]))}
