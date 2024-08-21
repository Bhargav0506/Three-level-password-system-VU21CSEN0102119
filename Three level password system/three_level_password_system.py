import random
import hashlib
import getpass

# Function to generate a one-time password (OTP)
def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

# Function to hash passwords using SHA-1
def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

# Function for the first level of authentication (Textual Password)
def level_one(username, stored_password):
    password = getpass.getpass("Enter your password: ")
    if hash_password(password) == stored_password:
        print("Level 1 authenticated.")
        return True
    else:
        print("Invalid password.")
        return False

# Function for the second level of authentication (Color Combination)
def level_two():
    colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
    print("Select a color combination (e.g., Red, Green, Blue):")
    print("Available colors:", colors)
    color_input = input("Enter your color combination: ").split(", ")
    if len(color_input) >= 2 and all(color in colors for color in color_input):
        print("Level 2 authenticated.")
        return True
    else:
        print("Invalid color combination.")
        return False

# Function for the third level of authentication (Image Ordering)
def level_three(images):
    print("Select the images in the correct order:")
    random_images = random.sample(images, len(images))
    print("Images (in random order):", random_images)
    user_selection = input("Enter the images in the correct order (comma-separated): ").split(", ")
    if user_selection == images:
        print("Level 3 authenticated.")
        return True
    else:
        print("Incorrect image order.")
        return False

# Main function to run the authentication system
def main():
    username = input("Enter your username: ")
    stored_password = hash_password("2119")  # Replace with actual stored password hash
    images = ["image1.jpg", "image2.jpg", "image3.jpg"]  # Replace with actual image filenames

    if level_one(username, stored_password):
        if level_two():
            if level_three(images):
                print("Access granted.")
            else:
                print("Access denied.")
        else:
            print("Access denied.")
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()