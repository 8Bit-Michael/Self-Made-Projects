def top_k_frequent(nums, k):
    counts = {}  

    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    top_k = [item[0] for item in sorted_counts[:k]]

    return top_k

print(top_k_frequent([1, 1, 1, 2, 2, 3, 4, 4], 2))
