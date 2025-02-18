a=0
b=1
count=0
echo "enter a number"
read num

for i in $(seq 1 $((num)))
do
echo -n "$a "
c=$((a+b))
a=$b
b=$c
done

