a,b=1,0
a=b=a^b
a=a^b
print(a)

#Let's break down the code you provided:

#```python
#a, b = 1, 0
#a = b = a ^ b
#a = a ^ b
#print(a)
#```

#Here's what happens step by step:

#1. `a, b = 1, 0`: This line initializes variables `a` and `b` with the values `1` and `0` respectively.

#2. `a = b = a ^ b`: In Python, `^` represents the bitwise XOR operator. `a ^ b` will result in `1` because `1 XOR 0` equals `1`. The expression `a = b = a ^ b` assigns the value of `1` to both `a` and `b`. After this line, `a` and `b` both become `1`.

#3. `a = a ^ b`: Now, `a` is `1`, and `b` is also `1`. `a ^ b` will be `0` because `1 XOR 1` equals `0`. So, `a` becomes `0` after this line.

#4. `print(a)`: Finally, it prints the value of `a`, which is `0`.

#Therefore, the output of the code is `0`.