import argparse
from startup import env
from app.mailing.send_general_email import send_general_email
from app.mailing.send_greeting_email import send_greeting_email
import csv

description = '''Mail broadcast sender, send email either general or with name greeting to recipients from csv file.
Write the email content and put it inside "app/templates/emails" folder, then let the script do the rest!
'''

def main():
  parser = argparse.ArgumentParser(description=description)

  parser.add_argument('-i', '--input', help='Specify csv input file that contains email address and/or name recipients', required=1)
  parser.add_argument('-gr', '--greeting', help='Specify this flag if you want to send email using name greeting template', action='store_true')
  parser.add_argument('-s', '--subject', help='Spesify subject', default='Berita')
  parser.add_argument('-c', '--content', help='Specify "file name" which contains email content that stored inside "app/templates/emails"', required=1)
  parser.add_argument('-ecp','--email_column_position', type=int, help='Specify position of email column in csv input file, default is 2 since first column usually for timestamps in google form. This is required if your email position is other than 2. \n*Note column starts from 1', default=2)
  parser.add_argument('-ncp', '--name_column_position', type=int, help='Specify position of email column in csv input file, default is 3. This is required if you use name greeting template. \n*Note column starts from 1', default=3)
  parser.add_argument('-sfr', '--skip_first_row', help='Usually first row is only header column, spesify this flag if you want to skip first row', action='store_true', default=True)
  
  args = parser.parse_args()

  email_column_position = args.email_column_position-1
  name_column_position = args.name_column_position-1

  subject = args.subject
  template = "emails/%s" % args.content
  content = env.get_template(template).render()
  
  input = open(args.input)
  reader = csv.reader(input)
  recipients = [(item[email_column_position], item[name_column_position]) for item in reader.__iter__()]
  input.close()

  if args.skip_first_row:
    recipients = recipients[1:]

  if args.greeting:
    print 'Sending greeting email'
    send_greeting_email(subject, content, recipients)
  else:
    print 'Sending general email'
    send_general_email(subject, content, map(lambda item: item[0], recipients))

if __name__ == '__main__':
  main()