import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

serH=None
serA=None
def run_hydroponics():
    
    global serH,serA
    #initializing variables
    PH=[]
    WaterLevel=[]
    CO2=[]               # from aqua
    Temp=[]              # from aqua
    Humidity=[]          # from aqua
    H2OPO4=[]            # from aqua

    # Set up the serial connection (make sure to adjust the port)
    serH = serial.Serial('COM3', 9600, timeout=1) 
    #print(serH) 
    time.sleep(2) 
    
    serA = serial.Serial('COM3', 9600, timeout=1) 
    #print(serA) 
    time.sleep(2) 

    fig, axs = plt.subplots(3, 2, figsize=(10, 8))
    fig.suptitle('Hydroponics', fontsize=16)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.5, wspace=0.3)


    # Function to read and process serial data
    def read_serial(frame):
        try:
            
            data = serH.readline().decode('utf-8').strip()  
            #data=(PH,WaterLevel,CO2,Temp,Humidity,H2OPO4)
            data=data[1:-1]
            data=data.split(",")
            values = tuple([float(i) if i != ""  else np.NAN for i in data])
            ph,wl=values
            
            data = serA.readline().decode('utf-8').strip()  
            #data=(PH,WaterLevel,CO2,Temp,Humidity,H2OPO4)
            data=data[1:-1]
            data=data.split(",")
            values = tuple([float(i) if i != ""  else np.NAN for i in data])
            _,temp,_,_,co2,hum,h20po4=values      
            
            
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
            WaterLevel.append(wl)
            CO2.append(co2)
            Temp.append(temp)
            Humidity.append(hum)
            H2OPO4.append(h20po4)
            
            if len(PH) >= 15:
                PH.pop(0)
            if len(WaterLevel) >= 15:
                WaterLevel.pop(0)
            if len(CO2) >= 15:
                CO2.pop(0)
            if len(Temp) >= 15:
                Temp.pop(0)
            if len(Humidity) >= 15:
                Humidity.pop(0)
            if len(H2OPO4) >= 15:
                H2OPO4.pop(0)
                
            for ax in axs.flat:
                ax.clear()  # Clear previous frame

            # Plot each sensor's values, calculate the average, and display it with spacing
            if PH:
                avg_pH = np.mean(PH)
                axs[0, 0].plot(PH,'r-', label="pH", linewidth=2, marker='o', markersize=4)
                axs[0, 0].text(0.5, 1.05, f"Avg: {avg_pH:.2f}", ha='center', va='center', transform=axs[0, 0].transAxes, fontsize=10)  # Add space above the title
                axs[0, 0].set_title("pH Sensor", pad=20)  # Add space below the avg value
                axs[0, 0].legend()
                axs[0, 0].grid(True)

            if WaterLevel:
                avg_wl = np.mean(WaterLevel)
                axs[0, 1].plot(WaterLevel,'g-', label="Water Level", linewidth=2, marker='o', markersize=4)
                axs[0, 1].text(0.5, 1.05, f"Avg: {avg_wl:.2f}", ha='center', va='center', transform=axs[0, 1].transAxes, fontsize=10)
                axs[0, 1].set_title("Water Level Sensor", pad=20)
                axs[0, 1].legend()
                axs[0, 1].grid(True)

            if CO2:
                avg_CO2 = np.mean(CO2)
                axs[1, 0].plot(CO2,'o-', label="CO2", linewidth=2, marker='o', markersize=4)
                axs[1, 0].text(0.5, 1.05, f"Avg: {avg_CO2:.2f}", ha='center', va='center', transform=axs[1, 0].transAxes, fontsize=10)
                axs[1, 0].set_title("CO2 Sensor", pad=20)
                axs[1, 0].legend()
                axs[1, 0].grid(True)

            if Temp:
                avg_Temp = np.mean(Temp)
                axs[1, 1].plot(Temp, 'b-',label="Temp", linewidth=2, marker='o', markersize=4)
                axs[1, 1].text(0.5, 1.05, f"Avg: {avg_Temp:.2f}", ha='center', va='center', transform=axs[1, 1].transAxes, fontsize=10)
                axs[1, 1].set_title("Temp Sensor", pad=20)
                axs[1, 1].legend()
                axs[1, 1].grid(True)

            if Humidity:
                avg_hum= np.mean(Humidity)
                axs[2, 0].plot(Humidity, 'c-', label="Humidity", linewidth=2, marker='o', markersize=4)
                axs[2, 0].text(0.5, 1.05, f"Avg: {avg_hum:.2f}",ha='center', va='center', transform=axs[2, 0].transAxes, fontsize=10)
                axs[2, 0].set_title("Humidity Sensor", pad=20)
                axs[2, 0].legend()
                axs[2, 0].grid(True)

            if H2OPO4:
                avg_h2opo4 = np.mean(H2OPO4)
                axs[2, 1].plot(H2OPO4, label="H2OPO4", linewidth=2, marker='o', markersize=4)
                axs[2, 1].text(0.5, 1.05, f"Avg: {avg_h2opo4:.2f}", ha='center', va='center', transform=axs[2, 1].transAxes, fontsize=10)
                axs[2, 1].set_title("Water PH Sensor", pad=20)
                axs[2, 1].legend()
                axs[2, 1].grid(True)

                    
        except KeyboardInterrupt:
            print("Exiting...")
            serH.close()
            serA.close()

            
        return None
    global ani
    ani = animation.FuncAnimation(fig, read_serial, interval=1000, cache_frame_data=False)

    # Read data continuously and update the plot
    #plt.show()
    #ser.close()
        
    return fig
