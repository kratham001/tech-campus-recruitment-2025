import sys
import os
import mmap

def extract_logs(log_file, target_date):
    output_dir = "../output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = f"{output_dir}/output_{target_date}.txt"

    with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        # Memory-map the file for fast access
        with mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            for line in iter(mm.readline, b""):
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith(target_date):
                    outfile.write(decoded_line)
    
    print(f"Logs for {target_date} saved in {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    log_file = "test_logs.log"
    target_date = sys.argv[1]

    extract_logs(log_file, target_date)
