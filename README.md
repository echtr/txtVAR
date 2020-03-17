# txtDB
Database for files with .txt extension.
<br>

## Wiki:

#### Basics:
 - You do not need to put the extensions of the text files: database.txt => txtdb("database") 
 - Simply variable definition: x > y (You have to leave a space before and after the '>' sign.)


<br>
<br>


#### Functions:

| Function | Description | Usage |
| --- | --- | --- |
| variables() | Returns the variables in the file in dictionary type. | txtdb("database").variables() |
| numofvars() | Returns the total number of variables in the file. | txtdb("database").numofvars() |
| append_var() | Assigns a new variable to the file. | txtdb("database","name","your_name").append_var() |

<br>
<br>

#### Output:

```
database.txt:
developer > echtr
steam id > echtr
```

| Function | Output |
| --- | --- |
| variables() | {'developer':'echtr','steam id':'echtr'} |
| numofvars() | 2 |
