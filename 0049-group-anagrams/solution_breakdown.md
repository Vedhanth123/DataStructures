# 🎯 Group Anagrams - Complete Solution Breakdown

_Solving like a Google SWE_

## 📋 Problem Understanding

**What are anagrams?**

- Words with the same characters in different orders
- "eat" ↔ "tea" ↔ "ate" (all have: 1 'e', 1 'a', 1 't')

**Goal:** Group strings that are anagrams of each other.

## 🤔 Thought Process (Interview Approach)

### Step 1: Identify the Pattern

- Anagrams have the **same character frequency**
- We need a way to identify anagrams → **Create a unique key**

### Step 2: Key Generation Strategies

#### Strategy 1: Sort Characters

```python
"eat" → sorted → "aet" (key)
"tea" → sorted → "aet" (same key!)
"bat" → sorted → "abt" (different key)
```

#### Strategy 2: Character Count Array ⭐ (More Efficient)

```python
"eat" → [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
         a b c d e f g h i j k l m n o p q r s t u v w x y z
```

## 🔧 Solution Implementations

### Approach 1: Sorting-Based (Easier to understand)

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        # Create key by sorting characters
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())
```

**Time:** O(N × M log M) where N = number of strings, M = average length
**Space:** O(N × M)

### Approach 2: Character Counting (Optimal) ⭐

```python
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        # Create key using character frequency
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        # Use tuple as dictionary key
        key = tuple(count)
        groups[key].append(word)

    return list(groups.values())
```

**Time:** O(N × M) - Linear in string length!
**Space:** O(N × M)

## 🎨 Visual Walkthrough

Let's trace through: `["eat","tea","tan","ate","nat","bat"]`

### Step-by-Step Execution:

```
Input: ["eat","tea","tan","ate","nat","bat"]

Word: "eat"
Count: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
       a                 e                   t
Key: (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)
groups = {key1: ["eat"]}

Word: "tea"
Count: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
Key: (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) ← Same!
groups = {key1: ["eat", "tea"]}

Word: "tan"
Count: [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0]
       a                             n       t
Key: (1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0) ← Different!
groups = {key1: ["eat", "tea"], key2: ["tan"]}

... continue for remaining words
```

## 🧪 Test Cases & Edge Cases

```python
# Test your understanding:
test_cases = [
    ["eat","tea","tan","ate","nat","bat"],  # Normal case
    [""],                                    # Empty string
    ["a"],                                   # Single character
    ["abc", "bca", "cab", "xyz"],           # Mixed groups
    ["abddde", "dddeab"]                    # Longer strings
]
```

## 💡 Key Insights (Google Interview Points)

1. **HashMap Pattern Recognition:** This is fundamentally a grouping problem
2. **Key Design:** The hardest part is choosing the right key
3. **Trade-offs:** Sorting vs Counting (time complexity difference)
4. **Space Optimization:** Could we do better than O(N×M)?
5. **Edge Cases:** Empty strings, single characters, duplicates

## ⚡ Optimization Variations

### Memory-Optimized (if strings are very long):

```python
def groupAnagrams(strs):
    from collections import Counter
    groups = defaultdict(list)

    for word in strs:
        # Only store non-zero counts
        key = tuple(sorted(Counter(word).items()))
        groups[key].append(word)

    return list(groups.values())
```

## 🎯 Interview Tips

1. **Start Simple:** Always mention the sorting approach first
2. **Optimize:** Then explain the counting optimization
3. **Communicate:** Walk through examples step by step
4. **Edge Cases:** Don't forget empty strings!
5. **Complexity:** Always analyze time/space complexity

## 🔍 Related Problems

- Valid Anagram (242)
- Find All Anagrams in a String (438)
- Minimum Window Substring (76)

---

_This is the kind of systematic approach that gets you through FAANG interviews! 🚀_
