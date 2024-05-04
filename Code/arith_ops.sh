echo "Select an arithmetic operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit"

read -p "Enter your choice (1/2/3/4/5): " choice

case $choice in
    1)
        read -p "Enter the first number: " num1
        read -p "Enter the second number: " num2
        result=$((num1 + num2))
        echo "Result: $result"
        ;;
    2)
        read -p "Enter the first number: " num1
        read -p "Enter the second number: " num2
        result=$((num1 - num2))
        echo "Result: $result"
        ;;
    3)
        read -p "Enter the first number: " num1
        read -p "Enter the second number: " num2
        result=$((num1 * num2))
        echo "Result: $result"
        ;;
    4)
        read -p "Enter the dividend: " dividend
        read -p "Enter the divisor: " divisor
        result=$(bc -l <<< "scale=2; $dividend / $divisor")
        echo "Result: $result"
        ;;
    5)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo "Invalid choice."
        ;;
esac

