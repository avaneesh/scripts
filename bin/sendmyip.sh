#!/bin/bash

send_myemail()
{
  TO=$1
  eval SUBJECT='$'$2

  # temporary file to hold email content
  local MAIL_BODY_FILE=/$HOME/mail-body`date +%F-%T`

  echo -e "To: ${TO}" >> $MAIL_BODY_FILE
  echo -e "Subject: ${SUBJECT}" >> $MAIL_BODY_FILE

  echo Sending email: `cat $MAIL_BODY_FILE`
  /usr/lib/sendmail -oi -t < $MAIL_BODY_FILE

  #remove the temporary file
  rm $MAIL_BODY_FILE
}

my_ip=`ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'`
echo my ip is $my_ip
SUBJECT_L="avkrpi $my_ip"

send_myemail avaneesh.kadam@gmail.com SUBJECT_L
