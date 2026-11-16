#!/usr/bin/env python3
"""Create a CSV pivot table using only the standard library."""
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def pivot(rows, row_field, column_field, value_field=None, agg="count"):
    buckets = defaultdict(list)
    row_values, column_values = set(), set()
    for item in rows:
        if row_field not in item or column_field not in item:
            raise ValueError("row and column fields must exist in the CSV header")
        row_key = item[row_field] or "(blank)"
        column_key = item[column_field] or "(blank)"
        row_values.add(row_key)
        column_values.add(column_key)
        if agg == "count":
            buckets[(row_key, column_key)].append(1)
        else:
            if not value_field or value_field not in item:
                raise ValueError("this aggregation requires --values")
            try:
                buckets[(row_key, column_key)].append(float(item[value_field]))
            except (TypeError, ValueError):
                raise ValueError(f"non-numeric value in {value_field}: {item[value_field]!r}")
    columns = sorted(column_values)
    result = [["", *columns]]
    for row_key in sorted(row_values):
        output = [row_key]
        for column_key in columns:
            values = buckets[(row_key, column_key)]
            if not values:
                output.append(0 if agg == "count" else "")
            elif agg == "count":
                output.append(len(values))
            elif agg == "sum":
                output.append(sum(values))
            elif agg == "avg":
                output.append(round(sum(values) / len(values), 4))
            elif agg == "min":
                output.append(min(values))
            elif agg == "max":
                output.append(max(values))
            else:
                raise ValueError(f"unsupported aggregation: {agg}")
        result.append(output)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--rows", required=True, help="row dimension column")
    parser.add_argument("--columns", required=True, help="column dimension")
    parser.add_argument("--values", help="numeric value column for sum/avg/min/max")
    parser.add_argument("--agg", choices=("count", "sum", "avg", "min", "max"), default="count")
    parser.add_argument("--output", type=Path, help="output CSV path; stdout if omitted")
    args = parser.parse_args()
    try:
        with args.file.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            result = pivot(reader, args.rows, args.columns, args.values, args.agg)
        target = args.output.open("w", encoding="utf-8", newline="") if args.output else sys.stdout
        try:
            csv.writer(target).writerows(result)
        finally:
            if args.output:
                target.close()
        return 0
    except (OSError, ValueError, csv.Error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
