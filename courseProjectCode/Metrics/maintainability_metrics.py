from pathlib import Path

main_directory = Path("./pyinstrument") #only check the main code directory (not tests and docs)
file_extensions = {".py"} # focus on main python code files

total_loc = 0
total_comments = 0
file_count = 0

for path in sorted(main_directory.rglob("*")):
    if path.is_file() and path.suffix in file_extensions:
        try:
            with path.open("r", encoding="utf-8") as file:
                for line in file:
                    if line.strip():
                        total_loc += 1

                        if line.strip().startswith("#"):
                            total_comments += 1

                file_count += 1
        except:
            print(f"{path}: error reading file")

average_loc = total_loc / file_count # average LoC per file 
comment_density = total_comments / total_loc # proportion of total non-blank lines that are comment lines (comment density)

print(f"\nLoC / file: {average_loc}")
print(f"\nComment lines / total lines: {comment_density}")