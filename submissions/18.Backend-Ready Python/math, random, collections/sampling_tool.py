"""
Exercise R3 — Random Sampling
Build sampling_tool.py.

Requirements:
- Start with a list of at least 50 unique IDs.
- Select 10 distinct IDs for a test batch.
- Verify that the sample has 10 entries and no duplicate IDs.
- Shuffle a copy of the original list without modifying the original.
- Demonstrate that using a fixed seed makes your selection reproducible.

"""

import random

random.seed(42)

original_list1  = [f"ORD-{i:03d}" for i in range(1,51)]

sample_data1 = random.sample(original_list1,k=10)

print(f"First Sample Selection: {sample_data1}")

seen_sample = set(sample_data1)

if len(sample_data1) == 10 and len(sample_data1) == len(seen_sample):

    print(f"✅ Success: All {len(sample_data1)} order IDs are completely unique.")

else:

    print("❌ Warning: Duplicate order IDs were detected!")


shuffled_copy  = original_list1.copy()
random.shuffle(shuffled_copy)


print(f"\nOriginal List (First 3): {original_list1[:3]} -> (Remained unchanged)")
print(f"Shuffled Copy (First 3): {shuffled_copy[:3]} -> (Successfully shuffled)")


random.seed(42)


sample_data2 = random.sample(original_list1,k=10)

print(f"Second Sample Selection: {sample_data2}")

if sample_data1 == sample_data2:
    print("✅ Reproducibility Confirmed: Both sample batches match exactly because of the fixed seed.")
else:
    print("❌ Reproducibility Failed: The samples do not match.")

