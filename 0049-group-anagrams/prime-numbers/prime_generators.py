#!/usr/bin/env python3
"""
Prime Number Generation - Multiple Approaches
From worst to best performance with detailed analysis
"""

import time
import math
from typing import List, Generator, Tuple

class PrimeGenerators:
    """Collection of prime number generation algorithms"""
    
    def __init__(self):
        self.timing_results = {}
    
    def time_function(self, func, *args, **kwargs):
        """Helper to time function execution"""
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result, end - start
    
    # Approach 1: Brute Force Trial Division (Worst)
    def brute_force_primes(self, n: int) -> List[int]:
        """
        Generate first n primes using brute force trial division
        Time: O(n² * sqrt(p)) where p is the nth prime
        Space: O(n)
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
    
    # Approach 2: Trial Division with Square Root Optimization
    def trial_division_sqrt(self, n: int) -> List[int]:
        """
        Generate first n primes using trial division up to sqrt(num)
        Time: O(n * sqrt(p) * sqrt(p)) = O(n * p) where p is the nth prime
        Space: O(n)
        """
        if n <= 0:
            return []
        
        primes = []
        num = 2
        
        while len(primes) < n:
            is_prime = True
            # Only check up to sqrt(num)
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
            num += 1
        
        return primes
    
    # Approach 3: Trial Division Against Known Primes
    def trial_division_primes(self, n: int) -> List[int]:
        """
        Generate first n primes by testing divisibility against known primes only
        Time: O(n² * π(sqrt(p))/ln(sqrt(p))) where π(x) is prime counting function
        Space: O(n)
        """
        if n <= 0:
            return []
        
        primes = [2]
        if n == 1:
            return primes
        
        num = 3
        while len(primes) < n:
            is_prime = True
            # Only test against known primes up to sqrt(num)
            sqrt_num = math.sqrt(num)
            for prime in primes:
                if prime > sqrt_num:
                    break
                if num % prime == 0:
                    is_prime = False
                    break
            
            if is_prime:
                primes.append(num)
            num += 2  # Skip even numbers after 2
        
        return primes
    
    # Approach 4: Sieve of Eratosthenes (Best for range)
    def sieve_of_eratosthenes(self, n: int) -> List[int]:
        """
        Generate first n primes using Sieve of Eratosthenes
        Time: O(m * log(log(m))) where m is upper bound estimate
        Space: O(m)
        """
        if n <= 0:
            return []
        
        # Estimate upper bound for nth prime using prime number theorem
        if n < 6:
            limit = 12
        else:
            # Upper bound: n * (ln(n) + ln(ln(n)))
            limit = max(int(n * (math.log(n) + math.log(math.log(n)))), n * 15)
        
        # Create boolean array
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        # Sieve process
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                # Mark multiples as composite
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        
        # Collect first n primes
        primes = []
        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                if len(primes) == n:
                    break
        
        return primes
    
    # Approach 5: Segmented Sieve (Best for very large n)
    def segmented_sieve(self, n: int) -> List[int]:
        """
        Generate first n primes using segmented sieve
        Time: O(m * log(log(m))) with better memory efficiency
        Space: O(sqrt(m)) for each segment
        """
        if n <= 0:
            return []
        
        # For small n, use regular sieve
        if n <= 1000:
            return self.sieve_of_eratosthenes(n)
        
        # Estimate upper bound
        if n < 6:
            limit = 12
        else:
            limit = max(int(n * (math.log(n) + math.log(math.log(n)))), n * 15)
        
        segment_size = max(int(math.sqrt(limit)), 1000)
        
        # Generate small primes first
        small_limit = int(math.sqrt(limit)) + 1
        small_sieve = [True] * small_limit
        small_sieve[0] = small_sieve[1] = False
        
        for i in range(2, int(math.sqrt(small_limit)) + 1):
            if small_sieve[i]:
                for j in range(i * i, small_limit, i):
                    small_sieve[j] = False
        
        small_primes = [i for i in range(2, small_limit) if small_sieve[i]]
        primes = []
        
        # Process segments
        low = 0
        high = segment_size
        
        while len(primes) < n and low < limit:
            high = min(high, limit)
            
            # Create segment
            segment = [True] * (high - low + 1)
            
            # Mark multiples of small primes in this segment
            for prime in small_primes:
                # Find first multiple of prime in [low, high]
                start = max(prime * prime, (low + prime - 1) // prime * prime)
                
                for j in range(start, high + 1, prime):
                    segment[j - low] = False
            
            # Collect primes from this segment
            for i in range(max(2, low), high + 1):
                if segment[i - low]:
                    primes.append(i)
                    if len(primes) == n:
                        break
            
            low = high + 1
            high = low + segment_size
        
        return primes[:n]
    
    def benchmark_all_approaches(self, n: int) -> dict:
        """Benchmark all approaches and return timing results"""
        approaches = [
            ("Brute Force", self.brute_force_primes),
            ("Trial Division (√n)", self.trial_division_sqrt),
            ("Trial Division (Primes)", self.trial_division_primes),
            ("Sieve of Eratosthenes", self.sieve_of_eratosthenes),
            ("Segmented Sieve", self.segmented_sieve)
        ]
        
        results = {}
        
        for name, func in approaches:
            try:
                # Skip brute force for large n to avoid long wait times
                if name == "Brute Force" and n > 100:
                    results[name] = {
                        "primes": [],
                        "time": float('inf'),
                        "status": "Skipped (too slow for large n)"
                    }
                    continue
                
                primes, exec_time = self.time_function(func, n)
                results[name] = {
                    "primes": primes,
                    "time": exec_time,
                    "status": "Completed"
                }
                print(f"{name}: {exec_time:.6f}s")
                
            except Exception as e:
                results[name] = {
                    "primes": [],
                    "time": float('inf'),
                    "status": f"Error: {str(e)}"
                }
        
        return results

def main():
    """Test and demonstrate all approaches"""
    generator = PrimeGenerators()
    
    # Test with different values of n
    test_cases = [10, 50, 100, 500]
    
    for n in test_cases:
        print(f"\n{'='*50}")
        print(f"Generating first {n} primes:")
        print('='*50)
        
        results = generator.benchmark_all_approaches(n)
        
        # Verify all approaches give same result (excluding skipped ones)
        valid_results = [r["primes"] for r in results.values() 
                        if r["status"] == "Completed" and r["primes"]]
        
        if valid_results and all(result == valid_results[0] for result in valid_results):
            print(f"\n✓ All approaches produced identical results")
            print(f"First 10 primes: {valid_results[0][:10]}")
        else:
            print(f"\n✗ Results differ between approaches!")
        
        # Show timing comparison
        print(f"\nTiming Results:")
        for name, result in results.items():
            if result["time"] != float('inf'):
                print(f"{name:25}: {result['time']:.6f}s")
            else:
                print(f"{name:25}: {result['status']}")

if __name__ == "__main__":
    main()
