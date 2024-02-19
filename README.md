# LineGraph
 A linear sequence line finder and creator for graphs

## Features
Currently it has the ability to save and load a set of coordinates from a .txt file. You can even exit the application!

## Using LineGraph
0.2.0 and lower are made with C++, later builds are with Python. As of updating, this currently does not have a general-use build that is a download-and-go option.
To run it, open up any Python compiler or IDE and select the "Run" option. To use the program effectively, please run from main.py as any other file will not make the program run properly!

## TODO
I want to make this an incredible project, and with graphs there's a lot to use. I'll detail all the ones I want here for now:
1. Have a linear sequence decoder (find x, y, gradient, y-intercept)
2. Give support for other sequences (quadratic, cubic, reciprocal)
3. Visualise all this on a GUI
4. 3D support? Maybe separate

## Message Level Priority
This is a little confusing, as my way of visualising what is and isn't important may be different to your use case, so I want to make it clear what each error level stand for when using the project.
0 - standard console output. No need for logging, as it will fill up with spam over time.
1 - debug. Generally for using when another problem exists
2 - warn. To mention in the log where a problem is likely to arise due to a lack of future-proofing or thought
3 - error. Where a problem will affect the intended result. Ideally this message is good, as it highlights where you would see red text.

## Issues/Feedback
Want to help me out with the project? Leave an issue or make a PR if you have an issue. Feedback is always appreciated, and you can leave requests if there's anything you want to see in the project I haven't already stated!