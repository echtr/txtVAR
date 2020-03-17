# txtVAR
Database for files with .txt extension.
<br>

## Wiki:

#### Basics:
 - You do not need to put the extensions of the text files: database.txt => txtvar("database") 
 - Simply variable definition: var1 > var1value (You have to leave a space before and after the '>' sign.)
 - The append_var() function moves to the next line before defining a variable.


<br>
<br>


#### Functions:

| Function | Description | Usage |
| --- | --- | --- |
| variables() | Returns the variables in the file in dictionary type. | txtvar("database").variables() |
| numofvars() | Returns the total number of variables in the file. | txtvar("database").numofvars() |
| append_var() | Assigns a new variable to the file. | txtvar("database","name","your_name").append_var() |

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
