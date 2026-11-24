from bisect import bisect_right, insort
import hashlib

file = "aoc-2026-pre-1-challenge-1.txt"
# file = "aoc-2026-pre-1-challenge-2.txt"
with open(file) as f:
    data = list(map(int, f.read().splitlines()))

lst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
indexes = []  # sorted original indices of chocolates already picked
answer = ""

sint_index = 0  # current index in the remaining chocolates
for step in data[:]:
    sint_index += step

    # Convert remaining-list index `sint_index` to original belt index `orig_idx`
    orig_idx = sint_index
    while True:
        # Count how many removed items have original index <= orig_idx
        removed_before = bisect_right(indexes, orig_idx)
        new_orig = sint_index + removed_before
        if new_orig == orig_idx:
            break
        orig_idx = new_orig

    answer += lst[orig_idx % 26]
    insort(indexes, orig_idx)

print(answer)
checksum = hashlib.sha256(answer.encode("utf-8")).hexdigest()
print(checksum)