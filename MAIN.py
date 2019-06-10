from tkinter import *


class RocketClicker:

    def __init__(self, master):

        self.frame = Frame(master, bg='#153450')
        self.frame.pack(side=TOP, pady='5', padx='5')

        self.lower_main_frame = Frame(master, bg='#153450')
        self.lower_main_frame.pack(pady='10', padx='10')

        self.shop_frame = Frame(master, bg='#153450')

        print("Created by Jorge Soderberg\nJuly 2016")
        print("My first working game made completely on my own with a GUI!")
        print("Still contains various bugs such as boost score not updating automatically on main menu after buying "
              "auto-clickers, buttons beciming active after purchasing, going to main menu, and coming back, etc."
              "Could have been avoided by creating only one single page containing the button AND shop. ")

        # main menu

        main_title = Label(self.frame, font=('Segoe UI Bold Italic', '40'), text="Rocket Clicker",
                           bg='#153450', fg='#FFFFFF', width='15', pady='10')
        main_title.grid(row=0)

        main_button = Button(self.frame, text="Click!", font=('Segoe UI Bold Italic', '20'), bg='#6699CC',
                             fg='#FFFFFF', bd='5', activebackground='#6699CC', activeforeground='#FFFFFF',
                             width='12', command=self.boost)
        main_button.grid(row=1)

        shop_button = Button(self.lower_main_frame, text="Shop", font=('Segoe UI Bold', '12'), bg='#6699CC',
                             fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                             width='6', command=self.shop)
        shop_button.grid(row=2, column=1, ipadx='2', sticky=W)

        self.boost_label = Label(self.lower_main_frame, font=('Segoe UI Bold', '16'),
                                 text="Boost: 0", bg='#153450', fg='#FFFFFF')
        self.boost_label.grid(row=2, column=0, ipadx='20', ipady='10', sticky=E)

        self.octane_image = PhotoImage(file='octaneCLICKER_blueBG.gif')
        self.octane = Label(self.lower_main_frame, image=self.octane_image, borderwidth=0)
        self.octane.grid(row=3, columnspan=2)

        self.click = 0
        self.multiplier = 1

# Hides shop frame and shows main menu frames.
    def main_menu(self):
        self.frame.pack(side=TOP, pady='5', padx='5')
        self.lower_main_frame.pack(pady='10', padx='10')
        self.shop_frame.pack_forget()
        self.boost_label.destroy()

        boost_click = ("Boost:", self.click)
        # shows boost amount
        boost_label = Label(self.lower_main_frame, font=('Segoe UI Bold', '16'),
                            text=boost_click, bg='#153450', fg='#FFFFFF')
        boost_label.grid(row=2, column=0, ipadx='20', ipady='10', sticky=E)

    # counts main button clicks (boost)
    def boost(self):
        self.click += self.multiplier

        boost_click = ("Boost:", self.click)
        # shows boost amount
        boost_label = Label(self.lower_main_frame, font=('Segoe UI Bold', '16'),
                            text=boost_click, bg='#153450', fg='#FFFFFF')
        boost_label.grid(row=2, column=0, ipadx='20', ipady='10', sticky=E)


# Contains EVERYTHING within the shop interface
    def shop(self):
        # forgets both frames on main screen and packs shop frame
        self.lower_main_frame.pack_forget()
        self.frame.pack_forget()
        self.shop_frame.pack(padx='10', pady='10')

    # will allows button press to have no effect when already purchased.(need to impliment updates to keep disabled.)
        def none():
            pass

    # Creates window that contains more info on a purchase
        def purchase_1_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_1_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="2x Multiplier (100 Boost)")
            purchase_1_info_title.grid(ipadx='10', ipady='10')

            purchase_1_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="Each click will now be worth\n"
                                          " 2 boost instead of 1!")
            purchase_1_info_label.grid(ipadx='10', ipady='15')

            def purchase_1_info_back():
                top.destroy()
                self.shop()

            purchase_1_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_1_info_back)
            purchase_1_info_quit.grid()

    # Creates window that contains more info on a purchase
        def purchase_2_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_2_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="3x Multiplier (200 Boost)")
            purchase_2_info_title.grid(ipadx='10', ipady='10')

            purchase_2_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="Each click will now be worth\n"
                                          " 3 boost instead of 1!")
            purchase_2_info_label.grid(ipadx='10', ipady='15')

            def purchase_2_info_back():
                top.destroy()
                self.shop()

            purchase_2_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_2_info_back)
            purchase_2_info_quit.grid()

    # Creates window that contains more info on a purchase
        def purchase_3_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_3_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="Rookie Auto-Clicker (250 Boost)")
            purchase_3_info_title.grid(ipadx='10', ipady='10')

            purchase_3_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="You will automatically receive\n"
                                               "0.2 boost per second without\n"
                                               "even having to click!")
            purchase_3_info_label.grid(ipadx='10', ipady='15')

            def purchase_3_info_back():
                purchase_3_info_title.destroy()
                purchase_3_info_label.destroy()
                purchase_3_info_quit.destroy()
                top.destroy()

            purchase_3_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_3_info_back)
            purchase_3_info_quit.grid()

    # Creates window that contains more info on a purchase
        def purchase_4_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_4_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="Veteran Auto-Clicker (300 Boost)")
            purchase_4_info_title.grid(ipadx='10', ipady='10')

            purchase_4_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="You will automatically receive\n"
                                               "1 boost per second without\n"
                                               "even having to click! If you have\n"
                                               "already purchased the Rookie\n"
                                               "Auto-Clicker, it will continue\n"
                                               "to work!")
            purchase_4_info_label.grid(ipadx='10', ipady='15')

            def purchase_4_info_back():
                purchase_4_info_title.destroy()
                purchase_4_info_label.destroy()
                purchase_4_info_quit.destroy()
                top.destroy()

            purchase_4_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_4_info_back)
            purchase_4_info_quit.grid()

    # Creates window that contains more info on a purchase
        def purchase_5_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_5_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="Master Auto-Clicker (500 Boost)")
            purchase_5_info_title.grid(ipadx='10', ipady='10')

            purchase_5_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="You will automatically receive\n"
                                               "5 boost per second without\n"
                                               "even having to click! If you have\n"
                                               "already purchased the Rookie and Veteran\n"
                                               "Auto-Clickers, they will continue\n"
                                               "to work!")
            purchase_5_info_label.grid(ipadx='10', ipady='15')

            def purchase_5_info_back():
                purchase_5_info_title.destroy()
                purchase_5_info_label.destroy()
                purchase_5_info_quit.destroy()
                top.destroy()

            purchase_5_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_5_info_back)
            purchase_5_info_quit.grid()

    # Creates window that contains more info on a purchase
        def purchase_6_information():
            top = Toplevel()
            top.configure(bg='#153450')

            purchase_6_info_title = Label(top, font=('Segoe UI Bold', '16'), bg='#153450', fg='#FFFFFF',
                                          text="Legend Auto-Clicker (500 Boost)")
            purchase_6_info_title.grid(ipadx='10', ipady='10')

            purchase_6_info_label = Label(top, font=('Segoe UI Light', '13'), bg='#153450', fg='#FFFFFF',
                                          text="You will automatically receive\n"
                                               "10 boost per second without\n"
                                               "even having to click! If you have\n"
                                               "already purchased any of the other\n"
                                               "Auto-Clickers, they will continue\n"
                                               "to work!")
            purchase_6_info_label.grid(ipadx='10', ipady='15')

            def purchase_6_info_back():
                purchase_6_info_title.destroy()
                purchase_6_info_label.destroy()
                purchase_6_info_quit.destroy()
                top.destroy()

            purchase_6_info_quit = Button(top, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                          fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                          text="Back", width='4', command=purchase_6_info_back)
            purchase_6_info_quit.grid()

    # implements x2 multiplier when purchased
        def purchase_1_execute():
            update_display()
            purchase_1_update()
            if self.click >= 100:
                self.click -= 100
                self.multiplier = 2

    # implements x2 multiplier when purchased
        def purchase_2_execute():
            update_display()
            purchase_2_update()
            if self.click >= 200:
                self.click -= 200
                self.multiplier = 3

    # implements rookie auto clicker
        def purchase_3_execute():
            update_display()
            purchase_3_update()

            if self.click >= 250:
                self.click -= 250
                purchase_3_execute_clicker()

        def purchase_3_execute_clicker():
            self.click += 1
            self.shop_frame.after(5000, purchase_3_execute_clicker)

    # implements veteran auto clicker
        def purchase_4_execute():
            update_display()
            purchase_4_update()

            if self.click >= 300:
                self.click -= 300
                purchase_4_execute_clicker()

        def purchase_4_execute_clicker():
            self.click += 1
            self.shop_frame.after(1000, purchase_4_execute_clicker)

    # implements master auto clicker
        def purchase_5_execute():
            update_display()
            purchase_5_update()

            if self.click >= 500:
                self.click -= 500
                purchase_5_execute_clicker()

        def purchase_5_execute_clicker():
            self.click += 5
            self.shop_frame.after(1000, purchase_5_execute_clicker)

    # implements legend auto clicker
        def purchase_6_execute():
            update_display()
            purchase_6_update()

            if self.click >= 1000:
                self.click -= 1000
                purchase_6_execute_clicker()

        def purchase_6_execute_clicker():
            self.click += 10
            self.shop_frame.after(1000, purchase_6_execute_clicker)

    # changes color of text in shop and disables buttons once something is purchsed.
    # BUG: Un-done when leave shop and go back
        def purchase_1_update():
            purchase_1.configure(fg='#696969')
            purchase_1_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_1_update)

        def purchase_2_update():
            purchase_1.configure(fg='#696969')
            purchase_1_button.configure(command=none, state=DISABLED)
            purchase_2.configure(fg='#696969')
            purchase_2_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_2_update)

        def purchase_3_update():
            purchase_3.configure(fg='#696969')
            purchase_3_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_3_update)

        def purchase_4_update():
            purchase_4.configure(fg='#696969')
            purchase_4_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_4_update)

        def purchase_5_update():
            purchase_5.configure(fg='#696969')
            purchase_5_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_5_update)

        def purchase_6_update():
            purchase_6.configure(fg='#696969')
            purchase_6_button.configure(command=none, state=DISABLED)
            root.after(500, purchase_6_update)

        main_title = Label(self.shop_frame, font=('Segoe UI Bold Italic', '36'), text="Shop",
                           bg='#153450', fg='#FFFFFF', width='15')
        main_title.grid(row=0, columnspan=2)

    # shows boost amount in shop frame (& updates it every second)
        def update_display():
            self.boost_label.destroy()
            boost_click = ("Boost:", self.click)
            self.boost_label = Label(self.shop_frame, font=('Segoe UI Bold', '16'), text=boost_click,
                                     bg='#153450', fg='#FFFFFF')
            self.boost_label.grid(row=1, columnspan=2, ipadx='8', ipady='10')
            self.shop_frame.after(300, update_display)
        update_display()

    # displays text and buttons to buy x2 multiplier
        purchase_1 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="2x Multiplier (100 Boost)  ")
        purchase_1.grid(row=2, column=0, sticky=E)

        purchase_1_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_1_execute, width='4')
        purchase_1_button.grid(row=2, column=1, sticky=E)

        purchase_1_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_1_information)
        purchase_1_info.grid(row=2, column=1, sticky=W)

        if self.click >= 100:
            purchase_1_button.configure(state=NORMAL)

    # displays text and button to buy x3 multiplier
        purchase_2 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="3x Multiplier (200 Boost)  ")
        purchase_2.grid(row=3, column=0, sticky=E)

        purchase_2_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_2_execute, width='4')
        purchase_2_button.grid(row=3, column=1, sticky=E)

        purchase_2_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_2_information)
        purchase_2_info.grid(row=3, column=1, sticky=W)

        if self.click >= 200:
            purchase_2_button.configure(state=NORMAL)

    # displays rookie auto-click purchase
        purchase_3 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="Rookie Auto-Clicker (250 Boost)  ")
        purchase_3.grid(row=4, column=0, sticky=E)

        purchase_3_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_3_execute, width='4')
        purchase_3_button.grid(row=4, column=1, sticky=E)

        purchase_3_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_3_information)
        purchase_3_info.grid(row=4, column=1, sticky=W)

        if self.click >= 250:
            purchase_3_button.configure(state=NORMAL)

    # displays veteran auto-click purchase
        purchase_4 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="Veteran Auto-Clicker (300 Boost)  ")
        purchase_4.grid(row=5, column=0, sticky=E)

        purchase_4_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_4_execute, width='4')
        purchase_4_button.grid(row=5, column=1, sticky=E)

        purchase_4_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_4_information)
        purchase_4_info.grid(row=5, column=1, sticky=W)

        if self.click >= 300:
            purchase_4_button.configure(state=NORMAL)

    # displays master auto-click purchase
        purchase_5 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="Master Auto-Clicker (500 Boost)  ")
        purchase_5.grid(row=6, column=0, sticky=E)

        purchase_5_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_5_execute, width='4')
        purchase_5_button.grid(row=6, column=1, sticky=E)

        purchase_5_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_5_information)
        purchase_5_info.grid(row=6, column=1, sticky=W)

        if self.click >= 500:
            purchase_5_button.configure(state=NORMAL)

    # displays legend auto-click purchase
        purchase_6 = Label(self.shop_frame, font=('Segoe UI Light', '16'), bg='#153450', fg='#FFFFFF',
                           text="Legend Auto-Clicker (1000 Boost)  ")
        purchase_6.grid(row=7, column=0, sticky=E)

        purchase_6_button = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                   fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                   text="BUY", state=DISABLED, command=purchase_6_execute, width='4')
        purchase_6_button.grid(row=7, column=1, sticky=E)

        purchase_6_info = Button(self.shop_frame, font=('Segoe UI Bold', '10'), bg='#6699CC',
                                 fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                                 text="INFO", width='4', command=purchase_6_information)
        purchase_6_info.grid(row=7, column=1, sticky=W)

        if self.click >= 1000:
            purchase_6_button.configure(state=NORMAL)

    # Button leading back to main menu
        back_button = Button(self.shop_frame, text="Back", font=('Segoe UI Bold', '12'), bg='#6699CC',
                             fg='#FFFFFF', activebackground='#6699CC', activeforeground='#FFFFFF',
                             width='6', command=self.main_menu)
        back_button.grid(row=10, columnspan=2)

root = Tk()
root.title("Rocket Clicker")
root.geometry('500x530')
root.configure(background='#153450')

a = RocketClicker(root)

root.mainloop()
