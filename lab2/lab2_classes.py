class Disciplina:
    def __init__(self, nazvanie, kafedra):
        self.nazvanie = nazvanie
        self.kafedra = kafedra
        self.specialnosti = set()
 
 
class Kafedra:
    def __init__(self, nazvanie):
        self.nazvanie = nazvanie
        self.discipliny = {}
 
    def chitaet_li(self, nazvanie, spec):
        return nazvanie in self.discipliny and spec in self.discipliny[nazvanie].specialnosti
 
 
class Student:
    def __init__(self, id_, fio, spec):
        self.id = id_
        self.fio = fio
        self.spec = spec
        self.semestr = 1
        self.status = "учится"
        self.profil = None
        self.kafedra = None
        self.ball_konkursa = None
        self.zapisan = {}
        self.ocenki = {}
 
    @property
    def kurs(self):
        return (self.semestr + 1) // 2
 
    def srednii_ball(self):
        vse = [b for sem in self.ocenki.values() for b in sem.values()]
        return round(sum(vse) / len(vse), 2) if vse else 0
 
 
FAIL_VEDOMOSTI = "vedomosti.txt"
RAZDELITEL = "\n=====\n"
MIN_BALL = 4
MAX_BALL = 10
 
MAT = "Кафедра высшей математики и математической физики"
FIZ = "Кафедра физики и аэрокосмических технологий"
KIS = "Кафедра информатики и компьютерных систем"
INTSIS = "Кафедра интеллектуальных систем"
SACM = "Кафедра системного анализа и компьютерного моделирования"
KBIT = "Кафедра кибербезопасности и информационных технологий"
FEN = "Кафедра физической электроники и нанотехнологий"
KRO = "Кафедра квантовой радиофизики и оптоэлектроники"
RDMT = "Кафедра радиофизики и цифровых медиа технологий"
 
 
def norm(tekst):
    return " ".join(tekst.lower().replace("ё", "е").replace('"', "").replace("«", "").replace("»", "").split())
 
 
SPECIALNOSTI = {
    "РФ": ("Радиофизика и информационные технологии", ["радиофизика", "рфиит"]),
    "ПИ": ("Прикладная информатика", []),
    "КБ": ("Кибербезопасность", ["кибер безопасность"]),
    "ИнтЭЛ": ("Интеллектуальная электроника", ["иэ"]),
}
 
PROFILI = {
    "Аэрокосмические технологии": ("РФ", FIZ, 24, ["аэро"]),
    "Информатика, программируемые электроника и измерительные системы": ("РФ", KIS, 23, ["информатика", "ипэис"]),
    "Компьютерное проектирование и технологии микроэлектронных систем": ("РФ", FEN, 24, ["кптмс"]),
    "Фотоника и прикладные компьютерные технологии": ("РФ", KRO, 24, ["фпкт", "фотоника"]),
    "Радиофизика и цифровые технологии": ("РФ", RDMT, 23, ["рцт"]),
    "Интеллектуальные и киберфизические системы": ("ПИ", INTSIS, 27, ["икс"]),
    "Анализ больших данных и биоинформатика": ("ПИ", SACM, 27, ["абдиб", "биоинформатика"]),
    "Безопасность компьютерных технологий и систем": ("КБ", KBIT, 26, ["бктс"]),
    "Киберустойчивость и безопасность киберфизических систем": ("КБ", KBIT, 30, ["куб", "кубкфс"]),
    "Цифровые интеллектуальные системы": ("ИнтЭЛ", KIS, 30, ["цис"]),
}
 