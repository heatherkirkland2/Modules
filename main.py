# main.py
import text_utils as tu

def main():
    original_string = "hello, world!"

    # Using the reverse_string function
    reversed_result = tu.reverse_string(original_string)
    print(f"Reversed string: {reversed_result}")

    # Using the capitalize_string function
    capitalized_result = tu.capitalize_string(original_string)
    print(f"Capitalized string: {capitalized_result}")

if __name__ == "__main__":
    main()
