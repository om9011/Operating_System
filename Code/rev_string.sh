read -p "Enter a string: " input_string

length=${#input_string}
reversed=""

for (( i=$length-1; i>=0; i-- )); do
    reversed="${reversed}${input_string:$i:1}"
done

echo "Reversed string: $reversed"

