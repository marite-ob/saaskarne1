import PySimpleGUI as sg
class Logs():

  def __init__(self,cur):
    self.cur = cur
    self.cur.execute("""SELECT kategorija FROM Kategorija""")
    self.kateg = self.cur.fetchall()
    self.cur.execute("""SELECT nosaukums FROM Nosaukums""")
    self.nosauk = self.cur.fetchall()
    self.cur.execute("""SELECT tehn_rakst FROM Teh_raksturojums""")
    self.tehn_rakst = self.cur.fetchall()
    self.cur.execute("""SELECT nomas_cena_diena FROM Produkts""")
    self.produkt = self.cur.fetchall()
  def izkarto(self):
    self.layout = [ [sg.Text("Izvēlieties nopirkto produktu vai ievādiet jaunu nopirkto produktu")],
                [sg.Text("Kategorija"), sg.Listbox(values=self.kateg, key="-KATEG-", enable_events=True), sg.InputText(key="T-KATEG-")],
                [sg.Text("Nosaukums",size=(15, 1)), sg.Listbox(values=self.nosauk, size=(20,1), key="-NOSAUK-", enable_events=True), sg.InputText(key="T-NOSAUK-")],
                [sg.Text("Tehniskais raksturojums"), sg.Listbox(values=self.tehn_rakst, size=(30,1), key="-RAKSTUR-", enable_events=True), sg.InputText(key="T-RAKSTUR-")],
                [sg.Text("Nomas cena dienā", size=(7,1)), sg.Listbox(values=self.produkt, size=(30,1), key="-CENA-", enable_events=True), sg.InputText(key="T-CENA-")],
                [sg.Button("Ievadīt"), sg.Button("Atcelt")] ]
  def logu_veido(self):
    Logs.izkarto(self)
    window = sg.Window("Produkti", self.layout)
    return(window)