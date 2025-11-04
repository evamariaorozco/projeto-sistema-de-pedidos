Projeto de Dados — Sistema de Pedidos

## Objetivo
Projeto criado para demonstrar fundamentos de **Banco de Dados**, **Análise de Dados** e **Integração Python3 + SQL**, simulando um ambiente de empresa de dados.


## Tecnologias
- Python 3.10+
- SQLite
- Pandas
- Matplotlib

---

## ⚙️ Como Executar
```bash
# 1️- Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate # macOS/Linux
venv\\Scripts\\activate # Windows


# 2- Instalar dependências
pip3 install pandas matplotlib


# 3️⃣ Criar o banco\python3 src/criar_db.py


# 4️⃣ Inserir novos pedidos (pipeline CSV)
python3 src/pipeline_csv.py


# 5️⃣ Analisar dados e gerar gráfico
python3 src/analisar.py