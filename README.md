**Fut7 - Sorteador de Equipes (Padrão MVC)**

Sistema em Python para gestão de partidas de futebol de 7 (Fut7) e sorteio de equipes, desenvolvido aplicando o padrão de arquitetura MVC (Model-View-Controller) e conceitos fundamentais de Programação Orientada a Objetos.
---
## Funcionalidades
- Registo de Jogadores: Adição de até 14 jogadores com verificação automática de duplicados e definição de posição (Goleiro/Linha).
- Remoção de Jogadores: Permite retirar um jogador da lista de confirmados através do nome.
- Sorteio automático: Distribuição automática e aleatória de 1 goleiro e 6 jogadores de linha para cada equipe (Branco vs Preto).
- Listagem dos jogadores: Exibição clara e alinhada dos jogadores confirmados e das equipes sorteadas no terminal.
---
## Conceitos e Ferramentas Aplicadas
- Linguagem: Python
- Bibliotecas Nativas: random (para o algoritmo de sorteio)
- Modelagem Visual: Draw.io (Diagramação UML de classes)
- Controle de Versões: Git e GitHub

### Estruturas e Conceitos de Programação
- Arquitetura MVC: Separação estrita de responsabilidades entre as camadas de dados (Model), controle (Controller) e interface (View).
- Programação Orientada a Objetos:
  - Encapsulamento com atributos e métodos privados (__atributo).
  - Utilização de @property e getters/setters para acesso seguro aos dados.
  - Métodos de domínio e responsabilidade única.
- Estruturas de Repetição e Controle:
  - Loop de execução contínuo com while True.
  - Navegação de menu moderna com match case e wildcard case _.
  - Iterações e varreduras com laços for.
- Manipulação e Fatiamento de Listas:
  - Embaralhamento aleatório com random.shuffle.
  - Divisão e distribuição de equipes utilizando fatiamento de listas.
  - Métodos de lista como .append() e .extend().
- Tratamento e Validação de Dados:
  - Sanitização de texto (.strip(), .lower()).
  - Prevenção de duplicados pelo nome e controle rígido de limite de vagas (máximo de 14 jogadores).
---
## Estrutura do Projeto
```text
Time FUT7/
│
├── Controller/
│   └── partida_controller.py
├── Diagrama/
│   └── Modelação Time Fut7.png
├── Model/
│   ├── jogador.py
│   └── partida.py
├── View/
│   └── partida_view.py
├── .gitignore
├── main.py
└── README.md
```
Como Executar o Projeto:
1. Clona o repositório:
git clone [https://github.com/kretzerwq/time-fut7-mvc.git](https://github.com/kretzerwq/time-fut7-mvc.git)
cd time-fut7-mvc
2. Executa a aplicação:
python main.py