import smtplib

email="""pr@viu.tv
info@biohealth-plus.com.hk
support@deliveroo.hk
info@crown-motors.com
無Email，請去FB
無Email，請去官網
marketing@calbee.com.hk
無Email，請去FB
無Email，請去官網
官網Contact Us死link，請去FB
bluegirlbeercs@jebsen.com
webenquiry@osim.com.hk
無Email，請去官網
無Email，請去官網
inquiries@mentholatum.com.hk
enquiry@acuvue.com.hk
無Email，請去官網
無Email，請去官網
publicenquiry@hkma.gov.hk
fortress@asw.com.hk
無Email，請去官網
無Email，請去官網
kiehls.corphk@loreal.com
ateliercologne.csc@loreal.com
無Email，請去官網
無Email，請去官網
customerservice@octopus.com.hk
無Email，請去官網
info@biohealth-plus.com.hk
hk.enquiry@thebodyshop.com
無Email，請去官網
無Email，請去官網
無Email，請去官網
無Email，請去官網
marketing@kaohk.com
無Email，請去官網
press.office@franciskurkdjian.com
manningscs@dairy-farm.com.hk
info@jag.com.hk
hello@bowtie.com.hk
無Email，請去官網
無Email，請去FB
promotion@citygateoutlets.com
gr@oceanpark.com.hk
enquiry@theclub.com.hk
hkcf@hkcf.org"""

email=email.split('\n')

valid=[]
for x in email:
	if '@'in x:
		valid.append(x)

# Gmail Sign In
gmail_sender = 'xxx@gmail.com'
gmail_passwd = 'xxxxxxxxxxxx'

SUBJECT = """Complaint about your company's spokesperson personal conduct """

TEXT = """To whom it may concern,\n
I am writing to lodge a serious complaint concerning the personal conduct of an artistes under your company-- Denis Kwok Ka Chun. According to information available on an open forum LIHKG, the manners in which he behaved when handling the reimbursement caused by a mistaken transfer by one of his fans was by no means satisfactory. It is seriously doubted whether he constantly performs proper conduct that a television personality should always be equipped.\n    
As indicated by screenshots from the victim, a lump sum amounting to about HKD300 dollars was transferred from the victim's Payme account to LILABOC's for purchasing merchandise more than a half of a year ago. No reply was received by the victim. Throughout the time interval of waiting for the product, the victim sent multiple requests of clarification for the current status of the delivery. The victim finally demanded a reimbursement of cost paid if it was still out of stock on the day of 25/8. Kwok then replied the victim with insulting wordings, such as "Do you know Chinese?", "Illiterate", "Or burn the money to you?" etc. This clearly deviates values of treating supporters with basic politeness that a regular entertainment company should always uphold. After expressing this set of ugly words, Kwok revealed the victim's Instagram account and phone number on Instagram story. This damages the public confidence of shopping in online shops having similar affiliation with related artistes. Furthermore, suspicion of whether this set of action has violated ordinances related to privacy protection stipulated by the Hong Kong Government arises. This mistreatment inflicted certain psychological damage on the victim and the general public.\n
As a television personality, virtues like magnanimity should always be demonstrated when engaging supporters. Kwok's offensive words should be deemed as unacceptable behaviour and not tolerated by your company. It is a reasonable assumption that artistes under your company's management  are reminded to satisfy basic professional expectations required by the public at all times and the occurrence of this incident clearly proves the failure of the execution of it. The public has been disappointed by his way of handling relationships with fans. It is hoped that response made by your company will not disappoint us one more time.\n 
Your attention to this matter is always highly appreciated.\n
Best regards """


for i in valid:
    TO = i
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)
    
    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    
    #try:
    server.sendmail(gmail_sender, [TO], BODY)
    print (f'email sent to {i}')
    #except:
    print ('error sending mail')

server.quit()
