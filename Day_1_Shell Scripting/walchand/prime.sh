echo "enter a number"
read num
if [ $num -eq 1 ]
then
echo "It is a prime number"
fi

if [ $num -eq 2 ]
then
echo "It is a prime number"
fi

for i in $(seq 2 $((num - 1)))
do
if [ $((num % i)) -eq 0 ];
then
echo "It is not prime number"
break
else
echo "It is a prime number"
break
fi
done
