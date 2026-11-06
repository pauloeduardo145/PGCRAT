# PGCRAT
### Plataforma de Gerenciamento de Campanhas de RPG com Assistência de IA

O **PGCRAT** é um projeto de RPG de mesa digital desenvolvido em Python, com interface gráfica em CustomTkinter e integração com uma inteligência artificial local através do Ollama.

O programa tem como objetivo proporcionar uma experiência de RPG na qual uma IA atua como Mestre de Jogo (MJ), conduzindo a narrativa, interpretando personagens e reagindo às decisões do jogador.

## Funcionalidades

### 🎴 Sistema de cartas
- Cartas de personagens, criaturas, habilidades e equipamentos.
- Imagens personalizadas.
- Atributos e características individuais.
- Sistema de raridade.
- Habilidades e efeitos especiais.

### 🎲 Sistema de rolagem de dados
- Dados D4, D6, D8, D10, D12, D20 e D100.
- Rolagem de múltiplos dados.
- Modificadores de atributos.
- Histórico de resultados.

### 📜 Sistema de eventos
- Eventos aleatórios.
- Encontros com personagens.
- Eventos ambientais.
- Armadilhas e recompensas.
- Eventos condicionados às decisões do jogador.

### ⚔️ Sistema de combate
- Combates por turnos.
- Atributos de ataque, defesa e vida.
- Utilização de habilidades e equipamentos.
- Ações de aliados e inimigos.
- Cálculo de dano e efeitos pelo Python.

### 🤖 Inteligência artificial — Mestre de Jogo
Integração com modelos locais através do Ollama.

Responsabilidades da IA:
- Construir e conduzir narrativas.
- Descrever cenários e acontecimentos.
- Interpretar NPCs, aliados e inimigos.
- Reagir às decisões do jogador.
- Criar diálogos e interações.
- Participar da condução dos combates.

A IA será responsável pela interpretação e narrativa, enquanto o Python controlará as regras, os atributos e os resultados das ações.

## Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Lógica e sistemas do RPG |
| CustomTkinter | Interface gráfica |
| Pillow | Manipulação de imagens |
| Ollama | Execução da IA local |
| JSON | Armazenamento de dados |

## Estrutura do projeto

```text
PGCRAT/
│
├── main.py
├── README.md
├── requirements.txt
│
├── sistemas/
│   ├── __init__.py
│   ├── rolagem_dados.py
│   ├── eventos.py
│   ├── sistema_cartas.py
│   └── combate.py
│
├── ia/
│   ├── __init__.py
│   └── mestre.py
│
├── interface/
│   ├── __init__.py
│   ├── janela_principal.py
│   ├── painel_jogador.py
│   ├── painel_narrativa.py
│   └── painel_cartas.py
│
├── dados/
│   ├── cartas.json
│   ├── eventos.json
│   └── personagens.json
│
└── imagens/
    ├── cartas/
    ├── personagens/
    └── cenarios/
```

## Instalação

### 1. Clonar o projeto

```bash
git clone https://github.com/pauloeduardo145/PGCRAT.git
cd PGCRAT
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

```bash
python3 main.py
```

**Observação:** o Ollama deverá estar instalado e em execução para utilizar o Mestre de Jogo.

## Progresso do desenvolvimento

- [x] Estrutura inicial do projeto.
- [x] Implementação inicial da rolagem de dados.
- [ ] Sistema de cartas.
- [ ] Sistema de eventos.
- [ ] Sistema de combate.
- [ ] Integração com Ollama.
- [ ] Interface gráfica.
- [ ] Integração dos módulos.
- [ ] Sistema de salvamento de campanhas.
- [ ] Testes e otimização.

## Licença

Projeto em desenvolvimento. A definição da licença será realizada posteriormente.
