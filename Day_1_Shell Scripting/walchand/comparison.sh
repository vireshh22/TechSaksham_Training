echo "Please enter number1: "
read a
echo "Please enter number2: "
read b
if [ $a -gt $b ]
then
echo "$a is greater than $b"
else
echo "$b is greater than $a"
fi

