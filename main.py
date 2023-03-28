from data import *

a = Gui()
a.screen_settings()
a.img_settings()
a.info_label()
a.info_entry()
a.info_buttons()

def generate_password():
    a.e_pas.insert(0, a.generate())

def add_info():
    a.add_inf()

def search_folder():
    a.search_file()
    
a.gen_pas.config(command = generate_password)
a.add.config(command = add_info)
a.search.config(command = search_folder)

a.hold_screen()