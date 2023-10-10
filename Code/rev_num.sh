read -p "Enter a number: " number

reversed=""
length=${#number}

for (( i=$length-1; i>=0; i-- )); do
    reversed="${reversed}${number:$i:1}"
done

echo "Number in reverse order: $reversed"

