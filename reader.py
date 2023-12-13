import sys
import os
import csv

class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.input_data = []

    def read_file_from_source(self):
        if os.path.isfile(self.input_file):
            with open(self.input_file) as file:
                reader = csv.reader(file)
                for row in reader:
                    self.input_data.append(row)
        else:
            print(os.listdir(self.input_file))
            print("Is not a file.")

    def change_data(self):
        for change in self.changes:
            changes_list = change.split(",")
            self.input_data[int(changes_list[0])][int(changes_list[1])] = changes_list[2]

    def write_data_to_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            writer.writerows(self.input_data)

if len(sys.argv) < 4:
    sys.exit(1)
input_file = sys.argv[1]
output_file = sys.argv[2]
changes = (sys.argv[3:])

file_handler = FileHandler (input_file, output_file, changes)
file_handler.read_file_from_source(input_file)
file_handler.change_data()
file_handler.run()
print(sys.argv)

input_folder = os.path.dirname(input_file)
if not os.path.exists(input_file):
    print(f"Error: Folder '{input_file}' does not exist.")
    sys.exit(1)

if not input_file.lower().endswith('.csv'):
    print(f"Error: '{input_file}' is not a CSV file. Here are the CSV files in the folder:")
    csv_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.csv')]
    if csv_files:
        print("\n".join(csv_files))
    else:
        print("No CSV files found in the folder.")
    sys.exit(1)
file_handler.run()



print("Changed data:")
print(f"{changes}")

print(f"\nModified CSV saved to '{output_file}'.")