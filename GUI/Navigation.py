import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Aeroponics
import Aquaponics
import Vermicompost
import ControlPlant
import Hydroponics


# List of plotting functions from each module
programs = [Hydroponics.run_hydroponics, Aeroponics.run_aeroponics, Aquaponics.run_aquaponics]#,
            # Vermicompost.run_vermicompost, ControlPlant.run_controlplant]

current_index = 0
canvas = None

def load_program(index):
    
    global canvas
    # Clear the previous canvas if it exists
    if canvas:
        canvas.get_tk_widget().destroy()
        canvas = None

    # Call the function to get the figure
    fig = programs[index]()  # Should return only fig

    # Embed the figure in the tkinter frame (plot_frame)
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)  # Set master to plot_frame
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def next_program():
    global current_index
    
    # Handelling Serial Ports of system to manage conflicting ports operation 
    x=""" if Hydroponics.serH.is_open:
        print("Hydroponics Serial port is open.")
        Hydroponics.serH.close()
        print("Hydroponics Serial port Closed.")
    else: 
        print("Hydroponics Serial port is closed")
        
    if Aeroponics.serAe.is_open:
        print("Aeroponics Serial port is open.")
        Aeroponics.serAe.close()
        print("Aeroponics Serial port Closed.")
    else: 
        print("Aeroponics Serial port is closed")
        
    if Aquaponics.serAq.is_open:
        print("Aquaponics Serial port is open.")
        Aquaponics.serAq.close()
        print("Aquaponics Serial port Closed.")
    else: 
        print("Aquaponics Serial port is closed")
    
    if ControlPlant.serC.is_open:
        print("ControlPlant Serial port is open.")
        ControlPlant.serC.close()
        print("ControlPlant Serial port Closed.")
    else: 
        print("ControlPlant Serial port is closed")
        
    if Vermicompost.serV.is_open:
        print("VermiCompost Serial port is open.")
        Vermicompost.serV.close()
        print("Vermicompost Serial port Closed.")
    else: 
        print("VermiCompost Serial port is closed")
     """
    if Hydroponics.serH!=None:
        print("Hydroponics Serial port is open.")
        Hydroponics.serH.close()
        Hydroponics.serA.close()
        print("Hydroponics Serial port Closed.")
    else: 
        print("Hydroponics Serial port is closed")
        
    if Aeroponics.serAe!=None:
        print("Aeroponics Serial port is open.")
        Aeroponics.serAe.close()
        Aeroponics.serA.close()
        print("Aeroponics Serial port Closed.")
    else: 
        print("Aeroponics Serial port is closed")
        
    if Aquaponics.serAq!=None:
        print("Aquaponics Serial port is open.")
        Aquaponics.serAq.close()
        print("Aquaponics Serial port Closed.")
    else: 
        print("Aquaponics Serial port is closed")
    
    if ControlPlant.serC!=None:
        print("ControlPlant Serial port is open.")
        ControlPlant.serC.close()
        print("ControlPlant Serial port Closed.")
    else: 
        print("ControlPlant Serial port is closed")
        
    if Vermicompost.serV!=None:
        print("VermiCompost Serial port is open.")
        Vermicompost.serV.close()
        print("Vermicompost Serial port Closed.")
    else: 
        print("VermiCompost Serial port is closed")
    print("\n")    
       
    current_index = (current_index + 1) % len(programs)
    load_program(current_index)

def previous_program():
    global current_index
    
    # Handelling Serial Ports of system to manage conflicting ports operation 
    if Hydroponics.serH!=None:
        print("Hydroponics Serial port is open.")
        Hydroponics.serH.close()
        Hydroponics.serA.close()
        print("Hydroponics Serial port Closed.")
    else: 
        print("Hydroponics Serial port is closed")
        
    if Aeroponics.serAe!=None:
        print("Aeroponics Serial port is open.")
        Aeroponics.serAe.close()
        Aeroponics.serA.close()
        print("Aeroponics Serial port Closed.")
    else: 
        print("Aeroponics Serial port is closed")
        
    if Aquaponics.serAq!=None:
        print("Aquaponics Serial port is open.")
        Aquaponics.serAq.close()
        print("Aquaponics Serial port Closed.")
    else: 
        print("Aquaponics Serial port is closed")
    
    if ControlPlant.serC!=None:
        print("ControlPlant Serial port is open.")
        ControlPlant.serC.close()
        print("ControlPlant Serial port Closed.")
    else: 
        print("ControlPlant Serial port is closed")
        
    if Vermicompost.serV!=None:
        print("VermiCompost Serial port is open.")
        Vermicompost.serV.close()
        print("Vermicompost Serial port Closed.")
    else: 
        print("VermiCompost Serial port is closed")
    print("\n")

    current_index = (current_index - 1) % len(programs)
    load_program(current_index)

# Initialize tkinter window
root = tk.Tk()
root.title("Program Navigation")

# Frame to hold the plot
plot_frame = tk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Navigation buttons
nav_frame = tk.Frame(root)
nav_frame.pack(side="bottom", pady=10)

btn_prev = tk.Button(nav_frame, text="Previous", command=previous_program)
btn_prev.pack(side="left", padx=10)

btn_next = tk.Button(nav_frame, text="Next", command=next_program)
btn_next.pack(side="right", padx=10)

# Load the initial program
load_program(current_index)

# Run the tkinter main loop
root.mainloop()
