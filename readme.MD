Convert playbook from CSV to JSON
===

### INSTALL
Clone repo, create env and install requirements.
### HOW TO USE IT
Python CLI with 3 args :
* the file name input : a CSV file with three columns (section, question type, question content) and no header. See below :
    ```csv
    resiliation,qa,Le client bénéficie t-il d'une clause XXX?
    notice,qa,Le client bénéficie t-il d'une clause de XXX?
    forcemajeure,qa,Le client bénéficie t-il d'une clause de XXX?
    notice,qa,Le client bénéficie t-il d'une clause de XXX?
    ```
* the playbook name : a string
* the file name output : a string that will be the name of the json file created by the script

Example :
```shell
python playbook_csvtojson.py "example.csv" "test" "example.json"
```
