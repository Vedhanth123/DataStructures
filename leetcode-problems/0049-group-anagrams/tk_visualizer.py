#!/usr/bin/env python3
"""
Simple Group Anagrams Visualizer
"""

import tkinter as tk
from tkinter import ttk
import time
from collections import defaultdict

class GroupAnagramsVisualizer:
    def __init__(self, root):
        self.root = root        
        self.root.title("Group Anagrams Visualizer")
        self.root.geometry("800x600")
        self.root.config(bg="#f5f5f5")
        
        # Data
        self.strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.steps = []
        self.current_step = 0
        self.is_playing = False
        self.approach = "sorting"  # or "counting" or "prime"
        
        # Setup UI
        self.setup_ui()
        
        # Generate steps for initial view
        self.generate_steps()
        self.update_view()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = ttk.Label(main_frame, text="Group Anagrams Visualizer", font=("Arial", 16, "bold"))
        title.pack(pady=10)
          # Approach selection
        approach_frame = ttk.Frame(main_frame)
        approach_frame.pack(pady=10)
        
        ttk.Label(approach_frame, text="Algorithm Approach:").pack(side=tk.LEFT, padx=5)
        self.approach_var = tk.StringVar(value="sorting")
        
        ttk.Radiobutton(
            approach_frame, 
            text="Sorting Approach",
            variable=self.approach_var,
            value="sorting",
            command=self.change_approach
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            approach_frame, 
            text="Character Counting",
            variable=self.approach_var,
            value="counting",
            command=self.change_approach
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            approach_frame, 
            text="Prime Number Encoding",
            variable=self.approach_var,
            value="prime",
            command=self.change_approach
        ).pack(side=tk.LEFT, padx=5)
        
        # Input strings display
        input_frame = ttk.LabelFrame(main_frame, text="Input Strings")
        input_frame.pack(fill=tk.X, pady=10)
        
        self.input_display = ttk.Frame(input_frame)
        self.input_display.pack(fill=tk.X, pady=5, padx=5)
        
        # Controls
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(pady=10)
        
        self.play_button = ttk.Button(
            control_frame,
            text="▶ Play",
            command=self.toggle_play,
            width=10
        )
        self.play_button.pack(side=tk.LEFT, padx=5)
        
        self.prev_button = ttk.Button(
            control_frame,
            text="◀ Previous",
            command=self.prev_step,
            width=10
        )
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = ttk.Button(
            control_frame,
            text="Next ▶",
            command=self.next_step,
            width=10
        )
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = ttk.Button(
            control_frame,
            text="⟲ Reset",
            command=self.reset,
            width=10
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        # Step indicator
        self.step_label = ttk.Label(main_frame, text="Step 1 of X")
        self.step_label.pack(pady=5)
        
        # Step description
        self.description_frame = ttk.LabelFrame(main_frame, text="Current Step")
        self.description_frame.pack(fill=tk.X, pady=5)
        
        self.description_label = ttk.Label(
            self.description_frame, 
            text="",
            wraplength=780
        )
        self.description_label.pack(pady=5, padx=5)
        
        # Processing details (optional showing)
        self.details_frame = ttk.LabelFrame(main_frame, text="Processing Details")
        # Not packed initially - will show only when needed
        
        self.details_label = ttk.Label(
            self.details_frame, 
            text="",
            wraplength=780
        )
        self.details_label.pack(pady=5, padx=5)
        
        # Split view for hashmap and result
        split_frame = ttk.Frame(main_frame)
        split_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Hashmap view
        hashmap_frame = ttk.LabelFrame(split_frame, text="HashMap")
        hashmap_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.hashmap_text = tk.Text(hashmap_frame, height=8, wrap=tk.WORD)
        self.hashmap_text.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)
        
        # Result view
        result_frame = ttk.LabelFrame(split_frame, text="Result")
        result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.result_text = tk.Text(result_frame, height=8, wrap=tk.WORD)
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)
        
        # Complexity analysis
        complexity_frame = ttk.LabelFrame(main_frame, text="Complexity Analysis")
        complexity_frame.pack(fill=tk.X, pady=10)
        self.complexity_label = ttk.Label(
            complexity_frame, 
            text="",
            wraplength=780
        )
        self.complexity_label.pack(pady=5, padx=5)
        
    def generate_steps(self):
        """Generate step-by-step process for visualization"""
        if self.approach == "sorting":
            self.generate_sorting_steps()
            self.update_complexity_text(
                "Time: O(N×M log M) - N strings with average length M\n" +
                "Space: O(N×M) for storing the groups\n" +
                "Key operation: Sorting each string (M log M)"
            )
        elif self.approach == "counting":
            self.generate_counting_steps()
            self.update_complexity_text(
                "Time: O(N×M) - N strings with average length M\n" +
                "Space: O(N×M) for storing the groups + O(1) for count array\n" +
                "Key operation: Character counting (M)"
            )
        else:  # prime number approach
            self.generate_prime_steps()
            self.update_complexity_text(
                "Time: O(N×M) - N strings with average length M\n" +
                "Space: O(N×M) for storing the groups\n" +
                "Key operation: Mathematical prime product (higher constant factor)"
            )

    def generate_sorting_steps(self):
        """Generate steps for the sorting approach"""
        self.steps = []
        hashmap = {}
        result = []
        
        # Initial step
        self.steps.append({
            "description": "Initialize an empty hashmap and result array",
            "hashmap": {},
            "result": [],
            "current_string": None,
            "current_key": None,
            "details": None
        })
        
        # Process each string
        for string in self.strings:
            # Start processing
            self.steps.append({
                "description": f"Processing string: \"{string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": None
            })
            
            # Sort characters to create key
            sorted_string = ''.join(sorted(string))
            
            # Show sorting process
            self.steps.append({
                "description": f"Sorting \"{string}\" to create a key",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": sorted_string,
                "details": f"Original: \"{string}\" → Sorted: \"{sorted_string}\""
            })
            
            # Add to hashmap
            if sorted_string not in hashmap:
                hashmap[sorted_string] = []
            hashmap[sorted_string].append(string)
            
            # Show adding to hashmap
            self.steps.append({
                "description": f"Adding \"{string}\" to hashmap with key \"{sorted_string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": sorted_string,
                "details": None
            })
        
        # Final result
        result = list(hashmap.values())
        self.steps.append({
            "description": "Converting hashmap values to final result array",
            "hashmap": hashmap.copy(),
            "result": result.copy(),
            "current_string": None,
            "current_key": None,
            "details": None
        })

    def generate_counting_steps(self):
        """Generate steps for the character counting approach"""
        self.steps = []
        hashmap = {}
        result = []
        
        # Initial step
        self.steps.append({
            "description": "Initialize an empty hashmap and result array",
            "hashmap": {},
            "result": [],
            "current_string": None,
            "current_key": None,
            "details": None
        })
        
        # Process each string
        for string in self.strings:
            # Start processing
            self.steps.append({
                "description": f"Processing string: \"{string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": None
            })
            
            # Count characters
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            
            # Show character counting
            freq_display = {}
            for char in string:
                freq_display[char] = freq_display.get(char, 0) + 1
                
            freq_details = ", ".join([f"'{char}': {count}" for char, count in freq_display.items()])
            
            self.steps.append({
                "description": f"Counting character frequencies in \"{string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": f"Character frequencies: {freq_details}"
            })
            
            # Create key from character count
            key = tuple(char_count)
            key_display = ",".join([str(n) for n in char_count])
            
            # Show key creation
            self.steps.append({
                "description": f"Creating key from character frequency array",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": key,
                "details": f"Key (frequency array): [{key_display}]"
            })
            
            # Add to hashmap
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)
            
            # Show adding to hashmap
            self.steps.append({
                "description": f"Adding \"{string}\" to hashmap with frequency-based key",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": key,
                "details": None
            })
        
        # Final result
        result = list(hashmap.values())
        self.steps.append({
            "description": "Converting hashmap values to final result array",
            "hashmap": hashmap.copy(),
            "result": result.copy(),
            "current_string": None,
            "current_key": None,
            "details": None
        })

    def generate_prime_steps(self):
        """Generate steps for the prime number encoding approach"""
        # First 26 prime numbers for a-z
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
                  
        self.steps = []
        hashmap = {}
        result = []
        
        # Initial step
        self.steps.append({
            "description": "Initialize an empty hashmap and result array",
            "hashmap": {},
            "result": [],
            "current_string": None,
            "current_key": None,
            "details": None
        })
        
        # Process each string
        for string in self.strings:
            # Start processing
            self.steps.append({
                "description": f"Processing string: \"{string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": None
            })
            
            # Display prime number assignment
            prime_assignment = []
            for char in "abcdefghijklmnopqrstuvwxyz":
                idx = ord(char) - ord('a')
                prime_assignment.append(f"'{char}' → {primes[idx]}")
            
            self.steps.append({
                "description": f"Assigning prime numbers to characters",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": "Prime assignments: " + ", ".join(prime_assignment[:5]) + "..."
            })
            
            # Calculate the product of primes for this string
            prime_product = 1
            char_primes = {}
            
            for char in string:
                idx = ord(char) - ord('a')
                prime = primes[idx]
                prime_product *= prime
                char_primes[char] = prime
            
            # Show the prime calculation
            prime_calc = []
            for char in string:
                prime_calc.append(f"'{char}': {char_primes[char]}")
                
            self.steps.append({
                "description": f"Calculating prime product for \"{string}\"",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": None,
                "details": f"Prime products: {' × '.join(prime_calc)} = {prime_product}"
            })
            
            # Use product as key
            key = prime_product
            
            self.steps.append({
                "description": f"Using prime product {key} as key",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": key,
                "details": f"Key (prime product): {key}"
            })
            
            # Add to hashmap
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)
            
            # Show adding to hashmap
            self.steps.append({
                "description": f"Adding \"{string}\" to hashmap with prime product key",
                "hashmap": hashmap.copy(),
                "result": result.copy(),
                "current_string": string,
                "current_key": key,
                "details": None
            })
        
        # Final result
        result = list(hashmap.values())
        self.steps.append({
            "description": "Converting hashmap values to final result array",
            "hashmap": hashmap.copy(),
            "result": result.copy(),
            "current_string": None,
            "current_key": None,
            "details": None
        })

    def update_view(self):
        """Update the visualization based on the current step"""
        if not self.steps or self.current_step >= len(self.steps):
            return
            
        step = self.steps[self.current_step]
        
        # Update step indicator
        self.step_label.config(text=f"Step {self.current_step + 1} of {len(self.steps)}")
        
        # Update description
        self.description_label.config(text=step["description"])
        
        # Update input string display
        for widget in self.input_display.winfo_children():
            widget.destroy()
            
        for string in self.strings:
            # Create a label for each string
            bg_color = "#e1f0fa" if string == step["current_string"] else "#ffffff"
            string_label = ttk.Label(
                self.input_display,
                text=f'"{string}"',
                background=bg_color,
                padding=5,
                borderwidth=1,
                relief="solid"
            )
            string_label.pack(side=tk.LEFT, padx=3, pady=3)
        
        # Update details if available
        if step["details"]:
            self.details_frame.pack(fill=tk.X, pady=5)
            self.details_label.config(text=step["details"])
        else:
            self.details_frame.pack_forget()
          # Update hashmap view
        self.hashmap_text.config(state=tk.NORMAL)
        self.hashmap_text.delete(1.0, tk.END)
        
        if not step["hashmap"]:
            self.hashmap_text.insert(tk.END, "Empty hashmap")
        else:
            for key, values in step["hashmap"].items():
                key_str = str(key)
                # Handle large prime product keys by showing scientific notation
                if isinstance(key, int) and key > 1000000 and self.approach == "prime":
                    key_str = f"{key:e}"
                elif len(key_str) > 20:
                    key_str = key_str[:20] + "..."
                    
                self.hashmap_text.insert(tk.END, f"Key: {key_str}\n")
                self.hashmap_text.insert(tk.END, f"Values: {values}\n\n")
        
        self.hashmap_text.config(state=tk.DISABLED)
        
        # Update result view
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        
        if not step["result"]:
            self.result_text.insert(tk.END, "Result array is empty")
        else:
            for i, group in enumerate(step["result"]):
                self.result_text.insert(tk.END, f"Group {i+1}: {group}\n")
        
        self.result_text.config(state=tk.DISABLED)
        
        # Update button states
        self.prev_button.config(state=tk.DISABLED if self.current_step == 0 else tk.NORMAL)
        self.next_button.config(state=tk.DISABLED if self.current_step == len(self.steps) - 1 else tk.NORMAL)

    def next_step(self):
        """Go to the next step"""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_view()

    def prev_step(self):
        """Go to the previous step"""
        if self.current_step > 0:
            self.current_step -= 1
            self.update_view()

    def reset(self):
        """Reset to the beginning"""
        self.current_step = 0
        self.is_playing = False
        self.play_button.config(text="▶ Play")
        self.update_view()

    def toggle_play(self):
        """Start/stop automatic playback"""
        self.is_playing = not self.is_playing
        
        if self.is_playing:
            self.play_button.config(text="⏸ Pause")
            self.play_animation()
        else:
            self.play_button.config(text="▶ Play")

    def play_animation(self):
        """Animate through steps"""
        if not self.is_playing:
            return
            
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_view()
            self.root.after(1500, self.play_animation)
        else:
            self.is_playing = False
            self.play_button.config(text="▶ Play")

    def change_approach(self):
        """Switch between sorting and counting approaches"""
        self.approach = self.approach_var.get()
        self.reset()
        self.generate_steps()
        self.update_view()
        
    def update_complexity_text(self, text):
        """Update complexity analysis text"""
        self.complexity_label.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = GroupAnagramsVisualizer(root)
    root.mainloop()
