echo "enter a number: "
read num
digits=$(echo -n $num | wc -m)
temp=$num
sum=0
while [ $num -gt 0 ]
do
rem=$((num % 10))
sum=$((sum+rem**digits))
num=$((num / 10))
done

if [ $temp -eq $sum ]
then
echo "Armstrong Number"
else
echo "Not A Armstrong Number"
fi
