# CP Helper
A tool for competetive programming in sublime text.
# How to set it up?
- Install CP Companion plugin for Chrome and add port 8090 in its custom port settings.
- Clone this repository.
- Create a new build system in sublime text and copy paste the following. Then save it.
```
{
    "shell_cmd": "g++ \"${file}\" -o \"${file_path}/${file_base_name}\"",
    "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",
    "variants":
    [
        {
            "name": "Run",
            "shell_cmd": "timeout 3s python {Path where you cloned this repo}/CPHelper/Main.py \"${file_path}/${file_base_name}\""
        }
    ]
}
```
- In CPHelper.py change the TEMPLATE and baseContestPath according to your needs.
- Run CPHelper.py in the CPHelper directory.(And leave it running)
- When on a problem page click on the CP Companion plugin, it will parse the task data and open sublime text with your template.
- Write the code. Build and run using the new build system you made.
- create a input.txt file and change inputTxtPath in Main.py.
# input.txt
In this file you can enter a test case and it will be checked allong with the sample test cases of the problem.
To specify the correct output of this test case use --output. It will validate this test case with the provided output.
Example - 
```
4
2 4 5 7
--output
18
```
You can also use --add to add this test case to the set of sample test cases which are always checked.
Example - 
```
--add
4
2 4 5 7
--output
18
```
# To-Do
- Add testing of a task using brute force code and test case generator.
- Add special case for interactive problems.

# Screenshots
![](./Screenshots/screenshot1.png)

![](./Screenshots/Screenshot2.png)