from imbox import Imbox
import pikepdf
import os

host = "imap.gmail.com"
username = "mauriziobertucci282@gmail.com" #Gmail account
pwd_gmail = "hulmckyaifxfyctu" #Gmail password per le app --> https://myaccount.google.com/apppasswords
pwd_pdf = "4TNriDM" #Password pdf
path = "/Users/nico/Desktop/cedolino_dl" #Directory per il download del cedolino

def remove(file):
    #Rimozione della password dal PDF
    try:
        pdf = pikepdf.open(file, allow_overwriting_input=True)
        pdf.save(file)

    except:
        pdf = pikepdf.open(file, password=pwd_pdf, allow_overwriting_input=True)
        pdf.save(file)

def find_files():
    for i in os.listdir(path):
        if i.endswith(".pdf") or i.endswith(".PDF"):
            file = path + "/" + i
            remove(file)

def download_attachment():
    mail = Imbox(host, username=username, password=pwd_gmail, ssl=True, ssl_context=None, starttls=False)
    messages = mail.messages(sent_from='nicolo.bertucci@eng.it') #Mail del mittente

    for (uid, message) in messages:
        for idx, attachment in enumerate(message.attachments):
            try:
                att_fn = str(attachment.get('filename'))
                download_path = f"{path}/{att_fn}"
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())

            except:
                pass

        mail.delete(uid)

    #Rinomina file nel formato YYYYMM_cedolino.pdf
    for i in os.listdir(path):
        if i == att_fn:
            file = att_fn.split("_")
            os.rename(path + "/" + att_fn, path + "/" + file[1] + file[2] + "_cedolino.pdf")

    mail.logout()

    find_files()

if __name__ == '__main__':
    download_attachment()