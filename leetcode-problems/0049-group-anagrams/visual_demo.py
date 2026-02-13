#!/usr/bin/env python3
"""
🎯 Visual Step-by-Step Demonstration
Group Anagrams Problem - Interactive Learning Tool
"""

from collections import defaultdict

def visual_group_anagrams(strs):
    """
    Demonstrates the grouping process step by step with visual output
    """
    print("🚀 Starting Group Anagrams Algorithm")
    print("=" * 60)
    print(f"📥 Input: {strs}")
    print()
    
    groups = defaultdict(list)
    
    for i, word in enumerate(strs):
        print(f"🔄 Processing word #{i+1}: '{word}'")
        
        # Show character counting process
        char_count = [0] * 26
        print("   📊 Character frequency analysis:")
        
        for char in word:
            char_count[ord(char) - ord('a')] += 1
            print(f"      '{char}' → position {ord(char) - ord('a')} (count: {char_count[ord(char) - ord('a')]})")
        
        # Show the signature
        signature = tuple(char_count)
        non_zero_counts = [(chr(ord('a') + i), count) for i, count in enumerate(char_count) if count > 0]
        print(f"   🔑 Signature: {non_zero_counts}")
        
        # Add to group
        groups[signature].append(word)
        print(f"   📁 Added to group. Current groups: {dict(groups)}")
        print("   " + "-" * 50)
        print()
    
    result = list(groups.values())
    print("🎉 Final Result:")
    for i, group in enumerate(result):
        print(f"   Group {i+1}: {group}")
    
    return result

def demonstrate_key_concepts():
    """
    Shows why the algorithm works with concrete examples
    """
    print("\n🧠 Key Concept Demonstration")
    print("=" * 60)
    
    examples = [
        ("eat", "tea", "ate"),
        ("tan", "nat"),
        ("bat",),
    ]
    
    for group in examples:
        print(f"\n🔍 Analyzing group: {group}")
        
        signatures = []
        for word in group:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            
            signature = tuple(char_count)
            signatures.append(signature)
            
            non_zero = [(chr(ord('a') + i), count) for i, count in enumerate(char_count) if count > 0]
            print(f"   '{word}' → {non_zero}")
        
        # Check if all signatures are the same
        all_same = all(sig == signatures[0] for sig in signatures)
        print(f"   🎯 All signatures match: {all_same}")
        if all_same:
            print("   ✅ These are anagrams!")
        else:
            print("   ❌ These are NOT anagrams!")

def complexity_analysis():
    """
    Explains the time and space complexity
    """
    print("\n📈 Complexity Analysis")
    print("=" * 60)
    
    print("🕐 Time Complexity: O(N × M)")
    print("   • N = number of strings")
    print("   • M = average length of strings")
    print("   • For each string, we iterate through its characters once")
    print("   • Creating the signature takes O(M) time")
    print("   • HashMap operations are O(1) average case")
    
    print("\n💾 Space Complexity: O(N × M)")
    print("   • Storing all strings in the result: O(N × M)")
    print("   • HashMap with at most N entries: O(N)")
    print("   • Each signature is O(1) space (fixed size array)")
    
    print("\n⚡ Why this beats sorting approach:")
    print("   • Sorting approach: O(N × M log M)")
    print("   • Our approach: O(N × M)")
    print("   • For long strings, this difference is significant!")

if __name__ == "__main__":
    # Example from the problem
    test_input = ["eat","tea","tan","ate","nat","bat"]
    
    visual_group_anagrams(test_input)
    demonstrate_key_concepts()
    complexity_analysis()
    
    print("\n🎓 Pro Tips for Google Interviews:")
    print("   1. Always start with the simple sorting approach")
    print("   2. Then optimize to character counting")
    print("   3. Discuss trade-offs and complexity")
    print("   4. Consider edge cases (empty strings, single chars)")
    print("   5. Think about follow-up questions (Unicode? Case sensitivity?)")
