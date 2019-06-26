Written by Kevin Lee (undergrad student worker for Josh/Frank/Rich) 2017-2019
Contact: kevincorvallis@gmail.com, 541-243-3053

# SPA.C

SPA.c is a C program for calculating different zenith and azimuthal angles from a given input. 

## Running the Program
The way I ran and edited this program consisted of 
'''bash
gcc spa.c 
./a.out
'''

There is an executable that has been created but ultimately will need to be re-compiled as this program is not 100% complete. 

Once run the .exe file it should start running a terminal and you should be able to start inputting dates and times. 


Where this project stands right now 2019 May 28th (Kevin Lee)
- The program compiles and run
- The time interval problem has not been completed. 


For those picking up from my work:
If you know a little C, great, it shouldn't take more than 20 minutes to understand what is happening. 

Essentially, you want to scroll down all the way down in spa.c to find the int main() function. This is what the computer first looks for and starts executing.

I initialize structs called ti, dt1, dt2. You'll understand these once you see the "Input Action". I'm saving all the inputs into  ti, dt1, dt2. 

If you scroll down below, you will see the "SPA CALCULATION" 
This is where the fun stuff is. I haven't really had the full extent to completely figure out the time interval solution. 

For now, you have the first loop that iterates through the days but obviously it's not always 30 so you'll have to figure out something with calendar months. 

The next while loop is essentially another loop that loops through the hour. At the bottom of the closing bracket you should see where I increment the hour. 

The next while loop is the minute. Again, inside the loop you should see where I am incrementing 1 to the min. 


The rest inside the loop is the actual calculation that is done. I have commented out the spa calculator came with but I am not using. Feel free to uncomment if you want it included in the output.txt

Ok now when you are writing and testing this spa calculation, there is a handy feature when you input something illegitament (ex. Hour 25, minute 61), the spa calculation will give you an error. I wrote for what time it is giving it that error and what is happening. Essentially it'll most likely be you're giving it wrong dates. 

The rest is pretty straight forward. Right now the latitude and longitude is set for Eugene, OR. I would create an array of list of stations with latitudes and longitudes and input them in spa.latitude, spa.longtitude.



Feel free to email me if you have any questions. 
https://github.com/klee0288/spa_program.git
