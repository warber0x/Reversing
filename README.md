,# Live System Cracking


In this article, I will try to explain what I did to crack a license mechanism of a home automation system.
The machine contains linux Debian based and it runs under x86 architecture. The software that I was trying to crack is coded using Objective-C language. 

The first thing that I made is a plan containing the points that I should follow to make things go faster:
- Find the program responsible of checking the license.
- Use a disassembler like ADA Pro and try to see the flow of each function.
- Use a debugger: in this case I used GDB to see the behavior of the concerned function.
- Try to identify the value that make the program think that the license is valid.
- Try to change the value on the fly and to see what will happen.

The program uses a function called CheckLicense inside of another function which is called CheckAuthorization. Once the CheckLicense finishes, it returns a value that depends on whether the license is valid or not. When the license is not present or is not valid the register EAX = -84 and when is valid EAX = 10000. 

The challenge was, the function that examine the legitimacy of the license was always running each minute. So any manual modification on the register EAX will be overwritten by the next check. The solution was to create a Python Script that will inspect EAX if it has -84 value and change it by 10000 each time checkLicense terminates.

Another solution was to create a library that has the same behavior as the original one and returns the value that we want. However, this not ready yet. 

A video of demonstration is at this address: https://www.youtube.com/watch?v=myxcisebUZw

Thanks.



