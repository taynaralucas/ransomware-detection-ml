# Relatório Técnico – Detecção de Ransomware com Machine Learning

Autora: Taynara Aparecida Castilho Lucas
Projeto desenvolvido como extensão prática do Trabalho de Conclusão de Curso.

Relatório Técnico – Desenvolvimento do Projeto de Detecção de Ransomware com Machine Learning

1. Introdução
Este relatório descreve, de forma detalhada, o desenvolvimento prático de um sistema de detecção de ransomware utilizando técnicas de Machine Learning, com base no dataset CIC-MalMem-2022. O projeto tem como objetivo implementar, de maneira prática, os conceitos estudados no Trabalho de Conclusão de Curso.
O desenvolvimento buscou seguir boas práticas de engenharia de software e projetos de Machine Learning, contemplando organização de código, versionamento, reprodutibilidade e avaliação de desempenho do modelo.

2. Organização inicial do projeto
Inicialmente, foi definida a estrutura básica do projeto, visando a separação clara de responsabilidades e a organização dos artefatos gerados durante o desenvolvimento. Para isso, foram criados os seguintes diretórios:
•	docs/: destinado ao relatório do projeto;
•	src/: destinado ao código-fonte do projeto;
•	data/: destinado ao armazenamento do dataset utilizado;
•	models/: destinado aos modelos treinados e demais artefatos gerados após o treinamento.
Além disso, foi criado o arquivo “.gitignore”, com o objetivo de evitar o versionamento de arquivos grandes ou sensíveis, como o dataset bruto e os modelos treinados. Essa decisão segue boas práticas em projetos de Machine Learning, uma vez que tais artefatos podem ser regenerados a partir do código-fonte.

3. Versionamento e controle de alterações
O projeto foi versionado utilizando Git, com repositório remoto hospedado no GitHub. O versionamento permitiu o acompanhamento incremental das alterações realizadas ao longo do desenvolvimento, por meio de commits com mensagens descritivas, facilitando a rastreabilidade e a organização do histórico do projeto.
Desde o início, adotou-se a prática de versionar exclusivamente o código-fonte e os arquivos de documentação, mantendo fora do repositório os dados brutos (data/) e os modelos treinados (models/). Essa abordagem garante um repositório leve, organizado e reprodutível, alinhado com práticas adotadas em ambientes profissionais e acadêmicos.

4. Dataset e contexto dos dados
O projeto utiliza o dataset CIC-MalMem-2022, desenvolvido pelo Canadian Institute for Cybersecurity (CIC) da Universidade de New Brunswick (UNB). Esse conjunto de dados foi construído a partir da análise de dumps de memória RAM coletados em ambiente Windows 10, com foco na detecção de malwares ofuscados.
O dataset contém 58.596 amostras, distribuídas de forma balanceada entre as classes Benign e Malware, e aproximadamente 55 atributos numéricos, representando características extraídas da memória do sistema. O balanceamento entre as classes elimina a necessidade de técnicas adicionais de balanceamento, como oversampling ou undersampling.

5. Análise exploratória e preparação dos dados
Após a organização inicial do projeto, iniciou-se o desenvolvimento do código principal no arquivo train_model.py, localizado na pasta src/. A primeira etapa consistiu no carregamento do dataset utilizando a biblioteca Pandas, permitindo a leitura e manipulação eficiente dos dados.
Em seguida, foi realizada uma análise estrutural do conjunto de dados, verificando:
•	número de amostras e atributos;
•	tipos de dados de cada coluna;
•	presença de valores nulos;
•	distribuição das classes.
A análise confirmou que o dataset não possui valores ausentes e apresenta distribuição perfeitamente balanceada entre as classes Benign e Malware.
Posteriormente, os dados foram preparados para o treinamento do modelo. A variável alvo (Class) foi separada das variáveis preditoras, e colunas que não contribuem diretamente para o processo de classificação, como Category e Filename, foram removidas. Essa etapa garante que o modelo seja treinado apenas com atributos relevantes.

6. Codificação da variável alvo
Como o algoritmo XGBoost requer rótulos numéricos para a variável alvo, foi aplicada a técnica de codificação de rótulos utilizando o LabelEncoder. Essa etapa converteu as classes textuais (Benign e Malware) em valores numéricos, garantindo compatibilidade com o algoritmo e mantendo a correspondência entre os rótulos originais e os valores codificados.
A escolha do LabelEncoder permite também a posterior decodificação das predições, tornando os resultados interpretáveis.

7. Divisão dos dados e treinamento do modelo
Após a preparação dos dados, o conjunto foi dividido em dados de treino e teste utilizando a função train_test_split, com estratificação das classes. Essa abordagem assegura que a proporção entre as classes seja mantida em ambos os conjuntos, permitindo uma avaliação justa do desempenho do modelo.
O treinamento foi realizado utilizando o algoritmo XGBoost, escolhido por seu elevado desempenho, robustez e eficiência computacional em tarefas de classificação, além de sua relevância em estudos acadêmicos e aplicações reais na área de segurança da informação.
O modelo foi treinado com parâmetros iniciais padrão, suficientes para validar a eficácia da abordagem proposta.

8. Avaliação do desempenho
Após o treinamento, o modelo foi avaliado utilizando o conjunto de teste. Foram calculadas métricas de desempenho amplamente utilizadas em problemas de classificação, incluindo:
•	acurácia;
•	precisão;
•	recall;
•	F1-score.
Os resultados demonstraram desempenho elevado, com acurácia aproximada de 99,99%, além de métricas equilibradas entre as classes. Esses resultados confirmam a eficácia do modelo e são coerentes com os achados apresentados no Trabalho de Conclusão de Curso.

9. Persistência do modelo e inferência
Após a validação do desempenho, o modelo treinado e o codificador de rótulos foram persistidos utilizando a biblioteca Joblib. Para garantir portabilidade e correta organização dos arquivos, foi adotado o uso de caminhos absolutos, assegurando que os artefatos fossem salvos na pasta models/, localizada na raiz do projeto, independentemente do diretório de execução do script.
Em seguida, foi desenvolvido o script predict.py, responsável por carregar o modelo treinado e o LabelEncoder, preparar novos dados de entrada e realizar a predição das classes. Esse script completa o pipeline do projeto, permitindo a utilização prática do modelo para inferência em novos conjuntos de dados.

10. Considerações finais
Ao longo do desenvolvimento, o projeto seguiu boas práticas de organização, versionamento e reprodutibilidade. O resultado final é um pipeline funcional de Machine Learning, contemplando todas as etapas necessárias, desde o carregamento dos dados até a inferência.
O projeto demonstra, na prática, a aplicação dos conceitos estudados no TCC, validando experimentalmente o uso do algoritmo XGBoost na detecção de ransomware.