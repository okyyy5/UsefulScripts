
### Usage

Needs Python 3.10 but you can probably get away with less.

Set the folder_dir variable to whatever the directory of your semester top level folder is. 
For example, `C:\Users\Oktay\Google Drive\2022 Sem 1`

Set the semester_weeks variable to however many weeks there are in the semester. 
For example, `14`

This is what your directory should look like before running the script.
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

