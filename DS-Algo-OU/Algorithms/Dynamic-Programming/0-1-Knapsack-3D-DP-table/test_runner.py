import pandas as pd
import time
import sys
from Knapsack3d import DP3D

# Assumes your Knapsack3d.py file contains the DP3d class with the solution method.
obj = DP3D()

# ===============================================================
#  (Your knapsack solver from the other file is imported above)
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
    return [int(x) for x in str_list.split('|') if x.strip()]

def parse_item_tuples(str_tuples):
    """Converts a pipe-separated string of tuples to a list of tuples."""
    if not isinstance(str_tuples, str) or not str_tuples:
        return []
    # Using eval is simple for this trusted context. For untrusted data, use a safer parser.
    return [eval(t) for t in str_tuples.split('|')]

def load_test_cases(filename="testcases.csv"):
    """Loads and parses the 2D knapsack test cases from the CSV file."""
    try:
        df = pd.read_csv(filename)
        # Parse the three arrays for the 2D knapsack problem
        df['weights'] = df['weights'].apply(parse_int_list)
        df['volumes'] = df['volumes'].apply(parse_int_list)
        df['values'] = df['values'].apply(parse_int_list)
        # The expected output items are now 3-element tuples (w, v, val)
        df['expected_items'] = df['expected_items'].apply(parse_item_tuples)
        return df
    except FileNotFoundError:
        print(f"{TColors.FAILED}Error: The file '{filename}' was not found.{TColors.RESET}")
        print("Please make sure 'testcases.csv' is in the same directory.")
        sys.exit(1)
    except KeyError as e:
        print(f"{TColors.FAILED}Error: Missing column in '{filename}': {e}{TColors.RESET}")
        print("Please ensure your CSV has columns: 'weights', 'volumes', 'values', 'max_weight', 'max_volume', etc.")
        sys.exit(1)


# --- The Main Test Runner ---
def run_tests():
    """
    Loads 2D knapsack test cases and runs the solver against each one.
    """
    test_data = load_test_cases()
    passed_count = 0
    total_count = len(test_data)
    TIME_LIMIT_SECONDS = 5.0  # Increased time limit for the more complex problem

    print("🚀 Starting automated tests for your 2D Knapsack solver...\n")

    for index, row in test_data.iterrows():
        print(f"--- Running Test #{index + 1}: {row['test_case_name']} ---")

        # Get the inputs and expected output for the current test case
        weights = row['weights']
        volumes = row['volumes']
        values = row['values']
        max_weight = row['max_weight']
        max_volume = row['max_volume']
        expected_value = row['expected_value']
        expected_items = sorted(row['expected_items']) # Sort for consistent comparison

        # Run the solver and measure the time
        start_time = time.time()
        # The solver now returns both the max value and the list of items
        actual_value, actual_items_list = obj.solution(weights, volumes, values, max_weight, max_volume)
        actual_items = sorted(actual_items_list) # Sort for comparison
        end_time = time.time()

        duration = end_time - start_time

        # --- Compare results and report status ---
        # We'll check both the total value and the items chosen
        if actual_items == expected_items and actual_value == expected_value:
            if duration > TIME_LIMIT_SECONDS:
                status = f"{TColors.WARNING}PASSED (BUT SLOW){TColors.RESET}"
                print(f"Status: {status} | Time: {duration:.4f}s")
                print(f"      (This exceeded the {TIME_LIMIT_SECONDS}s time limit!)")
            else:
                status = f"{TColors.PASSED}PASSED{TColors.RESET}"
                print(f"Status: {status} | Time: {duration:.4f}s | Value: {actual_value}")
                passed_count += 1
        else:
            status = f"{TColors.FAILED}FAILED{TColors.RESET}"
            print(f"Status: {status} | Time: {duration:.4f}s")
            if actual_value != expected_value:
                print(f"      Value Mismatch -> Expected: {expected_value}, Got: {actual_value}")
            if actual_items != expected_items:
                print(f"      Items Mismatch -> Expected: {expected_items}")
                print(f"                       Got:      {actual_items}")

    # --- Print the final summary ---
    print("\n" + "="*50)
    print("📊 Test Summary:")
    if passed_count == total_count:
        print(f"  {TColors.PASSED}All {total_count} tests passed! Excellent work! 🎉{TColors.RESET}")
    else:
        print(f"  {TColors.PASSED}Passed: {passed_count}/{total_count}{TColors.RESET}")
        print(f"  {TColors.FAILED}Failed: {total_count - passed_count}/{total_count}{TColors.RESET}")
    print("="*50)


if __name__ == "__main__":
    run_tests()