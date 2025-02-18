echo "enter number of rows:"
read rows

for i in $(seq 1 $((rows)))
do
for j in $(seq 1 $((rows-i)) )
do
echo -n " "
done
for k in $(seq 1 $((i)))
do
echo -n "* "
done
echo ""
done
