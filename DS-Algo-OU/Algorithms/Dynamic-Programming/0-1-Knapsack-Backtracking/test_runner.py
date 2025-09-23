import pandas as pd
import time
import sys
from knapsack import Knapsack

solution = Knapsack()

# ===============================================================
#  ✅ PASTE YOUR KNAPSACK SOLVER FUNCTION HERE
# ===============================================================

# ===============================================================


# Helper class for color-coding the output in the terminal
class TColors:
    PASSED = '\033[92m'  # Green
    FAILED = '\033[91m'  # Red
    WARNING = '\033[93m' # Yellow
    RESET = '\033[0m'    # Reset color

# --- Utility functions to parse the CSV data ---
def parse_int_list(str_list):
    """Converts a pipe-separated string to a list of ints."""
    if not isinstance(str_list, str) or not str_list:
        return []
    return [int(x) for x in str_list.split('|')]

def parse_item_tuples(str_tuples):
    """Converts a pipe-separated string of tuples to a list of tuples."""
    if not isinstance(str_tuples, str) or not str_tuples:
        return []
    # Using eval is simple for this trusted context.
    return [eval(t) for t in str_tuples.split('|')]

def load_test_cases(filename="testcases.csv"):
    """Loads and parses the knapsack test cases from the CSV file."""
    try:
        df = pd.read_csv(filename)
        df['weights'] = df['weights'].apply(parse_int_list)
        df['costs'] = df['costs'].apply(parse_int_list)
        df['expected_items'] = df['expected_items'].apply(parse_item_tuples)
        return df
    except FileNotFoundError:
        print(f"{TColors.FAILED}Error: The file '{filename}' was not found.{TColors.RESET}")
        print("Please make sure 'testcases.csv' is in the same directory as this script.")
        sys.exit(1)


# --- The Main Test Runner ---
def run_tests():
    """
    Loads test cases and runs the user's solver against each one,
    reporting the results.
    """
    test_data = load_test_cases()
    passed_count = 0
    total_count = len(test_data)
    TIME_LIMIT_SECONDS = 2.0  # Set a 2-second time limit

    print("🚀 Starting automated tests for your Knapsack solver...\n")

    for index, row in test_data.iterrows():
        print(f"--- Running Test #{index + 1}: {row['test_case_name']} ---")
        
        # Get the inputs and expected output for the current test case
        weights = row['weights']
        costs = row['costs']
        capacity = row['capacity']
        expected_items = sorted(row['expected_items']) # Sort for consistent comparison
        
        # Run the solver and measure the time
        start_time = time.time()
        actual_items = sorted(solution.calculate(weights, costs, capacity)) # Sort for comparison
        end_time = time.time()
        
        duration = end_time - start_time
        
        # --- Compare results and report status ---
        if actual_items == expected_items:
            if duration > TIME_LIMIT_SECONDS:
                status = f"{TColors.WARNING}PASSED (BUT SLOW){TColors.RESET}"
                print(f"Status: {status} | Time: {duration:.4f}s")
                print(f"      (This exceeded the {TIME_LIMIT_SECONDS}s time limit!)")
            else:
                status = f"{TColors.PASSED}PASSED{TColors.RESET}"
                print(f"Status: {status} | Time: {duration:.4f}s")
                passed_count += 1
        else:
            status = f"{TColors.FAILED}FAILED{TColors.RESET}"
            print(f"Status: {status} | Time: {duration:.4f}s")
            print(f"      Expected: {expected_items}")
            print(f"      Got:      {actual_items}")

    # --- Print the final summary ---
    print("\n" + "="*40)
    print("📊 Test Summary:")
    if passed_count == total_count:
        print(f"  {TColors.PASSED}All {total_count} tests passed! Congratulations! 🎉{TColors.RESET}")
    else:
        print(f"  {TColors.PASSED}Passed: {passed_count}/{total_count}{TColors.RESET}")
        print(f"  {TColors.FAILED}Failed: {total_count - passed_count}/{total_count}{TColors.RESET}")
    print("="*40)


if __name__ == "__main__":
    run_tests()