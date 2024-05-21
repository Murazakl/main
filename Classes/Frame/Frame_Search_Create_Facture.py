import tkinter as tk
import gettext
import os
from Classes.DashBoard.CDashBoardSearchCreateFacture import DashBoardSearchCreateFacture
from Classes.Boutons.CButtonsSearchCreateFacture import ButtonsSearchCreateFacture

class Frame_Search_Create_Facture(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour la recherche et la création de clients pour l'application en appelant la classe DashBoardSearchCreateClients et la classe ButtonsSearchCreateClients
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Search_Create_Clients
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = DashBoardSearchCreateFacture(self)
        self.buttons = ButtonsSearchCreateFacture(self, self.dash_board, self, self.language_var)
        self.geometry('800x600')
        self.translate()

    def translate(self):
        '''
        Méthode qui permet de traduire les textes de la fenêtre
        '''
        lang = self.master.language_var.get()
        gettext.bindtextdomain(lang, './Langage')
        gettext.textdomain(lang)
        translation = gettext.translation(lang, localedir = os.path.join(os.path.dirname(__file__), '..', 'Langage'), languages=[lang])
        translation.install()
        _ = translation.gettext
        self.dash_board.label.config(text=_('Search clients'))
        self.dash_board.label1.config(text=_('Last Name'))
        self.dash_board.label2.config(text=_('First Name'))
        self.buttons.button1.config(text=_('Search'))
        self.buttons.button_confirm.config(text=_('Confirm'))
        self.buttons.button2.config(text=_('Back'))