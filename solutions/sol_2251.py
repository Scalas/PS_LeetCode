from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def fullBloom_flowers(flowers: List[List[int]], people: List[int]) -> List[int]:
        bloom_in = defaultdict(int)
        bloom_out = defaultdict(int)
        for i, o in flowers:
            bloom_in[i] += 1
            bloom_out[o] += 1

        ps = sorted(set(bloom_in.keys()) | set(bloom_out.keys()) | set(people))

        bloom_map = dict()
        bloom = 0
        for p in ps:
            bloom += bloom_in[p]
            bloom_map[p] = bloom
            bloom -= bloom_out[p]

        return list(map(lambda x: bloom_map[x], people))
