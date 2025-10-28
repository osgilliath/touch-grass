# touch-grass

A program to track your usage, including the apps you use, how long do you use them for and even the tabs you were using inside them, cause in the age of technology, nothing is hidden.<br/>
Trust me bro, privacy is a myth.

_touch-grass.py_ program, after running, tracks your usage and screen time,<br/>
 including the apps you used and the tabs, and for how long, and stores it in a .json file

_report.py_ program, parses that .json file and displays it in a neat format, for everyone to see what you've been up to

## libraries-required
- `psutil`
- `pygetwindow`
- `pyrect`

but why tf do you care,

## running instructions
- Just install the required libraries by running:

`pip install -r requirements.txt`

make sure you're in the program directory, then

- Just run the _touch-grass.py_ file by:<br/>

`python touch-grass.py` 

leave the rest in the hands of the Python Gods.

The tracking will start, and can be stopped whenever you want by pressing _Ctrl+C_ in the terminal.<br/>
The usage logs of the tracking will be stored in a .json file, and be displayed in the terminal automatically.

## eventually
_read that in spongebob narrator voice_

Will eventually make it so that, every iteration of tracking will make a new log file, and store results separately, so that you can access previous results as well.<br/>
So, that it can be a full fledged program, that runs as soon as you boot, until you turn off. (not that I want all your usage data *evil laugh*)<br/>
Just figuring out the way to implement it for now.

Thank you for reading through this and trying out the program (if you did), adios!!