# mail-broadcast
Mailing broadcast script aimed for internal uses only :p.

## setup credentials
Before running the script setup your google mail credentials in `settings.py`

## Usage
#### Required params:
- `-i` - To specify input csv file that contains emails, names of recipients. Example `-i Downloads/google-form.csv`
- `-c` - To specify file name that contains your email contents. This file must be place inside `app/templates/emails` folder. Example `-c xemail1.txt`

#### Flags
- `-gr` - Stands for `greeting`. If you want to use greeting template then specify this flag
- `-sfr` - Stands for `skip first row`. Default value for this flag is True, since first row of csv file (google form specifically) usually for header column, so we don't have to read the header column.
#### Optional params:
- `-s` - To specify email subject. Example `-s "Kabar gembira"`
- `-ecp` - Stands for `emai column position`. This is required if your email position in csv input file is other than 2. Example `-ecp 4`
- `-ncp` - Stands for `name column position`. This is required if you activate `-gr` flag. Default value for this param is 3, if your name column position is other than 3 than you have to specify the value fot this param. Example `-ncp 5`

## Supported Mail Server
- Google SMTP