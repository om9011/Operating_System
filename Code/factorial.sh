calculate_factorial() {
    local num=$1
    local fact=1

    for ((i = 1; i <= num; i++)); do
        fact=$((fact * i))
    done

    echo "$fact"
}


read -p "Enter a number: " number


result=$(calculate_factorial $number)


echo "Factorial of $number is $result"

