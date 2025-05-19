import csv

def remove_commas_from_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [cell.replace(',', '') for cell in row]
            writer.writerow(new_row)

# Example usage
input_csv = 'Steamdb.csv'
output_csv = 'steamdb.csv'
remove_commas_from_csv(input_csv, output_csv)