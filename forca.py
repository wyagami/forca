import streamlit as st
import random

# Configurar o layout e título da página
st.set_page_config(page_title="Jogo da Forca", layout="centered")
st.title("Jogo da Forca")
st.sidebar.header("Instruções")
st.sidebar.write("""
- Adivinhe a palavra secreta escolhendo uma letra de cada vez.
- Você tem 6 tentativas para adivinhar a palavra.
- Cada vitória soma 10 pontos, e cada derrota subtrai 5 pontos.
- Boa sorte!
""")

# Lista de palavras organizadas por categorias
palavras = {
    "Animais": [
        "cachorro", "gato", "vaca", "galinha", "porco",
        "pato", "coelho", "cavalo", "ovelha", "cabra",
        "leão", "tigre", "elefante", "zebra", "girafa",
        "hipopótamo", "rinoceronte", "camelo", "urso", "crocodilo"
    ],
    "Frutas": [
        "banana", "maçã", "laranja", "uva", "morango",
        "abacaxi", "melancia", "kiwi", "pêssego", "pera",
        "manga", "caju", "acerola", "goiaba", "carambola",
        "pitanga", "abacate", "maracujá", "tangerina", "limão"
    ],
    "Cores": [
        "vermelho", "azul", "amarelo", "verde", "roxo",
        "laranja", "rosa", "marrom", "cinza", "preto",
        "branco", "violeta", "turquesa", "índigo", "magenta",
        "coral", "esmeralda", "dourado", "prateado", "bege"
    ],
    "Natureza": [
        "sol", "lua", "estrela", "árvore", "flor",
        "montanha", "rio", "lago", "floresta", "oceano",
        "deserto", "vulcão", "campo", "grama", "nuvem",
        "tempestade", "arco-íris", "relâmpago", "neve", "areia"
    ],
    "Países": [
        "brasil", "argentina", "canadá", "estados-unidos", "méxico",
        "frança", "alemanha", "itália", "espanha", "portugal",
        "rússia", "japão", "china", "índia", "austrália",
        "egito", "turquia", "coreia do sul", "suécia", "noruega"
    ],
    "Cidades": [
        "são paulo", "rio de janeiro", "brasília", "salvador", "fortaleza",
        "belo horizonte", "curitiba", "recife", "porto alegre", "manaus",
        "belém", "goiânia", "campinas", "vitória", "são luís",
        "maceió", "natal", "florianópolis", "joão pessoa", "aracaju"
    ],
    "Esportes": [
        "futebol", "basquete", "vôlei", "tênis", "natação",
        "atletismo", "ciclismo", "boxe", "judô", "karatê",
        "ginástica", "esgrima", "beisebol", "críquete", "hóquei",
        "rugby", "polo", "surfe", "skate", "escalada"
    ],
    "Profissões": [
        "engenheiro", "médico", "advogado", "professor", "arquiteto",
        "enfermeiro", "dentista", "jornalista", "policial", "bombeiro",
        "empresário", "contador", "psicólogo", "veterinário", "artista",
        "designer", "programador", "cozinheiro", "piloto", "motorista"
    ],
    "Instrumentos": [
        "violão", "piano", "bateria", "violino", "saxofone",
        "guitarra", "flauta", "clarinete", "trompete", "contrabaixo",
        "órgão", "acordeão", "harpa", "banjo", "mandolim",
        "cello", "oboé", "fagote", "maracas", "sintetizador"
    ],
    "Filmes": [
        "inception", "avatar", "matrix", "titanic", "gladiador",
        "jurassic park", "interstellar", "batman", "superman", "up",
        "frozen", "avengers", "indiana jones", "rocky", "forrest gump",
        "star wars", "harry potter", "lord of the rings", "shawshank", "godfather"
    ],
    "Objetos": [
        "cadeira", "mesa", "computador", "televisão", "celular",
        "geladeira", "micro-ondas", "fogão", "sofá", "cama",
        "armário", "lâmpada", "livro", "relógio", "espelho",
        "ventilador", "quadro", "caneta", "copo", "garrafa"
    ],
    "Tecnologia": [
        "smartphone", "internet", "software", "hardware", "robô",
        "computador", "tablet", "drone", "inteligência artificial", "realidade virtual",
        "3d-impressão", "cloud computing", "big data", "blockchain", "cybersecurity",
        "nanotecnologia", "automação", "wearable", "data center", "algoritmo"
    ],
    "Insetos": [
        "abelha", "formiga", "borboleta", "mosca", "barata",
        "besouro", "libélula", "gafanhoto", "mariposa", "cupim",
        "cigarra", "percevejo", "pulga", "mosquito", "joaninha",
        "grilo", "lagarta", "colémbolo", "traça", "cigarrinha"
    ],
    "Comidas": [
        "pizza", "hambúrguer", "sushi", "lasanha", "salada",
        "feijoada", "churrasco", "coxinha", "pastel", "brigadeiro",
        "macarrão", "arroz", "bife", "frango", "peixe",
        "sopa", "omelete", "quibe", "empada", "torta"
    ]
}

# Inicializar o estado do jogo, se necessário
if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = 0
if 'categoria' not in st.session_state:
    st.session_state.categoria = random.choice(list(palavras.keys()))
if 'palavra_secreta' not in st.session_state:
    st.session_state.palavra_secreta = random.choice(palavras[st.session_state.categoria])
if 'letras_adivinhadas' not in st.session_state:
    st.session_state.letras_adivinhadas = []
if 'tentativas_restantes' not in st.session_state:
    st.session_state.tentativas_restantes = 6

# Função para reiniciar o jogo
def reiniciar_jogo():
    st.session_state.categoria = random.choice(list(palavras.keys()))
    st.session_state.palavra_secreta = random.choice(palavras[st.session_state.categoria])
    st.session_state.letras_adivinhadas = []
    st.session_state.tentativas_restantes = 6

# Função para exibir a palavra com as letras adivinhadas
def exibir_palavra():
    exibicao = ""
    for letra in st.session_state.palavra_secreta:
        if letra in st.session_state.letras_adivinhadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

# Função para verificar se o jogador venceu
def verificar_vitoria():
    return all(letra in st.session_state.letras_adivinhadas for letra in st.session_state.palavra_secreta)

# Função que retorna o desenho do boneco (ASCII art) conforme as tentativas restantes
def desenhar_boneco(tentativas):
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    return estados[6 - tentativas]

# Função para tocar som de vitória ou derrota utilizando st.audio()
def tocar_som(vitoria):
    if vitoria:
        som_url = "https://www.soundjay.com/misc/sounds/magic-chime-01.mp3"
    else:
        som_url = "https://www.soundjay.com/misc/sounds/fail-trombone-01.mp3"
    st.audio(som_url, format="audio/mp3")

# Exibir as informações do jogo (essas informações serão atualizadas após cada reexecução)
st.write(f"**Categoria:** {st.session_state.categoria}")
st.write(f"**Pontuação atual:** {st.session_state.pontuacao}")
st.write(f"**Tentativas restantes:** {st.session_state.tentativas_restantes}")
st.write(f"**Palavra secreta:** {exibir_palavra()}")
st.text(desenhar_boneco(st.session_state.tentativas_restantes))

# Área para entrada de dados do jogador
col1, col2 = st.columns([2, 1])
with col1:
    letra = st.text_input("Digite uma letra:", max_chars=1, key="input_letra").lower()
with col2:
    if st.button("Enviar"):
        if letra.isalpha() and len(letra) == 1:
            if letra in st.session_state.letras_adivinhadas:
                st.warning("Você já tentou essa letra!")
            else:
                st.session_state.letras_adivinhadas.append(letra)
                if letra in st.session_state.palavra_secreta:
                    st.success(f"Letra correta: **{letra.upper()}**")
                else:
                    st.session_state.tentativas_restantes -= 1
                    st.error(f"Letra incorreta: **{letra.upper()}**")
        else:
            st.warning("Por favor, insira uma letra válida.")
        # Reexecuta o script para atualizar todas as informações na tela
        st.rerun()

# Verificar se o jogador venceu ou perdeu
if verificar_vitoria():
    st.success("Parabéns! Você acertou a palavra!")
    st.session_state.pontuacao += 10
    tocar_som(True)
    if st.button("Jogar novamente"):
        reiniciar_jogo()
        st.rerun()

elif st.session_state.tentativas_restantes <= 0:
    st.error(f"Você perdeu! A palavra era: {st.session_state.palavra_secreta}")
    st.session_state.pontuacao -= 5
    tocar_som(False)
    if st.button("Jogar novamente"):
        reiniciar_jogo()
        st.rerun()
