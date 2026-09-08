from pathlib import Path

def get_test_files():
    dir = Path("test/")
    test_files = [f for f in dir.glob("*test*") if f.is_file() and f.name != "conftest.py"]
    return test_files

def num_tests_in_file(file: Path):
    contents = file.read_text(encoding="utf-8")
    count = 0
    for line in contents.splitlines():
        line_words = line.strip().split()
        if len(line_words) > 1 and line_words[0] == "def" and line_words[1].startswith("test"):
            count += 1
    return count

def num_test_suites_in_file(file: Path):
    contents = file.read_text(encoding="utf-8")
    count = 0
    for line in contents.splitlines():
        line_words = line.strip().split()
        if len(line_words) > 1 and line_words[0] == "class" and line_words[1].lower().startswith("test"):
            count += 1
    return count

def main():
    test_files = get_test_files()
    total_suites = 0
    total_files = len(test_files)
    total_tests = 0
    tests_in_suites = 0
    print("Searching for test files...")
    for file in test_files:
        suites = num_test_suites_in_file(file)
        tests = num_tests_in_file(file)
        total_suites += suites
        total_tests += tests
        print(f"\tTest file found: {file.name}")
        print(f"\t\tNumber of test classes: {suites}")
        print(f"\t\tTotal number of tests: {tests}")
        if suites > 0:
            print(f"\t\tAverage tests per suite in file: {tests/suites}")
            tests_in_suites += tests
        print()

    print("")
    print(f"Found {total_tests} tests and {total_suites} test suites in {total_files} total test files.")
    if total_suites > 0: print(f"\tAverage tests per suite (only including tests in test classes): {tests_in_suites/total_suites}")
    if total_files > 0: print(f"\tAverage tests per file: {total_tests/total_files}")
    if total_files > 0: print(f"\tAverage suites per file: {total_suites/total_files}")

if __name__ == "__main__":
    main()


