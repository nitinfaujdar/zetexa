import csv
from collections import defaultdict

def process_transaction_file(input_file='transaction.csv', output_file='user_totals.csv'):
    user_totals = defaultdict(int)
    try:
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, start=2):
                try:
                    user_id = int(row['user_id'])                    
                    amount = int(row['amount'])
                    user_totals[user_id] += amount
                except (KeyError, ValueError) as e:
                    print(f"Skipping malformed row {row_num}: {row} - Error: {e}")
                    continue
        
        with open(output_file, mode='w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['user_id', 'total_amount'])

            for user_id, total_amount in user_totals.items():
                writer.writerow([user_id, total_amount])

        print(f"Processed Successfully. Output written to {output_file}")
    
    except FileExistsError:
        print(f"Input file {input_file} not found")
    
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == '__main__':
    process_transaction_file()