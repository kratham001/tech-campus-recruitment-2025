import sys
import os

def extract_logs(log_file, target_date):
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = f"{output_dir}/output_{target_date}.txt"

    with open(log_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line.startswith(target_date):  # Match the required date
                outfile.write(line)
    
    print(f"Logs for {target_date} saved in {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    log_file = "test_logs.log"
    target_date = sys.argv[1]

    extract_logs(log_file, target_date)
