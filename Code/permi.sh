read -p "Enter a file path: " filepath

if [ -e "$filepath" ]; then
    echo "File exists."

    if [ -f "$filepath" ]; then
        echo "File type: Regular File"
    elif [ -d "$filepath" ]; then
        echo "File type: Directory"
    elif [ -b "$filepath" ]; then
        echo "File type: Block Special File"
    elif [ -c "$filepath" ]; then
        echo "File type: Character Special File"
    elif [ -L "$filepath" ]; then
        echo "File type: Symbolic Link"
    elif [ -p "$filepath" ]; then
        echo "File type: Named Pipe (FIFO)"
    elif [ -S "$filepath" ]; then
        echo "File type: Socket"
    fi


    permissions=$(ls -l "$filepath" | awk '{print $1}')
    echo "Permissions: $permissions"
else
    echo "File does not exist."
fi

