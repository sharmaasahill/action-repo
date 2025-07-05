"""
TechStax Assessment - Sample Code
This file demonstrates webhook functionality when modified.
"""

def greet_user(name):
    """
    A simple greeting function for demonstration
    """
    return f"Hello, {name}! Welcome to TechStax Assessment."

def main():
    """
    Main function to demonstrate the application
    """
    print("=" * 50)
    print("TechStax Assessment - GitHub Webhook Demo")
    print("=" * 50)
    
    # Sample user greeting
    user_name = "Developer"
    greeting = greet_user(user_name)
    print(greeting)
    
    # Sample calculations
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"\nSample calculations:")
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    
    print("\nWebhook events will be triggered when this file is modified!")
    print("Check the webhook receiver application to see the events.")

if __name__ == "__main__":
    main()