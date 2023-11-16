from logs import *
class Saglaba(Logs):
    def __init__(self,cur,saglabat,tab_nosauk):
        self.cur = cur
        self.saglabat = saglabat
        self.tab_nosauk = tab_nosauk
        super().__init__(self.cur)
    def druka_tab(self,cur,tab_nosauk):
        print("\nTabula", self.tab_nosauk)
        self.cur.execute(f""" SELECT * FROM '{self.tab_nosauk}' """)
        self.saturs = self.cur.fetchall()
        for rinda in self.saturs:
            print(rinda)
    def saglaba_jauno(self,cur,saglabat,tab_nosauk):
        self.cur.execute(f""" INSERT INTO Kategorija (kategorija) SELECT 'self.saglabat' WHERE NOT EXISTS(SELECT 1 FROM Kategorija WHERE kategorija = 'self.saglabat') """)