class Disciplina:
    def __init__(self, nazvanie, kafedra, kurs=1, semestr=1):
        self.nazvanie = nazvanie
        self.kafedra = kafedra
        self.kurs = kurs
        self.semestr = semestr
        self.specialnosti = set()


class Kafedra:
    def __init__(self, nazvanie, opisanie=""):
        self.nazvanie = nazvanie
        self.opisanie = opisanie
        self.discipliny = {}

    def chitaet_li(self, nazvanie, spec):
        return nazvanie in self.discipliny and spec in self.discipliny[nazvanie].specialnosti


class Student:
    def __init__(self, id_, fio, spec, semestr=1):
        self.id = str(id_)
        self.fio = fio
        self.spec = spec
        self.semestr = semestr
        self.status = "учится"
        self.profil = None
        self.kafedra = None
        self.ball_konkursa = None
        self.zapisan = {}
        self.ocenki = {}
        self.fayli_vedomostey = []

    @property
    def kurs(self):
        return (self.semestr + 1) // 2

    @property
    def semestr_v_kurse(self):
        return 1 if self.semestr % 2 == 1 else 2

    def srednii_ball(self):
        vse = [b for sem in self.ocenki.values() for b in sem.values() if b is not None]
        return round(sum(vse) / len(vse), 2) if vse else 0


FAIL_VEDOMOSTI = "vedomosti.txt"
FAIL_VEDOMOSTI_DISC = "vedomosti_discipliny.txt"
RAZDELITEL = "\n=====\n"
MIN_BALL = 4
MAX_BALL = 10

KAF_MAT = "Кафедра высшей математики и математической физики"
KAF_FIZ = "Кафедра физики и аэрокосмических технологий"
KAF_KIS = "Кафедра информатики и компьютерных систем"
KAF_INTSIS = "Кафедра интеллектуальных систем"
KAF_SACM = "Кафедра системного анализа и компьютерного моделирования"
KAF_TIT = "Кафедра телекоммуникаций и информационных технологий"
KAF_KRO = "Кафедра квантовой радиофизики и оптоэлектроники"
KAF_RDMT = "Кафедра радиофизики и цифровых медиатехнологий"
KAF_DRUG = "Другой факультет"


def norm(tekst):
    return " ".join(tekst.lower().replace("ё", "е").replace('"', "").replace("«", "").replace("»", "").split())


SPECIALNOSTI = {
    "РФ": ("Радиофизика и информационные технологии", ["радиофизика", "рфиит", "рф"]),
    "ПИ": ("Прикладная информатика", ["прикладная информатика", "пи"]),
    "КБ": ("Кибербезопасность", ["кибер безопасность", "кибербезопасность", "кб"]),
    "ИнтЭЛ": ("Интеллектуальная электроника", ["иэ", "интэл", "интеллектуальная электроника"]),
}

PROFILI = {
    "Аэрокосмические технологии": ("РФ", KAF_FIZ, 24, ["аэро"]),
    "Информатика, программируемые электроника и измерительные системы": ("РФ", KAF_KIS, 23, ["информатика", "ипэис"]),
    "Компьютерное проектирование и технологии микроэлектронных систем": ("РФ", KAF_TIT, 24, ["кптмс"]),
    "Фотоника и прикладные компьютерные технологии": ("РФ", KAF_KRO, 24, ["фпкт", "фотоника"]),
    "Радиофизика и цифровые технологии": ("РФ", KAF_RDMT, 23, ["рцт"]),
    "Интеллектуальные и киберфизические системы": ("ПИ", KAF_INTSIS, 27, ["икс"]),
    "Анализ больших данных и биоинформатика": ("ПИ", KAF_SACM, 27, ["абдиб", "биоинформатика"]),
    "Безопасность компьютерных технологий и систем": ("КБ", KAF_TIT, 26, ["бктс"]),
    "Киберустойчивость и безопасность киберфизических систем": ("КБ", KAF_TIT, 30, ["куб", "кубкфс"]),
    "Цифровые интеллектуальные системы": ("ИнтЭЛ", KAF_KIS, 30, ["цис"]),
}

KAFEDRY_INFO = {
    KAF_MAT: "Кафедра факультета РФиКТ БГУ (высшая математика, линейная алгебра, дифференциальные уравнения и математическая физика)",
    KAF_FIZ: "Кафедра факультета РФиКТ БГУ (общая физика, электродинамика, оптика, аэрокосмические и информационные технологии)",
    KAF_KIS: "Кафедра факультета РФиКТ БГУ (программирование на C++, численные методы, архитектура компьютеров и компьютерные системы)",
    KAF_INTSIS: "Кафедра факультета РФиКТ БГУ (интеллектуальные системы, машинное обучение, интегральная электроника и алгоритмы)",
    KAF_SACM: "Кафедра факультета РФиКТ БГУ (теория вероятностей и математическая статистика, базы данных, системный анализ и моделирование)",
    KAF_TIT: "Кафедра факультета РФиКТ БГУ (телекоммуникации и информационные технологии, компьютерные сети, ОС и безопасность систем)",
    KAF_KRO: "Кафедра факультета РФиКТ БГУ (квантовая радиофизика и оптоэлектроника)",
    KAF_RDMT: "Кафедра факультета РФиКТ БГУ (радиофизика и цифровые медиатехнологии, прикладная электродинамика и теория информации)",
    KAF_DRUG: "Общеуниверситетская / иная кафедра за пределами РФиКТ БГУ",
}

DISCIPLINY_PO_KURSAM = {
    1: {
        1: {
            "РФ": [("Математический анализ", KAF_MAT), ("Механика", KAF_FIZ)],
            "ПИ": [("Математический анализ", KAF_MAT), ("Механика", KAF_FIZ)],
            "КБ": [("Математический анализ", KAF_MAT), ("Механика", KAF_FIZ)],
            "ИнтЭЛ": [("Математический анализ", KAF_MAT), ("Механика", KAF_FIZ)],
        },
        2: {
            "РФ": [("Электричество и магнетизм", KAF_FIZ), ("Программирование на C++", KAF_KIS)],
            "ПИ": [("Аналитическая геометрия и линейная алгебра", KAF_MAT), ("Программирование на C++", KAF_KIS)],
            "КБ": [("Алгоритмы и структуры данных", KAF_INTSIS), ("Программирование на C++", KAF_KIS)],
            "ИнтЭЛ": [("Электричество и магнетизм", KAF_FIZ), ("Программирование на C++", KAF_KIS)],
        },
    },
    2: {
        1: {
            "РФ": [("Оптика", KAF_FIZ), ("Теория вероятностей и математическая статистика", KAF_SACM)],
            "ПИ": [("Численные методы", KAF_KIS), ("Теория вероятностей и математическая статистика", KAF_SACM)],
            "КБ": [("Дифференциальные уравнения", KAF_MAT), ("Базы данных", KAF_SACM)],
            "ИнтЭЛ": [("Дифференциальные уравнения", KAF_MAT), ("Оптика", KAF_FIZ)],
        },
        2: {
            "РФ": [("Интегральная электроника", KAF_INTSIS), ("Базы данных", KAF_SACM)],
            "ПИ": [("Архитектура компьютеров", KAF_KIS), ("Искусственный интеллект и методы машинного обучения", KAF_INTSIS)],
            "КБ": [("Квантовая физика", KAF_FIZ), ("Программирование на Java", KAF_SACM)],
            "ИнтЭЛ": [("Архитектура компьютеров", KAF_KIS), ("Интегральная электроника", KAF_INTSIS)],
        },
    },
    3: {
        1: {
            "РФ": [("Термодинамика и статистическая физика", KAF_FIZ)],
            "ПИ": [("Операционные системы", KAF_TIT)],
            "КБ": [("Основы кибербезопасности", KAF_TIT)],
            "ИнтЭЛ": [("Операционные системы", KAF_TIT)],
        },
        2: {
            "РФ": [("Статистическая радиофизика и теория информации", KAF_RDMT)],
            "ПИ": [("Интеллектуальный анализ данных", KAF_SACM)],
            "КБ": [("Прикладная электродинамика", KAF_RDMT)],
            "ИнтЭЛ": [("Цифровая обработка сигналов", KAF_FIZ)],
        },
    },
    4: {
        1: {
            "РФ": [("Квантовая радиофизика и оптоэлектроника", KAF_KRO)],
            "ПИ": [("Анализ больших данных", KAF_SACM)],
            "КБ": [("Криптографический инжиниринг", KAF_SACM)],
            "ИнтЭЛ": [("Анализ больших данных", KAF_SACM)],
        },
        2: {
            "РФ": [("Геоинформационные системы и технологии", KAF_FIZ)],
            "ПИ": [("Мультиагентные системы", KAF_INTSIS)],
            "КБ": [("Распределённые вычислительные системы и (облачные) технологии", KAF_TIT)],
            "ИнтЭЛ": [("Распределённые вычислительные системы и (облачные) технологии", KAF_TIT)],
        },
    },
}


class FakultetRFKT:
    def __init__(self, nazv="РФиКТ БГУ"):
        self.nazv = nazv
        self.studenty = []
        self.kafedry = {}
        self.discipliny = []
        for nazv_kaf, opis in KAFEDRY_INFO.items():
            self.kafedry[nazv_kaf] = Kafedra(nazv_kaf, opis)
        for kurs, semestry in DISCIPLINY_PO_KURSAM.items():
            for semestr, spec_dict in semestry.items():
                for spec_kod, sp_disc in spec_dict.items():
                    for nazv_disc, nazv_kaf in sp_disc:
                        if nazv_kaf not in self.kafedry:
                            self.kafedry[nazv_kaf] = Kafedra(nazv_kaf)
                        d = self._disc(nazv_disc, nazv_kaf, kurs, semestr)
                        self.kafedry[nazv_kaf].discipliny[d.nazvanie] = d
                        d.specialnosti.add(spec_kod)

    def _disc(self, nazv_disc, nazv_kaf, kurs=1, semestr=1):
        for d in self.discipliny:
            if norm(d.nazvanie) == norm(nazv_disc) and norm(d.kafedra) == norm(nazv_kaf) and d.kurs == kurs and d.semestr == semestr:
                return d
        d = Disciplina(nazv_disc, nazv_kaf, kurs, semestr)
        self.discipliny.append(d)
        return d

    def _spec(self, spec_vvod):
        n = norm(spec_vvod)
        for kod, (polnoe, sinonimy) in SPECIALNOSTI.items():
            if n == norm(kod) or n == norm(polnoe) or n in [norm(s) for s in sinonimy]:
                return kod
        return None

    def _stud(self, id_stud):
        return next((s for s in self.studenty if s.id == str(id_stud)), None)

    def _disc_stud(self, stud, nazv_disc):
        return next((d for d in stud.zapisan if norm(d.nazvanie) == norm(nazv_disc)), None)

    def _sem_discipliny(self, spec_kod, kurs, semestr):
        sp = DISCIPLINY_PO_KURSAM.get(kurs, {}).get(semestr, {}).get(spec_kod, [])
        return [self._disc(nd, nk, kurs, semestr) for nd, nk in sp]

    def _ubrat_iz_faila(self, filename, stud):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                bloki = f.read().split(RAZDELITEL)
        except FileNotFoundError:
            return
        ost = [b.strip() for b in bloki if b.strip() and f"ID: {stud.id}\n" not in b and f"Студент: {stud.fio}\n" not in b]
        with open(filename, "w", encoding="utf-8") as f:
            f.write((RAZDELITEL.join(ost) + RAZDELITEL) if ost else "")

    def zachislit(self, id_stud, fio, spec_vvod, kurs=1, semestr=1):
        spec_kod = self._spec(spec_vvod)
        if not spec_kod:
            raise ValueError(f"Специальность '{spec_vvod}' не найдена")
        if not (1 <= kurs <= 4 and 1 <= semestr <= 2):
            raise ValueError("Курс должен быть 1-4, семестр 1-2")
        if self._stud(id_stud):
            raise ValueError(f"Студент с ID {id_stud} уже существует")
        obshiy_sem = (kurs - 1) * 2 + semestr
        stud = Student(id_stud, fio, spec_kod, obshiy_sem)
        for k, semestry in DISCIPLINY_PO_KURSAM.items():
            for s, spec_dict in semestry.items():
                d_sem = (k - 1) * 2 + s
                if d_sem < obshiy_sem:
                    for nd, nk in spec_dict.get(spec_kod, []):
                        d = self._disc(nd, nk, k, s)
                        stud.ocenki.setdefault(d_sem, {})[d.nazvanie] = MIN_BALL
        for d in self._sem_discipliny(spec_kod, kurs, semestr):
            stud.zapisan[d] = None
            stud.ocenki.setdefault(obshiy_sem, {})[d.nazvanie] = None
        self.studenty.append(stud)
        return stud

    def otchislit(self, id_stud):
        stud = self._stud(id_stud)
        if not stud:
            raise LookupError("Студент не найден")
        for fname in set(stud.fayli_vedomostey) | {FAIL_VEDOMOSTI}:
            self._ubrat_iz_faila(fname, stud)
        stud.status = "отчислен"
        self.studenty.remove(stud)
        return stud

    def dobavit_na_disciplinu(self, id_stud, nazv_disc):
        stud = self._stud(id_stud)
        if not stud:
            raise LookupError("Студент не найден")
        n = norm(nazv_disc)
        podh = [d for d in self.discipliny if norm(d.nazvanie) == n and stud.spec in d.specialnosti]
        if not podh:
            raise ValueError("Дисциплина не найдена для специальности студента")
        disc = next((d for d in podh if d.kurs == stud.kurs and d.semestr == stud.semestr_v_kurse), None)
        if not disc:
            raise ValueError(f"Дисциплина не относится к {stud.kurs} курсу, {stud.semestr_v_kurse} семестру ({stud.spec})")
        kaf = self.kafedry.get(disc.kafedra)
        if not kaf or not kaf.chitaet_li(disc.nazvanie, stud.spec):
            raise ValueError("Кафедра не читает эту дисциплину для специальности студента")
        if disc in stud.zapisan:
            raise ValueError("Студент уже записан на эту дисциплину")
        stud.zapisan[disc] = None
        stud.ocenki.setdefault(stud.semestr, {})[disc.nazvanie] = None
        return disc

    def ubrat_s_discipliny(self, id_stud, nazv_disc):
        stud = self._stud(id_stud)
        if not stud:
            raise LookupError("Студент не найден")
        disc = self._disc_stud(stud, nazv_disc)
        if not disc:
            raise ValueError("Студент не записан на эту дисциплину")
        del stud.zapisan[disc]
        stud.ocenki.get(stud.semestr, {}).pop(disc.nazvanie, None)
        return disc
