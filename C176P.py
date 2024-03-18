from tkinter import*
import speedtest
import matplotlib as plt
import time
root = Tk()
root.title("Internet Stability")
root.geometry("500x500")

list_download_speed = []
list_upload_speed = []

for i in range(5):
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000, 2)
    list_download_speed.append(download_speed)
    upload_speed = round(st.upload()/1000000, 2)
    list_upload_speed.append(upload_speed)
    time.sleep(60)
    print(list_download_speed)
    print(list_upload_speed)

no = [1, 2, 3, 4, 5]    
plt.plot(no, list_download_speed, label = "Download speed")
plt.plot(no, list_upload_speed, label = "Upload speed")
plt.title("Speed")
plt.legend()
plt.show()
    
    



root.mainloop()