import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

serV=None
def run_vermicompost():
    global serV
    #initializing variables
    Temp=[]
    PH=[]
    Humidity=[]
    CO2=[]

    # Set up the serial connection (make sure to adjust the port)
    serV = serial.Serial('COM3', 9600, timeout=1)  
    time.sleep(2) 

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Vermicompost', fontsize=16)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.5, wspace=0.3)


    # Function to read and process serial data
    def read_serial(frame):
        try:
            
            data = serV.readline().decode('utf-8').strip()  
            #data=(PH,WaterLevel,CO2,Temp,Humidity,H2OPO4)
            data=data[1:-1]
            data=data.split(",")
            values = tuple([float(i) if i != ""  else np.NAN for i in data])
            ph,hum,temp,co2=values
            
            
            """if(ph!=np.NAN):
                PH.append(ph)
            if(wl!=np.NAN):
                WaterLevel.append(wl)
            if(co2!=np.NAN):
                CO2.append(co2)
            if(temp!=np.NAN):
                Temp.append(temp)
            if(hum!=np.NAN):
                Humidity.append(hum)
            if(h20po4!=np.NAN):
                H2OPO4.append(h20po4)"""
            
            PH.append(ph)
            Humidity.append(hum)
            CO2.append(co2)
            Temp.append(temp)
            
            if len(PH) >= 15:
                PH.pop(0)
            if len(Humidity) >= 15:
                Humidity.pop(0)
            if len(CO2) >= 15:
                CO2.pop(0)
            if len(Temp) >= 15:
                Temp.pop(0)
            if len(Humidity) >= 15:
                Humidity.pop(0)
            
            for ax in axs.flat:
                ax.clear()  # Clear previous frame

            # Plot each sensor's values, calculate the average, and display it with spacing
            if PH:
                avg_ph = np.mean(PH)
                axs[0, 0].plot(PH,'r-', label="PH", linewidth=2, marker='o', markersize=4)
                axs[0, 0].text(0.5, 1.05, f"Avg: {avg_ph:.2f}", ha='center', va='center', transform=axs[0, 0].transAxes, fontsize=10)  # Add space above the title
                axs[0, 0].set_title("PH Sensor", pad=20)  # Add space below the avg value
                axs[0, 0].legend()
                axs[0, 0].grid(True)

            if Humidity:
                avg_hum = np.mean(Humidity)
                axs[0, 1].plot(Humidity,'g-', label="Humidity", linewidth=2, marker='o', markersize=4)
                axs[0, 1].text(0.5, 1.05, f"Avg: {avg_hum:.2f}", ha='center', va='center', transform=axs[0, 1].transAxes, fontsize=10)
                axs[0, 1].set_title("Humidity Sensor", pad=20)
                axs[0, 1].legend()
                axs[0, 1].grid(True)

            if Temp:
                avg_temp = np.mean(Temp)
                axs[1, 0].plot(Temp,'o-', label="Temp", linewidth=2, marker='o', markersize=4)
                axs[1, 0].text(0.5, 1.05, f"Avg: {avg_temp:.2f}", ha='center', va='center', transform=axs[1, 0].transAxes, fontsize=10)
                axs[1, 0].set_title("Temp Sensor", pad=20)
                axs[1, 0].legend()
                axs[1, 0].grid(True)

            if CO2:
                avg_co2 = np.mean(CO2)
                axs[1, 1].plot(CO2, 'b-',label="CO2", linewidth=2, marker='o', markersize=4)
                axs[1, 1].text(0.5, 1.05, f"Avg: {avg_co2:.2f}", ha='center', va='center', transform=axs[1, 1].transAxes, fontsize=10)
                axs[1, 1].set_title("CO2 Sensor", pad=20)
                axs[1, 1].legend()
                axs[1, 1].grid(True)
                    
        except KeyboardInterrupt:
            print("Exiting...")
            serV.close()
    global ani
    ani = animation.FuncAnimation(fig, read_serial, interval=1000, cache_frame_data=False)
    #plt.show()
    #ser.close()
    return fig
