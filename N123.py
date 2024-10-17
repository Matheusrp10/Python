import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkFont

# Estrutura para armazenar dados dos jogadores
jogadores = {
    "Neymar": "Neymar Jr - PSG",
    "Messi": "Lionel Messi - Inter Miami",
    "Cristiano": "Cristiano Ronaldo - Al Nassr",
    "Mbappé": "Kylian Mbappé - PSG",
    "Haaland": "Erling Haaland - Manchester City",
    "Benzema": "Karim Benzema - Al Ittihad",
    "Salah": "Mohamed Salah - Liverpool",
    "Lewandowski": "Robert Lewandowski - Barcelona",
    "Son": "Heung-min Son - Tottenham",
    "Kane": "Harry Kane - Bayern Munich",
}

# Chuteira de Ouro 2023/2024
chuteira_de_ouro = [
    ["Nome", "Clube", "Gols", "Assistências"],
    ["Erling Haaland", "Manchester City", 36, 6],
    ["Kylian Mbappé", "PSG", 31, 8],
    ["Harry Kane", "Bayern Munich", 30, 5],
    ["Mohamed Salah", "Liverpool", 28, 7],
    ["Robert Lewandowski", "Barcelona", 27, 3],
    ["Karim Benzema", "Al Ittihad", 25, 4],
    ["Neymar", "PSG", 24, 10],
    ["Lionel Messi", "Inter Miami", 23, 8],
    ["Son Heung-min", "Tottenham", 21, 5],
    ["Cristiano Ronaldo", "Al Nassr", 20, 2],
    ["Gavi", "Barcelona", 19, 4],
    ["Rodrygo", "Real Madrid", 18, 5],
]

campeonatos = [
    "Premier League", "La Liga", "Bundesliga", "Campeonato Brasileiro"
]

# Classificações dos campeonatos
classificacoes = {
    "Premier League": [
        ["MNC", "Manchester City", 91, 38, 28, 7, 3, 96, 34, 62],
        ["ARS", "Arsenal", 89, 38, 28, 5, 5, 91, 29, 62],
        ["MNU", "Manchester United", 75, 38, 22, 9, 7, 69, 34, 35],
        ["NEW", "Newcastle United", 71, 38, 19, 14, 5, 63, 32, 31],
        ["LIV", "Liverpool", 68, 38, 19, 11, 8, 61, 45, 16],
        ["TOT", "Tottenham", 64, 38, 18, 10, 10, 62, 45, 17],
        ["BHA", "Brighton", 60, 38, 18, 6, 14, 64, 50, 14],
        ["AVL", "Aston Villa", 58, 38, 17, 7, 14, 51, 46, 5],
        ["CHE", "Chelsea", 57, 38, 16, 9, 13, 46, 45, 1],
        ["WOL", "Wolverhampton", 55, 38, 15, 10, 13, 38, 43, -5],
    ],
    "La Liga": [
        ["RMA", "Real Madrid", 95, 38, 29, 8, 1, 87, 26, 61],
        ["FCB", "Barcelona", 85, 38, 26, 7, 5, 79, 44, 35],
        ["ATM", "Atlético de Madrid", 76, 38, 22, 10, 6, 62, 29, 33],
        ["BIL", "Athletic Bilbao", 69, 38, 19, 12, 7, 54, 31, 23],
        ["SFC", "Sevilla", 68, 38, 19, 11, 8, 55, 32, 23],
        ["REAL", "Real Sociedad", 66, 38, 18, 12, 8, 48, 33, 15],
        ["CEL", "Celta de Vigo", 56, 38, 15, 11, 12, 51, 45, 6],
        ["VAL", "Valencia", 53, 38, 15, 8, 15, 49, 56, -7],
        ["VIL", "Villarreal", 50, 38, 14, 8, 16, 40, 50, -10],
        ["EIB", "Eibar", 47, 38, 13, 8, 17, 40, 54, -14],
    ],
    "Bundesliga": [
        ["BAY", "Bayern de Munique", 80, 34, 24, 8, 2, 83, 33, 50],
        ["BVB", "Borussia Dortmund", 79, 34, 23, 10, 1, 77, 32, 45],
        ["BSC", "Hertha Berlim", 66, 34, 18, 12, 4, 62, 40, 22],
        ["RBL", "RB Leipzig", 64, 34, 19, 7, 8, 64, 39, 25],
        ["WOL", "Wolfsburg", 60, 34, 17, 9, 8, 52, 38, 14],
        ["BMG", "Borussia Mönchengladbach", 58, 34, 17, 7, 10, 54, 45, 9],
        ["TSC", "TSG Hoffenheim", 55, 34, 15, 10, 9, 47, 42, 5],
        ["FCN", "Nuremberg", 51, 34, 14, 9, 11, 45, 46, -1],
        ["AUS", "Augsburg", 49, 34, 14, 7, 13, 38, 40, -2],
        ["FRA", "Eintracht Frankfurt", 45, 34, 12, 9, 13, 39, 45, -6],
    ],
    "Campeonato Brasileiro": [
        ["PAL", "Palmeiras", 70, 38, 20, 10, 8, 64, 33, 31],
        ["GRE", "Grêmio", 68, 38, 21, 5, 12, 63, 56, 7],
        ["FLA", "Flamengo", 65, 38, 18, 11, 9, 58, 45, 13],
        ["SAO", "São Paulo", 64, 38, 17, 13, 8, 54, 37, 17],
        ["SFC", "Santos", 59, 38, 17, 8, 13, 50, 45, 5],
        ["COR", "Corinthians", 58, 38, 16, 10, 12, 42, 35, 7],
        ["ATL", "Atlético Mineiro", 56, 38, 14, 14, 10, 47, 49, -2],
        ["VAS", "Vasco", 52, 38, 14, 8, 16, 42, 52, -10],
        ["FLU", "Fluminense", 50, 38, 13, 11, 14, 44, 46, -2],
        ["BOT", "Botafogo", 48, 38, 14, 5, 19, 40, 55, -15],
    ]
}

def criar_janela(titulo, largura, altura):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry(f"{largura}x{altura}")
    janela.configure(bg="black")
    return janela

def criar_label(janela, texto, fonte, cor_fonte, cor_fundo):
    label = tk.Label(janela, text=texto, font=fonte, fg=cor_fonte, bg=cor_fundo)
    return label

def criar_botoes(janela, texto, comando):
    botao = tk.Button(janela, text=texto, command=comando, bg="gray", fg="white")
    return botao

def abrir_tela_campeonatos():
    campeonato_janela = criar_janela("Campeonatos", 400, 300)
    
    font_padrao = tkFont.Font(family="Helvetica", size=12)

    criar_label(campeonato_janela, "Selecione o Campeonato:", font_padrao, "white", "black").pack(pady=10)

    # Combo box para selecionar o campeonato
    campeonato_selecionado = tk.StringVar(value=campeonatos[0])
    combobox = ttk.Combobox(campeonato_janela, textvariable=campeonato_selecionado, values=campeonatos)
    combobox.pack(pady=10)

    def mostrar_classificacao():
        campeonato = campeonato_selecionado.get()
        abrir_tela_classificacao(campeonato)

    botao_mostrar = criar_botoes(campeonato_janela, "Mostrar Classificação", mostrar_classificacao)
    botao_mostrar.pack(pady=20)

def abrir_tela_classificacao(campeonato):
    classificacao_janela = criar_janela(campeonato, 2000, 400)

    font_padrao = tkFont.Font(family="Helvetica", size=12)

    criar_label(classificacao_janela, campeonato, font_padrao, "white", "black").pack(pady=5)

    # Estilização da Treeview
    estilo = ttk.Style()
    estilo.configure("Treeview", background="black", foreground="blue", rowheight=25, fieldbackground="black")
    estilo.configure("Treeview.Heading", background="gray", foreground="blue", font=('APTO', 12, 'bold'))

    tree = ttk.Treeview(classificacao_janela, columns=("Posição", "Clube", "Pontos", "Jogos", "V", "E", "D", "GP", "GC", "SG"), show='headings')
    tree.heading("Posição", text="Posição", anchor=tk.CENTER)
    tree.heading("Clube", text="Clube", anchor=tk.CENTER)
    tree.heading("Pontos", text="Pontos", anchor=tk.CENTER)
    tree.heading("Jogos", text="Jogos", anchor=tk.CENTER)
    tree.heading("V", text="V", anchor=tk.CENTER)
    tree.heading("E", text="E", anchor=tk.CENTER)
    tree.heading("D", text="D", anchor=tk.CENTER)
    tree.heading("GP", text="GP", anchor=tk.CENTER)
    tree.heading("GC", text="GC", anchor=tk.CENTER)
    tree.heading("SG", text="SG", anchor=tk.CENTER)

    # Adicionar dados à tabela
    for classificacao in classificacoes[campeonato]:
        tree.insert("", "end", values=classificacao)

    tree.pack(expand=True, fill='both')

    # Adiciona uma barra de rolagem
    scrollbar = ttk.Scrollbar(classificacao_janela, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

def abrir_tela_chuteira_de_ouro():
    chuteira_janela = criar_janela("Chuteira de Ouro", 800, 400)
    
    font_padrao = tkFont.Font(family="APTO", size=12)

    criar_label(chuteira_janela, "Chuteira de Ouro 2023/2024", font_padrao, "white", "black").pack(pady=10)

    # Estilização da Treeview
    estilo = ttk.Style()
    estilo.configure("Treeview", background="black", foreground="blue", rowheight=25, fieldbackground="black")
    estilo.configure("Treeview.Heading", background="gray", foreground="blue", font=('APTO', 12, 'bold'))

    tree = ttk.Treeview(chuteira_janela, columns=("Nome", "Clube", "Gols", "Assistências"), show='headings')
    tree.heading("Nome", text="Nome", anchor=tk.CENTER)
    tree.heading("Clube", text="Clube", anchor=tk.CENTER)
    tree.heading("Gols", text="Gols", anchor=tk.CENTER)
    tree.heading("Assistências", text="Assistências", anchor=tk.CENTER)

    # Adicionar dados à tabela
    for jogador in chuteira_de_ouro[1:]:  # Ignora o cabeçalho
        tree.insert("", "end", values=jogador)

    tree.pack(expand=True, fill='both')

    # Adiciona uma barra de rolagem
    scrollbar = ttk.Scrollbar(chuteira_janela, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side='right', fill='y')

def abrir_tela_pesquisa():
    pesquisa_janela = criar_janela("Pesquisa de Jogadores", 400, 200)
    
    font_padrao = tkFont.Font(family="Helvetica", size=12)

    criar_label(pesquisa_janela, "Pesquisar Jogador", font_padrao, "white", "black").pack(pady=10)

    entry_jogador = tk.Entry(pesquisa_janela, font=("Helvetica", 12))
    entry_jogador.pack(pady=10)

    botao_buscar = criar_botoes(pesquisa_janela, "Buscar", lambda: buscar_jogador(entry_jogador.get()))
    botao_buscar.pack(pady=20)

def buscar_jogador(nome):
    info = jogadores.get(nome)
    if info:
        messagebox.showinfo("Resultado da Pesquisa", info)
    else:
        messagebox.showinfo("Resultado da Pesquisa", "Jogador não encontrado.")

def abrir_tela_principal():
    global root
    root = tk.Tk()
    root.title("FutMG")  # Título da aplicação
    root.geometry("300x300")
    root.configure(bg="black")

    font_padrao = tkFont.Font(family="Helvetica", size=12)

    criar_label(root, "FutMG", font_padrao, "White", "Black").pack(pady=10)

    botoes = [
        ("Campeonatos", abrir_tela_campeonatos),
        ("Chuteira de Ouro", abrir_tela_chuteira_de_ouro),
        ("Pesquisa de Jogadores", abrir_tela_pesquisa),
    ]

    for texto, comando in botoes:
        botao = criar_botoes(root, texto, comando)
        botao.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    abrir_tela_principal()
