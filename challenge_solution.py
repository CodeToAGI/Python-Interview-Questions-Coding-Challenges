"""
CodeToAGI — Episode 59 Challenge Solution
Python Interview Questions & Coding Challenges

Complete solutions for all 6 problems + timing for bonus.
"""

# ====================== 1. TWO SUM ======================
def two_sum(nums, target):
    """Optimal O(n) solution using dictionary."""
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return None


# ====================== 2. REVERSE STRING ======================
def reverse_string(s):
    """Two-pointer approach (no slicing)."""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)


# ====================== 3. PALINDROME ======================
def is_palindrome(s):
    """Two-pointer approach - O(n) time, O(1) space."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ====================== 4. FIND DUPLICATES ======================
def find_duplicates(nums):
    """O(n) time using set."""
    seen = set()
    duplicates = set()
    for n in nums:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    return list(duplicates)


# ====================== 5. FIZZBUZZ ======================
def fizzbuzz(n=100):
    """Clean string-build approach."""
    result = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        result.append(s or str(i))
    return result[:20]  # Show first 20 for demo


# ====================== 6. FIBONACCI ======================
def fib_iterative(n):
    """Optimal iterative solution - O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ====================== DEMO & TIMING ======================
def main():
    print("═" * 70)
    print("CodeToAGI EP59 — FULL CHALLENGE SOLUTION")
    print("═" * 70)

    print("\n1. TWO SUM")
    nums = [2, 7, 11, 15]
    print(f"Input: {nums}, target=9 → {two_sum(nums, 9)}")

    print("\n2. REVERSE STRING")
    print(f"'hello' → '{reverse_string('hello')}'")
    print(f"'racecar' → '{reverse_string('racecar')}'")

    print("\n3. PALINDROME")
    print(f"'racecar' → {is_palindrome('racecar')}")
    print(f"'python' → {is_palindrome('python')}")

    print("\n4. FIND DUPLICATES")
    print(f"[1, 2, 3, 2, 4, 1, 5] → {find_duplicates([1,2,3,2,4,1,5])}")

    print("\n5. FIZZBUZZ (first 20)")
    print(fizzbuzz(20))

    print("\n6. FIBONACCI")
    print(f"fib(10) = {fib_iterative(10)}")
    print(f"fib(20) = {fib_iterative(20)}")

    # Bonus: Timing
    print("\nBONUS — Performance Test")
    import time
    n = 40
    start = time.time()
    fib_iterative(n)
    print(f"Iterative fib({n}) took {time.time()-start:.6f} seconds")

    print("\n✅ CHALLENGE COMPLETE!")
    print("Reply with your time on YouTube!")


if __name__ == "__main__":
    main()
