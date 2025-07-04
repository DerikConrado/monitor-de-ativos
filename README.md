📈 Monitor de Ativos da B3 com Python
Este é um projeto de um dashboard web simples, desenvolvido em Python, para monitorar cotações de ações da bolsa de valores brasileira (B3) em tempo quase real. A aplicação utiliza a API da brapi para buscar os dados e o framework Streamlit para criar uma interface de usuário interativa e amigável.
Funcionalidades
Visualização em Cards: Exibe um resumo rápido de cada ativo, incluindo o preço atual e a variação percentual do dia.
Tabela Detalhada: Apresenta uma lista completa dos ativos monitorados com seus respectivos logos, preços e variações.
Atualização de Dados: Inclui um botão para forçar a atualização dos dados e um sistema de cache que atualiza as informações automaticamente a cada 10 minutos para evitar chamadas excessivas à API.
Interface Web Simples: A interface é limpa, intuitiva e pode ser acessada localmente através de qualquer navegador web.
🛠️ Tecnologias Utilizadas
Python 3.10+
Streamlit: Para a criação do dashboard web interativo.
Pandas: Para a manipulação e estruturação dos dados.
Requests: Para realizar as chamadas HTTP à API de dados financeiros.
brapi API: Como fonte de dados das cotações da B3.
⚙️ Configuração e Instalação
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

1.. Pré-requisitos
Ter o Python 3 instalado em seu sistema.

2. Clone ou Faça o Download do Projeto
Se o projeto estiver em um repositório Git, clone-o:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Caso contrário, apenas crie uma pasta para o projeto e adicione o arquivo app.py dentro dela.

3. Crie e Ative um Ambiente Virtual (Recomendado)
Isso isola as dependências do projeto do restante do seu sistema.



# Crie o ambiente virtual
python -m venv venv
# Ative o ambiente
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

4. Instale as Dependências
Crie um arquivo chamado requirements.txt na pasta do projeto com o seguinte conteúdo:
streamlit
pandas
requests

Em seguida, instale todas as bibliotecas de uma vez com o comando:

pip install -r requirements.txt

5. Configure sua Chave de API
Acesse o site brapi.dev e crie uma conta gratuita para obter seu Token de API.
Abra o arquivo app.py em um editor de texto.
Localize a linha TOKEN_API = "SEU_TOKEN_AQUI" e substitua "SEU_TOKEN_AQUI" pelo seu token pessoal.

▶️ Como Executar
Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no seu terminal:

streamlit run app.py

O Streamlit iniciará um servidor local e abrirá o dashboard automaticamente em seu navegador. Caso não abra, o terminal fornecerá a URL local para acesso (geralmente http://localhost:8501).
