function welcome(){
echo "Welcome to function"
}
welcome

echo "Function with arguments"
function addition(){
result=$(( $a + $b ))
echo $result
}
a=10
b=20
addition $a $b

echo "Function with return statement"
function returnFunction(){
return 1
}
returnFunction
res1=$?
echo $res1
