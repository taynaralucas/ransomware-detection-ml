# Ransomware Detection using Machine Learning

## Descrição
Este projeto implementa um sistema de detecção de ransomware utilizando técnicas de Machine Learning, com foco no algoritmo XGBoost. O modelo foi treinado a partir do dataset público CIC-MalMem-2022, desenvolvido pelo Canadian Institute for Cybersecurity (CIC) da Universidade de New Brunswick (UNB). O conjunto de dados foca na detecção de malwares ofuscados através de engenharia de recursos de memória, amplamente utilizado em pesquisas acadêmicas na área de segurança da informação.

O objetivo é classificar amostras de memória como **Benign** ou **Malware**, auxiliando na identificação de comportamentos maliciosos.


## Dataset
- **Nome:** Cic-MalMem2022
- **Amostras:** 58.596
- **Classes:** Benign / Malware (balanceado)
- **Fonte:** Canadian Institute for Cybersecurity (CIC) – UNB
- **Objetivo:** Detecção de malware ofuscado por meio de engenharia de atributos de memória
- **Atributos:** Aproximadamente 55 atributos extraídos de dumps de memória
- **Sistema de Origem:** Windows 10

> O dataset não é versionado neste repositório, seguindo boas práticas de projetos de Machine Learning.

---

## Tecnologias Utilizadas
- Python
- Pandas
- Scikit-learn
- XGBoost
- Joblib
- Git / GitHub

---

##  Estrutura do Projeto
ransomware-detection-ml/
├── docs/
│ └── relatorio_tecnico.md # Uma descrição detalhada do desenvolvimento do projeto
├── src/
│ ├── train_model.py # Treinamento e avaliação do modelo
│ └── predict.py # Inferência utilizando modelo treinado
├── data/ # Dataset (ignorado pelo Git)
├── models/ # Modelos treinados (ignorado pelo Git)
├── .gitignore
└── README.md

---

##  Treinamento do Modelo
Para treinar o modelo, execute:

cd src
python train_model.py

---

##  Treinamento do Modelo
O script realiza:

- Carregamento e análise do dataset
- Preparação dos dados
- Divisão em conjuntos de treino e teste
- Treinamento do modelo XGBoost
- Avaliação com métricas de classificação
- Salvamento do modelo treinado
