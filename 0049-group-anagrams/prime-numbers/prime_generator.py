#!/usr/bin/env python3
"""
Prime Number Generation Approaches
From worst to best time complexity
"""

import time
import math
from typing import List


class PrimeGenerator:
    """
    Class containing various approaches to generate first n prime numbers
    Arranged from least efficient to most efficient
    """
    
    def __init__(self):
        """Initialize with timing and performance data storage"""
        self.timing_data = {}
    
    def time_operation(self, func, *args, **kwargs):
        """Utility to time the execution of a function"""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        return result, end_time - start_time
    
    # Approach 1: Brute Force Trial Division (Worst approach)
    def brute_force(self, n: int) -> List[int]:
        """
        Generate first n primes using brute force trial division
        Time Complexity: O(n²√p) where p is the nth prime
        Space Complexity: O(n)
        """
        if n <= 0:
            return []
        
        primes = []
        num = 2
        
        while len(primes) < n:
            is_prime = True
            # Check divisibility by all numbers from 2 to num-1
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
            num += 1
        
        return primes
    
    # Approach 2: Optimized Trial Division with square root optimization
    def optimized_trial_division(self, n: int) -> List[int]:
        """
        Generate first n primes using trial division with sqrt(n) optimization
        Time Complexity: O(n√p) where p is the nth prime
        Space Complexity: O(n)
        """
        if n <= 0:
            return []
        
        primes = []
        num = 2
        
        while len(primes) < n:
            is_prime = True
            # Check divisibility by numbers only up to sqrt(num)
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
            num += 1
        
        return primes
    
    # Approach 3: Trial Division against known primes only
    def trial_division_with_primes(self, n: int) -> List[int]:
        """
        Generate first n primes by checking divisibility against previously found primes
        Time Complexity: O(n√p) with better constant factors
        Space Complexity: O(n)
        """
        if n <= 0:
            return []
        
        if n == 1:
            return [2]
        
        primes = [2]  # Start with first prime
        num = 3       # Check from 3 onwards (odd numbers)
        
        while len(primes) < n:
            is_prime = True
            sqrt_num = math.sqrt(num)
            
            # Only check divisibility against known primes up to sqrt(num)
            for prime in primes:
                if prime > sqrt_num:
                    break
                if num % prime == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
            num += 2  # Skip even numbers
        
        return primes
    
    # Approach 4: Sieve of Eratosthenes
    def sieve_of_eratosthenes(self, n: int) -> List[int]:
        """
        Generate first n primes using Sieve of Eratosthenes
        Time Complexity: O(m log log m) where m is upper bound of nth prime
        Space Complexity: O(m)
        """
        if n <= 0:
            return []
        
        # Estimate an upper bound for the nth prime using prime number theorem
        # p_n ≈ n log n + n log log n for n > 6
        if n < 6:
            limit = 15  # Handle small n
        else:
            limit = int(n * (math.log(n) + math.log(math.log(n)))) + 1
            # Add extra margin to be safe
            limit = max(limit, n * 15)
        
        # Initialize sieve array
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        
        # Apply sieve algorithm
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                # Mark all multiples as composite
                for j in range(i*i, limit + 1, i):
                    sieve[j] = False
        
        # Collect primes
        primes = []
        for i in range(2, limit + 1):
            if sieve[i]:
                primes.append(i)
                if len(primes) == n:
                    break
        
        return primes
    
    # Approach 5: Segmented Sieve (best for very large numbers)
    def segmented_sieve(self, n: int) -> List[int]:
        """
        Generate first n primes using Segmented Sieve
        Time Complexity: O(m log log m) with better space efficiency
        Space Complexity: O(√m)
        """
        if n <= 0:
            return []
            
        # For small n, use regular sieve
        if n < 100:
            return self.sieve_of_eratosthenes(n)
        
        # Estimate upper bound
        if n < 6:
            limit = 15
        else:
            limit = int(n * (math.log(n) + math.log(math.log(n)))) + 1
            limit = max(limit, n * 15)
        
        # Size of segments
        segment_size = int(math.sqrt(limit))
        
        # Generate small primes up to sqrt(limit)
        small_limit = int(math.sqrt(limit)) + 1
        sieve = [True] * small_limit
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(math.sqrt(small_limit)) + 1):
            if sieve[i]:
                for j in range(i*i, small_limit, i):
                    sieve[j] = False
                    
        # Collect small primes
        small_primes = [i for i in range(small_limit) if sieve[i]]
        
        # Initialize final result
        result = []
        
        # Process segments
        low = 0
        high = segment_size
        
        while len(result) < n and low < limit:
            # Adjust high for last segment
            high = min(high, limit)
            
            # Create segment sieve
            segment = [True] * (high - low + 1)
            
            # Mark multiples of small primes in segment
            for prime in small_primes:
                # Find first multiple of prime in segment
                start = max(prime * prime, ((low + prime - 1) // prime) * prime)
                
                for j in range(start, high + 1, prime):
                    segment[j - low] = False
            
            # Collect primes from segment
            for i in range(max(2, low), high + 1):
                if segment[i - low]:
                    result.append(i)
                    if len(result) >= n:
                        break
            
            # Move to next segment
            low = high + 1
            high = low + segment_size
        
        return result[:n]
    
    # Compare all approaches
    def compare_approaches(self, n: int) -> dict:
        """Run and time all approaches for comparison"""
        if n > 1000:
            print("Warning: Large input may take significant time for inefficient methods")
            print("Skipping brute force for large n")
            
        approaches = [
            ("Brute Force", self.brute_force if n <= 100 else None),
            ("Optimized Trial Division", self.optimized_trial_division if n <= 1000 else None),
            ("Trial Division with Primes", self.trial_division_with_primes),
            ("Sieve of Eratosthenes", self.sieve_of_eratosthenes),
            ("Segmented Sieve", self.segmented_sieve)
        ]
        
        results = {}
        
        for name, func in approaches:
            if func is None:
                results[name] = {
                    "primes": [],
                    "time": float('inf'),
                    "status": "Skipped (too slow for large n)"
                }
                continue
                
            try:
                primes, execution_time = self.time_operation(func, n)
                results[name] = {
                    "primes": primes,
                    "time": execution_time,
                    "status": "Success"
                }
                print(f"{name}: Generated {len(primes)} primes in {execution_time:.6f} seconds")
            except Exception as e:
                results[name] = {
                    "primes": [],
                    "time": float('inf'),
                    "status": f"Error: {str(e)}"
                }
                print(f"{name}: Error - {str(e)}")
        
        return results


def main():
    """Test all prime generation approaches"""
    generator = PrimeGenerator()
    
    test_cases = [10, 100, 1000]
    
    for n in test_cases:
        print(f"\n{'='*50}")
        print(f"Generating first {n} prime numbers:")
        print(f"{'='*50}")
        
        results = generator.compare_approaches(n)
        
        # Verify all approaches produce the same result
        valid_results = [r["primes"] for r in results.values() if r["status"] == "Success" and r["primes"]]
        
        if valid_results:
            reference = valid_results[0]
            if all(r == reference for r in valid_results):
                print("\nAll approaches produced the same result!")
                print(f"First 10 primes: {reference[:10]}")
            else:
                print("\nWarning: Results differ between approaches!")
        
        # Print timing comparison
        print("\nTiming Comparison:")
        for name, result in results.items():
            if result["time"] != float('inf'):
                print(f"{name:25}: {result['time']:.6f} seconds")
            else:
                print(f"{name:25}: {result['status']}")


if __name__ == "__main__":
    main()
