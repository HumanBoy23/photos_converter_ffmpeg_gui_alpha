#
# Author: @HumanBoy23
# A simple image conversion app created using Python3 with Tkinter module
# Uses ffmpeg for windows to convert images
# official ffmpeg site: https://ffmpeg.org/ (used as backend to convert images)
#
import pdb  # debugger
from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import ImageTk, Image
from os import system, environ, path

root = Tk()
# App icon
root.iconbitmap("icon.ico")

# Application size (Window size)
root.geometry("468x430+440+100")
root.wait_visibility()
# App will not resize if root.resizable is set to 0, 0
root.resizable(False, False)
# Name or Title of app
root.title("Image Converter Windows Beta by HumanBoy23")

# declaring global variable fileloc (file location variable) as string
fileloc = ''


# Function for browsing or opening file(s) in your computer
def open_explorer():
    global fileloc
    global panel
    try:
        destroy_panel()
    except NameError as n:
        print("No image found on Preview Panel to remove")
        pass

    # Locates "image" type files with only the given or set image file types
    fileloc = filedialog.askopenfilename(filetypes=(("All Files", "*.*"), ("jpg", "*.jpg"), ("jpeg", "*.jpeg"), ("png", "*.png"),
                                                    ("webp", "*.webp"), ("bitmap", "*.bmp"),
                                                    ("icons", "*.ico")))
    print(fileloc)
    if fileloc != "":
        img = ImageTk.PhotoImage(Image.open(fileloc).resize((440, 322)))
        panel = Label(root, image=img, relief="groove")
        panel.photo = img
        panel.place(x=10, y=40)


# Global variable to get the location where the converted file is saved form convert() function
saved_to = ''


# Converted successfully message will be display to the user after conversion
def converted_message():
    global saved_to
    messagebox.showinfo("Success!", "Image converted successfully! \nLocation: " + saved_to)


# User will be notified or alerted if he doesn't select a file (or doesn't browse file or path)
def file_not_selected():
    messagebox.showwarning("Image not found!", "Please select a file to convert")


# Function or logic that triggers after user hits convert that removes preview image
def destroy_panel():
    panel.destroy()


# this function is called when user clicks Convert
def convert():
    global fileloc
    global saved_to
    # Pause for 3 seconds
    # root.after(3000)
    convertFile_widget.config(cursor="hand2")
    # Ask user where to save file
    prompt_user_for_save_location = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    saved_to = prompt_user_for_save_location
    if prompt_user_for_save_location == '':  # If user cancels where to save file
        print("User cancel path selection")
    else:
        value = prompt_user_for_save_location
        read_value = value
        save_location = read_value
        get_user_selected_format = fileFormat_Selector.get()
        if fileloc == '':
            file_not_selected()
        else:
            if get_user_selected_format == "jpg":
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i -y " + save_location + "%~ni.jpg")
                converted_message()
                destroy_panel()
            elif get_user_selected_format == "png":
                print(fileloc)
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i " + save_location + "%~ni.png")
                converted_message()
                destroy_panel()
            elif get_user_selected_format == "jpeg":
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i -y " + save_location + "%~ni.jpeg""")
                converted_message()
                destroy_panel()
            elif get_user_selected_format == "webp":
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i -y " + save_location + "%~ni.webp""")
                converted_message()
                destroy_panel()
            elif get_user_selected_format == "ico":
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i -y " + save_location + "%~ni.ico""")
                converted_message()
                destroy_panel()
            elif get_user_selected_format == "bmp":
                system(
                    "for %i in (" + fileloc + ") do ffmpeg -hide_banner -loglevel panic -i %i -y " + save_location + "%~ni.bmp""")
                converted_message()
                destroy_panel()
            else:
                print("Unknown Error Occurred!")


# Function or Logic for Quit
configof_exitstate = ''


def checkexitstate():
    global configof_exitstate
    system("IF NOT EXIST exitstate.txt echo | set /p=yes > exitstate.txt")
    fileexitstate = open("exitstate.txt", "r")
    configof_exitstate = fileexitstate.read()
    fileexitstate.close()
    if configof_exitstate == "yes ":
        quit_btn_func()
    elif configof_exitstate == "no ":
        root.destroy()
    else:
        print("Error on main> checkexitstate function")


# toplevel stackoverflow link:
# https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
checkbtn_val = ''
exitpromptwindow = ''


def quit_btn_func():
    global checkbtn_val
    global exitpromptwindow
    root.wm_attributes('-disabled', True)
    exitpromptwindow = Toplevel(root)
    exitpromptwindow.geometry("300x120")
    # To center child (toplevl) window with parent (root) window

    # Disabled Resizing of window
    exitpromptwindow.resizable(False, False)
    # Title
    exitpromptwindow.title('Confirm Exit')
    # Icon
    exitpromptwindow.iconbitmap('icon.ico')
    # Variable for exit lable
    message = "Are you sure you want to exit?"
    Label(exitpromptwindow, text=message, font=('calbri', 14, 'bold')).pack(anchor="n", expand=False)
    # Set variable for exit data as string
    checkbtn_val = StringVar()
    # Set default value if yes than exit without asking if no then prompt user for exit
    checkbtn_val.set('yes')
    Checkbutton(exitpromptwindow, text="Don't ask again?", variable=checkbtn_val, onvalue='no', offvalue='yes', command=upd_ckbtnstate).pack(anchor="w", ipadx=10, expand=False)
    # Yes/Exit button
    Button(exitpromptwindow, text='Exit', font=('calbri', 10, 'bold'), width=6,
           command=root.destroy).pack(side="left", padx=50, expand=False)
    # No/Cancel BUTTON
    Button(exitpromptwindow, text='Cancel', font=('calbri', 10, 'bold'), command=exitpromptwindow_cancelfunc).pack(side="left", expand=False)
    exitpromptwindow.protocol("WM_DELETE_WINDOW", exitpromptwindow_cancelfunc)
    # Toplevel window will always be on top of parent (named as root)
    exitpromptwindow.wm_transient(root)
    x = root.winfo_x() + root.winfo_width() // 2 - exitpromptwindow.winfo_width() // 2
    y = root.winfo_y() + root.winfo_height() // 2 - exitpromptwindow.winfo_height() // 2
    exitpromptwindow.geometry(f"+{x}+{y}")


def exitpromptwindow_cancelfunc():
    global exitpromptwindow
    root.wm_attributes('-disabled', False)
    exitpromptwindow.withdraw()


def upd_ckbtnstate():
    global checkbtn_val
    system("echo Do not Ask on Exit is set to: && type exitstate.txt && echo.")
    if checkbtn_val.get() == 'no':
        system("echo |set /p=no>exitstate.txt")
    elif checkbtn_val.get() == 'yes':
        system("echo |set /p=yes>exitstate.txt")
    else:
        return


settingsexityesnoVal = ''
settings_photosconverter = ''
# function for Settings (Under Development)
settingsexityesnoValstate = ''


def settings_func():
    global settings_photosconverter
    global settingsexityesnoValstate
    global settingsexityesnoVal
    settingsyesnoVal = StringVar()
    settingsyesnoVal.set('active')
    root.wm_attributes('-disabled', True)
    settings_photosconverter = Toplevel()
    settings_photosconverter.geometry("300x240")
    settings_photosconverter.title('Settings')
    settings_photosconverter.iconbitmap('icon.ico')
    settings_photosconverter.resizable(False, False)
    system("IF NOT EXIST exitstate.txt echo | set /p=yes > exitstate.txt")
    fileexitstate = open("exitstate.txt", "r")
    dat = fileexitstate.read()
    fileexitstate.close()
    settingsexityesnoValstate = StringVar()
    settingsexityesnoValstate.set('active')
    if dat == 'no ':
        settingsexityesnoValstate = 'active'
    elif dat == 'yes ':
        settingsexityesnoValstate = 'disabled'
    else:
        print("dat is: ", dat)
        print("Error")

    Label(settings_photosconverter, text='Ask on exit', underline=0, relief='flat', bg='grey',
          fg='white').pack(side='left', anchor='n', expand=False, fill='none')
    Label(settings_photosconverter, text='_' * 40, bg='grey', fg='white').pack(side='left', anchor='n',
                                                                               fill='none', expand=False)
    Checkbutton(settings_photosconverter, variable=settingsexityesnoVal, text='disabled by default', onvalue='active',
                offvalue='disabled', state=settingsexityesnoValstate, command=ckBtnUpd).place(x=10, y=25)
    Label(settings_photosconverter, text='Define Custom Format(s) (Advanced Users):', underline=0, bg='grey',
          fg='white').place(y=60)
    Label(settings_photosconverter, text='Coming Soon!', fg='white', bg='grey').place(x=8, y=80)

    # Opens issues.txt file wherein known bug(s) are listed
    def open_known_issues_file():
        system("start issues.txt")

    issues_label = Label(settings_photosconverter, bg='grey', fg='white', text='Known issues: ')
    issues_label.place(y=105)
    issues_button = Button(settings_photosconverter, text='Read', command=open_known_issues_file)
    issues_button.place(x=10, y=125)
    settings_photosconverter.config(bg="grey")
    settings_photosconverter.wm_transient(root)
    settings_photosconverter.protocol("WM_DELETE_WINDOW", settings_cancel)
    x = root.winfo_x() + root.winfo_width() // 2 - settings_photosconverter.winfo_width() // 2
    y = root.winfo_y() + root.winfo_height() // 2 - settings_photosconverter.winfo_height() // 2
    settings_photosconverter.geometry(f"+{x}+{y}")


# Function to change save location of converted files
def _change_file_save_location():
    global settings_photosconverter
    system("if not exist save_loc.txt @echo off > save_loc.txt")
    user_defined_directory = filedialog.askdirectory()
    if user_defined_directory == '':
        # prints message in console if user cancels directory selection
        print("Directory not selected")
    else:
        open_save_file = open('save_loc.txt', 'w')
        open_save_file.write(user_defined_directory)
        print("New save location set to: ", user_defined_directory)
        open_save_file.close()
        print("close setting menu")
        settings_cancel()
        settings_photosconverter.after(1000)
        print("Restarting settings menu")
        settings_func()


def ckBtnUpd():
    global settingsexityesnoVal
    settingsexityesnoVal = StringVar()
    settingsexityesnoVal.set('active')
    system("IF NOT EXIST exitstate.txt echo | set /p=yes > exitstate.txt")
    if settingsexityesnoVal.get() == 'disabled':
        system("echo | set /p=no>exitstate.txt")
    elif settingsexityesnoVal.get() == 'active':
        system("echo | set /p=yes>exitstate.txt")
    else:
        print("Error saving value to exitstate.txt")


def _under_development_message():
    messagebox.showinfo('Under Development!', 'This feature is not yet available')


def settings_cancel():
    global settings_photosconverter
    root.wm_attributes('-disabled', False)
    settings_photosconverter.destroy()


# ******************* WIDGETS - GUI ********************* #

# PREDEFINED BUTTON NAMES
openFile = "File"
convertFile = "Convert"

# *** FOR FUTURE REFERENCE *** #
# Button relief (style) keywords: ridge, flat, groove, sunken, raised

# openFile button widget
openFile_widget = Button(root, text=openFile, command=open_explorer, relief="flat", cursor="hand2",
                         width=5, underline=0, activebackground="light grey", bg="grey", foreground="white")
openFile_widget.place(x=-6, y=-1)

# Label (BOX)
label_butBox = Label(root, text="PREVIEW", font=("Ariel", 10, "bold"), relief="ridge", width=55, height=20)
label_butBox.config(bg="dark grey")
label_butBox.place(x=10, y=40)

# label/widget for text that says: "Output format"
selectFormat_lbl = Label(root, text="Format: ", font=("ariel", 10, "bold"), bg="grey")
selectFormat_lbl.pack(side="bottom", pady=28)

# Dropdown menu options for file format
OPTIONS = [
    "png",
    "jpg",
    "jpeg",
    "png",
    "webp",
    "ico",
    "bmp"
]

# datatype of File format selection text
fileFormat_Selector = StringVar()

# Default Format
fileFormat_Selector.set("png")

# Dropdown (a.k.a option menu) widget
dropdownWidgetFor_fileFormat_Selector = ttk.OptionMenu(root, fileFormat_Selector, *OPTIONS)
# ****** FOR FUTURE REFERENCE ******* #
# Cursors styles - "arrow", "circle", "pirate", "plus", "shuttle", "spider" and others
dropdownWidgetFor_fileFormat_Selector.config(cursor="hand2")
dropdownWidgetFor_fileFormat_Selector.place(x=280, y=380, height=25)

# Convert button widget
convertFile_widget = Button(root, text="Convert", font=("ariel", 9, "bold"), command=convert, relief="groove",
                            activebackground="light grey", cursor="hand2")
convertFile_widget.place(x=360, y=380)
# Settings button widget using a settings icon
setting_img = PhotoImage(file=r"settings_icon.png", height=23, width=23)
settings_BtnWidget = Button(root, bg="grey", activebackground="light blue", relief="flat", cursor="hand2",
                            command=settings_func, image=setting_img)
settings_BtnWidget.place(x=380, y=3)
# App background (bg) color
root.config(bg="grey")
# Exit message
root.protocol("WM_DELETE_WINDOW", checkexitstate)
''' infinite loop which is required to run tkinter program infinitely until
    an interrupt occurs '''
root.update()
root.mainloop()
 