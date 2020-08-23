def make_shirt(shirt_size, printed_message):
    """Display information about a shirt."""
    print(f"\nI will need a {shirt_size}.")
    print(f"I want the shirt to say {printed_message}.")

make_shirt('small', 'you are cool')
make_shirt(printed_message='awesome', shirt_size='medium')

def make_shirt(printed_message, shirt_size= 'large'):
    """Display information about a shirt."""
    print(f"\nI will need a {shirt_size}.")
    print(f"I want the shirt to say {printed_message}.")

make_shirt(printed_message='I love Python')

def make_shirt(shirt_size, printed_message='I love Python'):
    """Display information about a shirt."""
    print(f"\nI will need a {shirt_size}.")
    print(f"I want the shirt to say {printed_message}.")

make_shirt(shirt_size='medium')

