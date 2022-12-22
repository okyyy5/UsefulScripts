
## Usage

Needs Python 3.10 but you can probably get away with less.

By default the application is in Dry Run so it won't make any changes until you set it as follows: DRY_RUN: bool = False

Set the semester_weeks variable to however many weeks there are in the semester: SEMESTER_WEEKS: int = 13 - by default it is 12 weeks.

#### Run the application from Command Line as follows:

python UniFolderCreator.py (Directory path to your Folder Year such as 2022 Semester 1)

Another example:

python UniFolderCreator.py C:\Users\Gabe\Desktop\2022Semester1


If the folder for your provided directory doesn't exist (such as 2022Semester1 not existing) then the script will prompt you with (y/n) to create it automatically, however, you must create the subject folders yourself. Best way to do it is making your directories as shown below before running the script.


#### This is what your directory should look like before running the script.
```
├── 2022 Semester 1
|	├── Class 1
|	├── Class 2
|	├── Class 3
|	├── Class 4
```

After running the script on the directory this is what it becomes. One folder is made for each week in the semester.
```
├── 2022 Semester 1
|	├── Class 1
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Class 2
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Class 3
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Class 4
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
```

