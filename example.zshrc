# If you want the example integration with the terminal (unix-based) that has
# the merge success and error outputs, here's my example.  Do with it what you will
PDFmerge() {
    output=$(python3 <your_file_path_here>/main.py 2> /dev/null) # /dev/null for "Multiple definitions in dictionary at byte 0x4c1b for key /PageMode" stderror?

    if [ $? -ne 0 ]; then
        echo "\033[31m\u001b[4m\u001b[1m-----MERGE FAILED-----\u001b[0m\n" >&2  # ANSI escape sequences for colors
        return 1
    fi

    echo "$output\n"
}