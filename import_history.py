import sys, json

from utils.spotify import search_track

def read_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())

def main():
    raw_data = read_file(sys.argv[1])
    print(search_track(raw_data[0]))
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_history.py <filename>")
        sys.exit(1)
        
    main()