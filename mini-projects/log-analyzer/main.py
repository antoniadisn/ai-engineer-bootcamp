from pathlib import Path

class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def read_and_count(self):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith("INFO"):
                self.log_counts["INFO"] += 1
            elif line.startswith("WARNING"):
                self.log_counts["WARNING"] += 1
            elif line.startswith("ERROR"):
                self.log_counts["ERROR"] += 1

    def print_summary(self):
        print("========= Log Summary =========")
        print(f"INFO: {self.log_counts['INFO']}")
        print(f"WARNING: {self.log_counts['WARNING']}")
        print(f"ERROR: {self.log_counts['ERROR']}")

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    log_file = script_dir / "sample_log.txt"
    analyzer = LogAnalyzer(log_file)
    analyzer.read_and_count()
    analyzer.print_summary()