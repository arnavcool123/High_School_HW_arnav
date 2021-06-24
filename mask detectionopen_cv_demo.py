'''import datetime
from tkinter import *
import cv2

root=Tk()
root.geometry('1920x1080')
root.title('AI Mask Detector')
root.configure(background='#f2e6c2')

lb1 = Label(root, text=' Welcome to AI Mask Detection Program!! ', bg='#f2e6c2', fg='black', font=(None, 55))
lb1.place(x=50, y=20)

lb4 = Label(root, text=' Select the  video file or 0 or 1 to use webcam -->> ', bg='#f2e6c2', font=(None, 25))
lb4.place(x=45, y=230)

srkclip = 'C:/Users/arnav_4f0p59t/PycharmProjects/srk.mp4'
salmanclip = 'C:/Users/arnav_4f0p59t/PycharmProjects/Salman Khan.mp4'
classclip = 'C:/Users/arnav_4f0p59t/PycharmProjects/classroom.mp4'

clicked = StringVar()
clicked.set("0")
drop = OptionMenu(root, clicked, classclip, salmanclip, srkclip,"0", "1")
drop.place(x=800, y=240)

def ml():
    filename = clicked.get()
    if filename == '0':
        filename = int(filename)

    srkcascade = cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/srkcascade.xml')
    salmancascade = cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/salmancascade.xml')
    maincasscade= cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/maincascade.xml')

    cap = cv2.VideoCapture(filename)
    cap.set(3, 1920)
    cap.set(4, 1080)
    def empty(a):
        pass
    cv2.namedWindow('Video Feed: Press q to pause and click cross to close window')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        srk = srkcascade.detectMultiScale(gray, 15, 36)
        salman = salmancascade.detectMultiScale(gray, 15, 36)
        main = maincasscade.detectMultiScale(gray, 15, 36)

        for (x, y, w, h) in main:
            area = w*h
            if area > 500:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(frame, 'WARNING NO MASK', (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                print('Unknown Student was found to be not wearing mask. TAKE ACTION!')
                lb33 = Label(text='Caution Student was found to be not wearing mask. TAKE ACTION! See Terminal! ', fg='#FF0000', bg='#00C4FF', font=(None, 35))
                lb33.place(x=150, y=550)
                #winsound.Beep(800, 50)

        for (x, y, w, h) in salman:
            area = w*h
            if area > 500:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(frame, 'WARNING NO MASK', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                print('salman was found not wearing mask')

        for (x, y, w, h) in srk:
            area = w*h
            if area > 500:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(frame, 'WARNING NO MASK', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                print('sharukh was found to be not wearing mask. TAKE ACTION!')


        cv2.imshow('Video Feed: Press q to pause and click cross to close window', frame)


        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()

but1 = Button(root, text=' Click to launch webcam/video ', padx=10, pady=10, bg='#bcdba7', fg='black', font=(None, 25), command=ml)
but1.place(x=450, y=350)
lb2 = Label(root, text=' Press "q" to pause video and then close the window normally! ', bg='#f2e6c2', font=(None, 20))
lb2.place(x=400, y=480)
but2 = Button(root, text=' Click to Quit Application ', padx=10, pady=10, bg='#bcdba7', fg='black', font=(None, 25), command=root.destroy)
but2.place(x=1100, y=680)
a=datetime.datetime.now()
time="%s.%s" % (a.hour, a.minute) 
date=datetime.date.today()
print(date, time)

lb3 = Label(root, text=time+' hrs', bg='#f2e6c2', fg='#54a61c', font=(None,35))
lb3.place(x=100, y=600)
lb4 = Label(root, text=date, bg='#f2e6c2', fg='#54a61c', font=(None,35))
lb4.place(x=100, y=680)

root.mainloop()

#MAde by ARNAV SUMAN CLASS 11'''
r={
 "kind": "drive#file",
 "id": "1O2O66DQhAeqPKXbOyMKXtUVQHTejWIth",
 "name": "img-27-May-2021-09.50.22-0.jpg",
 "mimeType": "image/jpeg"
}
print(r['id'])

