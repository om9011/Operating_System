read -p "Enter the number of terms in the Fibonacci series: " n


a=0
b=1

echo "Fibonacci Series:"
echo -n "$a, $b"


for ((i=2; i<n; i++)); do
    next=$((a + b))
    echo -n ", $next"
    a=$b
    b=$next
done

echo "" 

