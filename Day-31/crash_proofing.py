print("--- Secure Registration Portal ---")

try:
    name = input("Enter Student Name: ").strip().title()
    year_input = input("Enter Starting Year (YYYY): ")
    
    starting_year = int(year_input) 
    
    print(f"Success! {name} registered for the year {starting_year}.")

except ValueError:

    print("\n INPUT ERROR: You entered text where a number was required.")
    print(f"'{year_input}' is not a valid year. Please use numbers only (e.g., 2026).")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("\n--- Process Ended ---")