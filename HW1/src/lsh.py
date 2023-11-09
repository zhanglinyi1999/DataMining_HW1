import random

class LSH:
    def __init__(self, num_hashes, num_bands):
        self.num_hashes = num_hashes
        self.num_bands = num_bands
        self.buckets = {}
        self.doc_to_band = {}

    def hash_band(self, band):
        return hash(tuple(band))

    def insert(self, doc_id, signature):
        for band_num in range(self.num_bands):
            band = signature[band_num * self.num_hashes:(band_num + 1) * self.num_hashes]
            band_hash = self.hash_band(band)

            if band_hash in self.buckets:
                self.buckets[band_hash].append(doc_id)
            else:
                self.buckets[band_hash] = [doc_id]

            self.doc_to_band[doc_id] = self.doc_to_band.get(doc_id, []) + [band_hash]

    def get_candidates(self):
        candidates = set()
        for bucket in self.buckets.values():
            if len(bucket) > 1:
                for doc_id1 in bucket:
                    for doc_id2 in bucket:
                        if doc_id1 == doc_id2:
                            candidates.add((doc_id1, doc_id2))
        return candidates

if __name__ == "__main__":
    # Replace these with your own MinHash signatures and document IDs
    minhash_signatures = {
        "doc1": [1, 2, 3, 4, 5],
        "doc2": [2, 3, 4, 5, 6],
        "doc3": [3, 4, 5, 6, 7],
        "doc4": [4, 5, 6, 7, 8],
    }

    num_hashes = 5  # Number of hashes in each signature
    num_bands = 2  # Number of bands for LSH

    lsh = LSH(num_hashes, num_bands)

    for doc_id, signature in minhash_signatures.items():
        lsh.insert(doc_id, signature)

    candidates = lsh.get_candidates()

    print("Candidate Pairs of Similar Documents:")
    for pair in candidates:
        print(pair)
