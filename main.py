import sys
import os
from num2words import num2words
import pyperclip
# import do PyQt5

from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QFileDialog


from src.gui import gui
from src.doc import Documento

meses = [
    "",
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
]

semana = [
    "",
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]

departamentos = [
    "Geografia",
    "Geologia",
    "Mineralogia e Petrologia",
    "Paleontologia e Estratigrafia",
    "Geodésia"
]

secretaria = [
    "Ariane Kravczyk Bernardes",
    "Erick Vaz",
    "Leonel Furtado Gonçalves",
    "Zélia da Silva Zaghetto",
]


class Convoc:

    head = ""
    mensagem = ""
    data = ""
    assinatura = ""
    pautas = ""
    prof = ""
    tec = ""
    alunos = ""

    def __init__(self):
        self.departamento = gui.uiConvoc.departamentoCombo.currentText()
        self.numero = gui.uiConvoc.convSpin.text()
        self.data_convc = gui.uiConvoc.convDate.date()
        self.presidencia = gui.uiConvoc.nomeLine.text()
        self.genero = bool(gui.uiConvoc.generoCombo.currentIndex())
        self.titulo = gui.uiConvoc.tituloLine.text()
        self.local = gui.uiConvoc.localLine.text()
        self.data_reuniao = gui.uiConvoc.reuniaoDate.date()
        self.hora_reuniao = gui.uiConvoc.reuniaoTime.time()
        convoc_pautas()
        self.pautas = gui.uiConvoc.pautaText.toPlainText().split("\n")
        # self.pautas = "\n".join(self.pautas)
        self.prof = gui.uiConvoc.profText.toPlainText().split("\n")
        self.prof.sort()
        self.prof = ", ".join(self.prof)
        self.tecnicos = gui.uiConvoc.tecnicosText.toPlainText().split("\n")
        self.tecnicos.sort()
        self.tecnicos = ", ".join(self.tecnicos )
        self.alunos = gui.uiConvoc.alunosText.toPlainText().split("\n")
        self.alunos.sort()
        self.alunos = ", ".join(self.alunos)

    def gerar_titulo(self):
        titulo = "Convocação "
        numero = str(self.numero)
        while len(numero) < 3:
            numero = "0" + numero
        titulo += numero + "/" + str(self.data_convc.year())
        self.head = titulo

    def gerar_mensagem(self):

        if self.genero:
            mensagem = "A "
        else:
            mensagem = "O "
        mensagem += self.titulo + " de " + self.departamento + " CONVOCA Vossa Senhoria para reunião departamental,"
        mensagem += " a ser realizada no dia " + str(
            self.data_reuniao.day()) + " de " + meses[self.data_reuniao.month()]
        mensagem += ", " + semana[self.data_reuniao.dayOfWeek()] + ", às "
        mensagem += str(self.hora_reuniao.hour()) + "h" + str(
            self.hora_reuniao.minute()) + "min, " + self.local + ", com a seguinte pauta:"

        self.mensagem = mensagem

    def gerar_assinatura(self):
        self.data = "Porto Alegre, " + str(self.data_convc.day())
        self.data += " de " + meses[self.data_convc.month()]
        self.data += " de " + str(self.data_convc.year()) + ".\n\n"
        self.assinatura = "[O original encontra-se assinado]\n"
        if self.genero:
            self.assinatura += "Prof.ª "
        else:
            self.assinatura += "Prof. "
        self.assinatura += self.presidencia + ",\n"
        self.assinatura += self.titulo


class Ata:

    head = ""
    abertura = ""    
    pautas = ""
    encerramento = ""

    def __init__(self):
        self.departamento = gui.uiAta.departamentoCombo.currentText()
        self.numero = gui.uiAta.convSpin.text()
        self.secretaria = gui.uiAta.secLine.text()
        self.presidencia = gui.uiAta.nomeLine.text()
        self.genero = bool(gui.uiAta.generoCombo.currentIndex())
        self.titulo = gui.uiAta.tituloLine.text()
        self.local = gui.uiAta.localLine.text()
        self.data = gui.uiAta.reuniaoDate.date()
        self.inicio = gui.uiAta.inicioTime.time()
        self.fim = gui.uiAta.fimTime.time()
        ata_pautas()
        self.pautas = gui.uiAta.pautaText.toPlainText().split("\n")        
        self.prof = gui.uiAta.profText.toPlainText().split("\n")
        self.prof.sort()
        self.prof = ", ".join(self.prof)
        self.tecnicos = gui.uiAta.tecnicosText.toPlainText().split("\n")
        self.tecnicos.sort()
        self.tecnicos = ", ".join(self.tecnicos )
        self.alunos = gui.uiAta.alunosText.toPlainText().split("\n")
        self.alunos.sort()
        self.alunos = ", ".join(self.alunos)

    def gerar_titulo(self):
        titulo = "Ata "
        numero = str(self.numero)
        while len(numero) < 3:
            numero = "0" + numero
        titulo += numero + "/" + str(self.data.year())
        self.head = titulo

    def gerar_mensagem(self):
        mensagem = "Ao " + escreve_data(self.data) + ", às " + escreve_hora(self.inicio)
        mensagem += ", " + self.local + ", sob a presidência d"
        pronome = ""
        if self.genero:
            pronome = "a Professora "
        else:
            pronome = "o Professor "
        mensagem += pronome + self.presidencia + ", reuniu-se a Plenária do Departamento de "
        mensagem += self.departamento + ", estando presentes "
        presentes = ""
        if len(self.prof):
            presentes += "os professores: " + self.prof + "; "
        if len(self.tecnicos):
            presentes += "os técnicos-administrativos: " + self.tecnicos + "; "
        if len(self.alunos):
            presentes += "os representantes discentes: " + self.alunos + "; "
        mensagem += presentes[:-2] + ". "
        mensagem += pronome.capitalize() + self.presidencia
        mensagem += " agradeceu a presença de todos e deu início a sessão com a seguinte ordem do dia: "
        self.abertura = mensagem
        mensagem = "Por fim, " + pronome.capitalize() + self.presidencia + " agradeceu a presença de todos. "
        mensagem += "Nada mais havendo a tratar, a reunião foi encerrada às " + escreve_hora(self.fim)
        mensagem += ", do que, para constar eu, "
        mensagem += self.secretaria
        linha = " "
        count = round((len(self.secretaria)/3)*2)
        for i in range(0, count):
            linha += "__"
        mensagem += linha
        mensagem += " Assistente em Administração, lavrei a presente ata."
        self.encerramento = mensagem


def escreve_data(data):
    texto = num2words(data.day(), lang="pt_BR", to="ordinal")
    texto += " dia do mês de " + meses[data.month()] + " do ano de " + num2words(data.year(), lang="pt_BR")
    return texto


def escreve_hora(hora):
    texto = num2words(hora.hour(), lang="pt_BR")
    texto = texto.replace("um", "uma")
    texto = texto.replace("dois", "duas")
    texto += " horas e " + num2words(hora.minute(), lang="pt_BR") + " minutos"
    return texto


def main_botao_depart():
    print(departamentos)
    gui.wDepartamentos.show()
    depart_combo()


def main_botao_conv():
    gui.wConvoc.show()
    convoc_combo()


def main_botao_ata():
    gui.wAta.show()
    ata_combo()
    

def convoc_combo():
    arquivos_ler(gui.uiConvoc, presidente=True)


def ata_combo():
    arquivos_ler(gui.uiAta, presidente=True)


def depart_combo():
    arquivos_ler(gui.uiDepartamentos)


def depart_salvar():
    arquivos_gravar(gui.uiDepartamentos)


def arquivos_ler(janela, presidente=False):
    departamento = janela.departamentoCombo.currentText()
    print(departamento)
    docentes = []
    tecnicos = []
    discentes = []
    for lista, nome in [
        (docentes, "docentes"),
        (tecnicos, "tecnicos"),
        (discentes, "discentes")
    ]:
        arquivo = open("data/" + departamento + "/" + nome + ".txt", "r")
        temp = arquivo.read().split("\n")
        arquivo.close()
        while "" in temp:
            temp.remove("")
        temp.sort()
        for item in temp:
            item = item.rstrip()
            item = item.title()
            lista.append(item)
        print(lista)
    janela.profText.clear()
    janela.profText.setText("\n".join(docentes))
    if presidente:
        completer = QCompleter(docentes)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        janela.nomeLine.setCompleter(completer)
    janela.tecnicosText.clear()
    janela.tecnicosText.setText("\n".join(tecnicos))
    janela.alunosText.clear()
    janela.alunosText.setText("\n".join(discentes))


def arquivos_gravar(janela):
    departamento = janela.departamentoCombo.currentText()
    print(departamento)

    docentes = janela.profText.toPlainText()
    tecnicos = janela.tecnicosText.toPlainText()
    discentes = janela.alunosText.toPlainText()

    for lista, nome in [
        (docentes, "docentes"),
        (tecnicos, "tecnicos"),
        (discentes, "discentes")
    ]:
        print(nome, lista)
        arquivo = open("data/" + departamento + "/" + nome + ".txt", "w")
        arquivo.write(lista)
        arquivo.close()
    gui.wDepartamentos.close()


def convoc_botao_ok():
    global Convocacao
    Convocacao = Convoc()
    Convocacao.gerar_mensagem()
    Convocacao.gerar_titulo()
    Convocacao.gerar_assinatura()

    pautas = "\n"
    cont = 0

    for item in Convocacao.pautas:
        cont += 1
        pautas += str(cont) + ". " + item + "\n"

    word = ""

    for texto in [
        Convocacao.head,
        Convocacao.mensagem,
        pautas,
        Convocacao.data,
        Convocacao.assinatura,
    ]:
        word += texto+"\n"

    word += "\n"

    for texto, lista in [
        ("Docentes", Convocacao.prof),
        ("Técnicos", Convocacao.tecnicos),
        ("Discentes", Convocacao.alunos)
    ]:
        if len(lista):
            word += texto+ ": " + lista + "\n"

    agora = QTime.currentTime().hour()

    email = ""
    if 5 < agora < 12:
        email = "Bom dia,\n\n"
    elif 11 < agora < 20:
        email = "Boa tarde,\n\n"
    else:
        email = "Boa noite,\n\n"

    for texto in [
        Convocacao.mensagem,
        pautas,
    ]:
        email += texto+"\n"

    gui.uiConvocGerar.emailText.setText(email)
    gui.uiConvocGerar.docText.setText(word)
    gui.wConvocGerar.show()


def ata_botao_ok():
    global Minuta

    Minuta = Ata()
    Minuta.gerar_titulo()
    Minuta.gerar_mensagem()
    texto = Minuta.head + "\n\n" + Minuta.abertura
    for i in Minuta.pautas:
        texto += "\n" + i
    texto += "\n" + Minuta.encerramento
    gui.uiAtaGerar.docText.setText(texto)
    gui.wAtaGerar.show()


def ata_gerar_botao_ok():
    global Minuta

    Doc = Documento(selectFile())
    Doc.cabecalho(Minuta.departamento)
    Doc.titulo(Minuta.head)
    Doc.ata(Minuta.abertura, Minuta.pautas, Minuta.encerramento)
    Doc.salvar()
    gui.wAtaGerar.hide()
    gui.wAta.hide()


def ata_gerar_cancel():
    gui.wAtaGerar.hide()


def convoc_gerar_botao_doc():
    global Convocacao

    Doc = Documento(selectFile())
    Doc.cabecalho(Convocacao.departamento)
    Doc.titulo(Convocacao.head)
    Doc.convoc(Convocacao.mensagem)
    Doc.pauta(Convocacao.pautas)
    Doc.data(Convocacao.data)
    Doc.assinatura(Convocacao.assinatura)
    Doc.rodape(
        Convocacao.prof,
        Convocacao.tecnicos,
        Convocacao.alunos
    )
    Doc.salvar()


def convoc_gerar_botao_email():
    pyperclip.copy(gui.uiConvocGerar.emailText.toPlainText())


def convoc_gerar_ok():
    gui.wConvocGerar.hide()
    gui.wConvoc.hide()


def convoc_gerar_cancel():
    gui.wConvocGerar.hide()


def convoc_pautas():
    limpar_pautas(gui.uiConvoc)


def ata_pautas():
    limpar_pautas(gui.uiAta)


def limpar_pautas(janela):
    texto = janela.pautaText.toPlainText()
    texto = texto.replace("\x00", "")
    linhas = texto.split("\n")
    if "" in linhas:
        linhas.remove("")
    linhas_nova = []
    for linha in linhas:
        while not linha[0].isalpha():
            linha = linha[1:]
        linhas_nova.append(linha)
    texto = "\n".join(linhas_nova)
    janela.pautaText.setText(texto)


def selectFile():
    arquivo = QFileDialog.getSaveFileUrl(
        caption="Salvar arquivo",
        filter="Documento (*.docx)"
    )
    return arquivo[0].path()+".docx"


gui = gui()

#textos
sec_completer = QCompleter(secretaria)
sec_completer.setCaseSensitivity(Qt.CaseInsensitive)
gui.uiAta.secLine.setCompleter(sec_completer)

#datas

hoje = QDate.currentDate()
for data in [
    gui.uiConvoc.convDate,
    gui.uiConvoc.reuniaoDate,
    gui.uiAta.reuniaoDate
]:
    data.setDate(hoje)

#combos
for combo in [
    gui.uiDepartamentos.departamentoCombo,
    gui.uiConvoc.departamentoCombo,
    gui.uiAta.departamentoCombo
]:
    combo.addItems(departamentos)

gui.uiDepartamentos.departamentoCombo.currentTextChanged.connect(depart_combo)
gui.uiConvoc.departamentoCombo.currentTextChanged.connect(convoc_combo)
gui.uiAta.departamentoCombo.currentTextChanged.connect(ata_combo)

#teste


#botões
gui.ui.departamentosButton.clicked.connect(main_botao_depart)
gui.ui.convocacaoButton.clicked.connect(main_botao_conv)
gui.ui.ataButton.clicked.connect(main_botao_ata)
gui.uiConvoc.limparButton.clicked.connect(convoc_pautas)
gui.uiConvocGerar.wordButton.clicked.connect(convoc_gerar_botao_doc)
gui.uiConvocGerar.emailButton.clicked.connect(convoc_gerar_botao_email)


#botões de diálogo
gui.uiDepartamentos.buttonBox.accepted.connect(depart_salvar)
gui.uiDepartamentos.buttonBox.rejected.connect(gui.wDepartamentos.close)
gui.uiConvoc.buttonBox.accepted.connect(convoc_botao_ok)
gui.uiConvoc.buttonBox.rejected.connect(gui.wConvoc.close)
gui.uiConvocGerar.buttonBox.accepted.connect(convoc_gerar_ok)
gui.uiConvocGerar.buttonBox.rejected.connect(convoc_gerar_cancel)
gui.uiAta.buttonBox.accepted.connect(ata_botao_ok)
gui.uiAta.buttonBox.rejected.connect(gui.wAta.close)
gui.uiAtaGerar.buttonBox.accepted.connect(ata_gerar_botao_ok)
gui.uiAtaGerar.buttonBox.rejected.connect(convoc_gerar_cancel)

sys.exit(gui.app.exec_())