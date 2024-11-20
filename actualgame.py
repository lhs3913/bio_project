import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Define the possible animals and body parts
animals = ['Lion', 'Tiger', 'Bear']
radiation_types = ['Alpha Radiation', 'Beta Radiation', 'Gamma Radiation']
body_parts = ['Eyes', 'Ears', 'Tail', 'Legs', 'Paws']
mutation_by_body_part = {
    'Eyes': ['Eagle Eyes', 'Dog Eyes', 'Cat Eyes'],
    'Ears': ['Bat Ears', 'Wolf Ears', 'Elephant Ears'],
    'Tail': ['Dragon Tail', 'Fox Tail', 'Lion Tail'],
    'Legs': ['Cheetah Legs', 'Kangaroo Legs', 'Elephant Legs'],
    'Paws': ['Bear Paws', 'Tiger Paws', 'Lion Paws']
}

# Global variables to store selections
chosen_animal = None
chosen_radiation = None
mutation_occurred = False
chosen_body_part = None
chosen_body_part_mutation = None

# Mutation chance values for each radiation type (hardcoded, not adjustable by the user)
mutation_chances = {
    'Alpha Radiation': 0.3,  # 30% chance
    'Beta Radiation': 0.5,  # 50% chance
    'Gamma Radiation': 0.7  # 70% chance
}


# Function to randomly choose an animal
def random_animal():
    global chosen_animal
    chosen_animal = random.choice(animals)
    animal_label.config(text=f"Animal: {chosen_animal}")
    update_image(chosen_animal, "No Mutation")


# Function to randomly choose a radiation type
def random_radiation():
    global chosen_radiation
    chosen_radiation = random.choice(radiation_types)
    radiation_label.config(text=f"Radiation: {chosen_radiation}")

    # Display the mutation chance for the selected radiation type
    mutation_chance_label.config(text=f"Mutation Chance: {mutation_chances[chosen_radiation]:.0%}")


# Function to simulate whether a mutation happens
def check_for_mutation():
    global mutation_occurred
    if chosen_radiation:
        mutation_chance = mutation_chances[chosen_radiation]
        mutation_occurred = random.random() < mutation_chance
        mutation_label.config(text="Mutation: " + ("Yes" if mutation_occurred else "No"))


# Function to randomly select a body part for mutation
def select_random_body_part():
    global chosen_body_part
    chosen_body_part = random.choice(body_parts)
    body_part_label.config(text=f"Body Part: {chosen_body_part}")
    return chosen_body_part  # Return the mutated body part


# Function to randomly select a mutation for the chosen body part
def select_random_body_part_mutation():
    global chosen_body_part_mutation
    if chosen_body_part:
        chosen_body_part_mutation = random.choice(mutation_by_body_part[chosen_body_part])
        body_part_mutation_label.config(text=f"Mutation: {chosen_body_part_mutation}")
        update_image(chosen_animal, chosen_body_part_mutation)


# Function to update the image based on selected animal and mutation
def update_image(animal, mutation):
    try:
        base_image = Image.open(f'{animal.lower()}.png')  # Assuming image files are named 'lion.png', etc.
        mutation_image_path = f'{animal.lower()}_{mutation.replace(" ", "_").lower()}.png'

        try:
            mutation_image = Image.open(mutation_image_path)
            # Overlay the mutation onto the base image (using transparency for proper overlay)
            base_image.paste(mutation_image, (0, 0), mutation_image)
        except FileNotFoundError:
            print(f"Mutation image {mutation_image_path} not found. Using base image.")

        # Convert to a format suitable for Tkinter and update the label
        tk_image = ImageTk.PhotoImage(base_image)
        image_label.config(image=tk_image)
        image_label.image = tk_image  # Keep a reference to avoid garbage collection
    except FileNotFoundError:
        print(f"Base image {animal.lower()}.png not found.")


# Create the main window
root = tk.Tk()
root.title('Animal Mutation Spinner')

# Set a fixed size for the window
root.geometry("400x850")

# Label for showing the animal
animal_label = tk.Label(root, text="Animal: ", font=('Arial', 12))
animal_label.pack(pady=10)

# Button to randomly choose an animal
random_animal_button = tk.Button(root, text="Choose Random Animal", command=random_animal, font=('Arial', 12))
random_animal_button.pack(pady=10)

# Label for showing the radiation type
radiation_label = tk.Label(root, text="Radiation: ", font=('Arial', 12))
radiation_label.pack(pady=10)

# Button to randomly choose a radiation type
random_radiation_button = tk.Button(root, text="Choose Random Radiation", command=random_radiation, font=('Arial', 12))
random_radiation_button.pack(pady=10)

# Label to display the mutation chance for the selected radiation
mutation_chance_label = tk.Label(root, text="Mutation Chance: 50%", font=('Arial', 12))
mutation_chance_label.pack(pady=10)

# Label for showing whether mutation occurred
mutation_label = tk.Label(root, text="Mutation: ", font=('Arial', 12))
mutation_label.pack(pady=10)

# Button to check for mutation
check_mutation_button = tk.Button(root, text="Check for Mutation", command=check_for_mutation, font=('Arial', 12))
check_mutation_button.pack(pady=10)

# Label to display the mutation result (if mutation happens)
result_label = tk.Label(root, text="Mutation Result: ", font=('Arial', 12))
result_label.pack(pady=10)

# Label for showing the body part to mutate
body_part_label = tk.Label(root, text="Body Part: ", font=('Arial', 12))
body_part_label.pack(pady=10)

# Button to select a random body part for mutation
select_body_part_button = tk.Button(root, text="Select Random Body Part", command=select_random_body_part,
                                    font=('Arial', 12))
select_body_part_button.pack(pady=10)

# Label to show the body part mutation
body_part_mutation_label = tk.Label(root, text="Mutation: ", font=('Arial', 12))
body_part_mutation_label.pack(pady=10)

# Button to select a random mutation for the body part
select_body_part_mutation_button = tk.Button(root, text="Select Random Body Part Mutation",
                                             command=select_random_body_part_mutation, font=('Arial', 12))
select_body_part_mutation_button.pack(pady=10)

# Label to display the animal image
image_label = tk.Label(root)
image_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
