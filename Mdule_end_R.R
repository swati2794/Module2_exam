
x<-20:50
print("Sequence of 20 to 50 number is:")
x
y<- mean(20:60)
print("mean of 20 to 60 number is:")
y
z<-sum(51:91)
print("sum of 51 to 91 number is:")
z



for (n in 1:100){
  if(n%%3==0 & n%%5==0){print("FizzBuzz")}
  else if( n%%3==0){print("Fizz")}
  else if(n%%5==0){print("Buzz")}
  else{print(n)}
}


