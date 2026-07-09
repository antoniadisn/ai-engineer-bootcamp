def read_log_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def analyze_logs(lines):
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        if line.startswith("INFO"):
            log_counts["INFO"] += 1
        elif line.startswith("WARNING"):
            log_counts["WARNING"] += 1
        elif line.startswith("ERROR"):
            log_counts["ERROR"] += 1

    return log_counts


def print_summary(log_counts):
    print("========= Log Summary =========")
    print(f"INFO: {log_counts['INFO']}")
    print(f"WARNING: {log_counts['WARNING']}")
    print(f"ERROR: {log_counts['ERROR']}")


def main():
    file_path = "sample_log.txt"
    lines = read_log_file(file_path)
    log_counts = analyze_logs(lines)
    print_summary(log_counts)


main()