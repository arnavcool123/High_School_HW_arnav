from tkinter import *
import cv2
import winsound

root1 = Tk()
root1.geometry('1920x1080')
root1.title('Drone Pollution Monitoring System')
root1.configure(background='white')

lb1 = Label(root1, text=' Welcome to Air Pollution Monitoring System!! ', bg='white', fg='green', font=(None, 35))
lb1.place(x=260, y=20)

lb4 = Label(root1, text='write the name of video file or 0 to use webcam -->> ', bg='white', font=(None, 15))
lb4.place(x=150, y=300)

ent1 = Entry(root1, width=29, bg='grey', font=(None, 25))
ent1.place(x=660, y=290)

#    Filenames
#    C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/60 Second Forest Fire.mp4
#    C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/China Aerials_ Industrial Lands,Factories,Exhaust Gas, Pollution in China.mp4
#    C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/Noida City __ 2021 __ Mini Japan of India __ View & Facts __ Debdut YouTube.mp4
#    C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/Smoke From Industries And Factories _ Air Pollution By Industries.mp4
def ml():
    filename = ent1.get()
    if filename == '0':
        filename = int(filename)
    airpollution_cascade = cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/20jancascade.xml')
    diwali_cascade = cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/21jancascade.xml')
    water_casscade = cv2.CascadeClassifier('C:/Users/arnav_4f0p59t/PycharmProjects/pythonProject1/22jancascade.xml')
    cap = cv2.VideoCapture(filename)
    cap.set(3, 1920)
    cap.set(4, 1080)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        airpollution = airpollution_cascade.detectMultiScale(gray, 10, 15)
        diwali = diwali_cascade.detectMultiScale(gray,10, 15)
        water = water_casscade.detectMultiScale(gray, 10, 15)

        for (x, y, w, h) in airpollution:
            area = w*h
            if area > 500:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(frame, 'Air Pollution Found', (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
                print('Caution Air Pollution Source Found. TAKE ACTION!')
                lb3 = Label(text='Caution Pollution Source Found. TAKE ACTION! See Terminal! ', fg='red', bg='white', font=(None, 35))
                lb3.place(x=150, y=550)
                #winsound.Beep(800, 50)

        for (x, y, w, h) in diwali:
            area = w*h
            if area > 1000:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
                cv2.putText(frame, 'Diwali Pollution Found', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
                print('Caution Diwali Pollution Source Found. TAKE ACTION!')

        for (x, y, w, h) in water:
            area = w*h
            if area > 1000:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                cv2.putText(frame, 'Water Pollution Found', (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
                print('Caution Water Pollution Source Found. TAKE ACTION!')


        cv2.imshow('Video Feed: Press q to pause and click cross to close window', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()

but1 = Button(root1, text=' Click to launch webcam/video ', padx=10, pady=10, bg='yellow', fg='black', font=(None, 25), command=ml)
but1.place(x=450, y=350)
lb2 = Label(root1, text=' Press "q" to pause video and then close the window normally! ', bg='white', font=(None, 20))
lb2.place(x=400, y=480)
but2 = Button(root1, text=' Click to Quit Application ', padx=10, pady=10, bg='yellow', fg='black', font=(None, 25), command=root1.destroy)
but2.place(x=1100, y=680)

root1.mainloop()
