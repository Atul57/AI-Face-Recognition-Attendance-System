import os

dataset_path = "dataset"

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    # Skip files (only allow folders)
    if not os.path.isdir(person_folder):
        continue

    print("Training:", person_name)

    for img_name in os.listdir(person_folder):

        img_path = os.path.join(person_folder, img_name)

        print("Processing:", img_path)