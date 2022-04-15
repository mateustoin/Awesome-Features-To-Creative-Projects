## Instalação do Qt

Esse guia servirá para instalar a versão mais atual do Qt para que possa ser utilizada em projetos futuros. Com isso será instalada a IDE Qt Creator e o kit necessário para compilar e executar os códigos. Se quiser acompanhar o passo a passo e explicação sobre o processo e saber mais detalhes sobre o motivo das escolhas do que foi selecionado, pode assistir o [vídeo de instalação](https://youtu.be/0STf7fhVM1k) no meu [canal do youtube](https://www.youtube.com/c/BitToin/) clicando no link do texto ou clicando na thumbnail abaixo.

<!--
[![Instalação Qt](../assets/assets-qt/thumbnail-qt.png)](https://youtu.be/0STf7fhVM1k)
-->

<a href="https://youtu.be/0STf7fhVM1k
" target="_blank"><img src="../assets/assets-qt/thumbnail-qt.png" 
alt="Vídeo sobre instalação do Qt" border="5" /></a>

## 1. Onde baixar o instalador online

Acesse a [página de download](https://www.qt.io/download), depois vá até seção *Downloads for open source users* e clique em *Go open source*. Lá dentro, você encontrará a opção *Download the Qt Online Installer*, basta clicar e aguardar o download finalizar.

![Figura 1. Go open source](../assets/assets-qt/fig1.png)

![Figura 2. Download the Qt Online Installer]()

## 2. Instalação

### 2.1 Abrindo instalador

Se estiver instalando no windows, basta executar o arquivo de instalação. No Linux, primeiro é necessário transformar o arquivo em algo executável, para conseguir abrí-lo. Existem duas formas de fazer isso. A primeira é através da interface gráfica, abrindo a pasta e clicando com botão direito no instalador, *Propriedades -> Permissões -> Permitir execução do arquivo como um programa*. 

![Figura 3. Permissão de execução do instalador]()

A segunda forma é abrindo a pasta onde o arquivo pelo terminal e digitar o seguinte comando:

`sudo chmod +x nome_do_arquivo`

E depois para executá-lo:

`./nome_do_arquivo`

Executar pelo terminal nos dá a vantagem de ter uma noção melhor do que está acontecendo, visualizando a saída no próprio console, principalmente se houver algum erro durante a execução do processo.

### 2.2 Welcome

Nessa tela será necessário fazer o login, então basta criar uma conta grátis a partir do botão *Sign up* ou no site em que foi feito o download do instalador.

![Figura 4. Criação de conta para acessar os serviços]()

Após isso, basta aceitar os termos e condições, além de aceitar que o uso não é comercial, pois estaremos utilizando principalmente para o desenvolvimento de protótipos e projetos pessoais.

![Figura 5. Aceitando termos necessários]()

### 2.3 Contribuição, Pasta e acordo

Na seção de contribuição, você decide se quer ajudar com dados estatísticos ou não. Depois disso pode ser escolhida a pasta padrão, que particularmente sempre deixo o padrão, além de poder escolher a versão LTS mais nova para desenvolver com o Qt que é a 6.2 e as bibliotecas necessárias para desenvolver para Android e iOS (dispositivos móveis), que pode ser útil no futuro.

![Figura 6. Pasta de instalação e Bibliotecas básicas]()

Com isso, basta aceitar os acordos de licença e aguardar o download e instalação. Pode demorar um pouco, por ter que baixar muitos arquivos, mas assim que acabar poderemos testar, criando o primeiro projeto. Quando finalizar, marque para inicializar a IDE Qt Creator.

![Figura 7. Execução do Qt Creator após fim da instalação]()

## 3. Criando primeiro projeto

### 3.1 Interface inicial do Qt Creator

Após abrir o Qt Creator, a IDE possui diversas áreas em sua interface para acessar. Aqui estão a descrição de algumas delas:

![Figura 8. Interface Inicial do Qt Creator]()

1. Área de criação e configuração básica de projetos
2. Abrir um projeto existente
3. Acesso à documentação offline do Qt, direto na IDE
4. Acesso aos seus projetos pessoais já criados ou abertos na IDE
5. Exemplos de projetos fornecidos pelo próprio Qt para se basear em projetos novos
6. Tutoriais fornecidos pelo Qt para aprendizado de bibliotecas e ferramentas
7. Loja para instalação de features adicionais que podem ser pagas ou grátis
8. Lista de Projetos para acessar rapidamente na IDE
9. Acessa página de Download
10. Acessa página para criar conta no Qt
11. Acessa o fórum do Qt
12. Acessa o blog do Qt
13. Acessa a documentação do Qt, mesmo do nº 3

### 3.2 Create Poject

Agora precisamos validar a instalação e ver se tudo está funcionando corretamente. Para isso, basta clicar em *Create Project...* e com isso abrirá uma janela com várias opções de projetos. Inicialmente testaremos a Qt Widgets Application. *Application (Qt) -> Qt Widgets Application -> Choose...*

![Figura 9. Escolhendo template de projeto]()

Em *Location*, escolha um *nome* para o projeto e a *localização* dele no computador, depois prossiga.

![Figura 10. Escolhendo nome do projeto e localização]()

Em *Build System*, escolha *CMake* de preferência, pois é o novo padrão adotado a partir do Qt 6.

![Figura 11. Escolhendo sistema de build do projeto]()

Em *Details* serão informados os nomes referentes a classe que estará no esqueleto do projeto. O nome da classe que irá compor a janela principal da interface, além da criação do form para o design dessa tela. Não precisa mudar nada, apenas manter o padrão e prosseguir.

![Figura 12. Definindo informações da classe principal]()

Em *Translation* não precisa modificar nada, pois não trabalharemos inicialmente com nenhum software que possua línguas diferentes.

![Figura 13. Definindo traduções para o software]()

Em *Kits*, selecionaremos o kit relacionado ao Desktop, já que inicialmente estaremos apenas trabalhando com aplicações desktop. Se estiver no Windows, recomendo a utilização do kit com MINGW.

![Figura 14. Escolhendo Kit Desktop]()

Depois disso, em *Summary*, caso não vá utilizar controle de versão (git) no projeto, basta finalizar.

![Figura 15. Finalizando Projeto]()

### 3.3 Executando projeto

A tela que abrirá será parecida com a da imagem abaixo. Tudo que precisa fazer para validar a instalação, é clicar em **1** e esperar o processo de build. Depois que a build do projeto estiver completa, basta clicar em **2** e executar o projeto, que deverá mostrar uma janela igual a **3**.

![Figura 15. Execução do Projeto]()

## 4. Adicionando bibliotecas extras / Qt maitenance Tool

Com tudo instalado, note que agora você também possui um programa chamado *Qt Maitenance Tool* instalado junto com o Qt Creator. Ele é responsável por fazer os updates do que você tem instalado, mas também pode remover componentes, adicionar outros ou até desinstalar tudo. Abrindo ele, basta fazer o login, assim como na instalação e chegará na página a seguir:

![Figura 16. Abrindo página de adição de componentes]()

Clique em adicionar componentes, pois é o que faremos a seguir. Após aguardar o carregamento, basta deixar selecionado apenas a opção *LTS (Long Term Support* e clicar em *Filter*, para filtrar apenas os produtos LTS, que são os que usaremos. Todas as versões LTS do Qt aparecerão, como pode ser visto na imagem a seguir:

![Figura 17. Filtrando versão LTS dos componentes]()

Como trabalharemos apenas com o Qt 6, então podemos abrir a aba *Qt 6.2.x*, dependendo de quando você ver esse guia, depois será possível ver todos os componentes dessa versão que já temos instalado, que são basicamente 2: o compilador, que no caso do Linux é o Desktop gcc e o componente Android. Para finalizar o propósito da instalação, basta abrir a sub aba chamada *Additional Libraries* para instalar as bibliotecas que utilizaremos em projetos futuros. Caso queira saber mais sobre elas, basta assistir o vídeo mencionado no início do guia.

![Figura 18. Bibliotecas adicionais que recomendo instalar]()

As bibliotecas selecionadas estão listadas abaixo:

- Qt Charts (adicionar referência)
- Qt Connectivity (adicionar referência)
- Qt Multimedia (adicionar referência)
- Qt Positioning (adicionar referência)
- Qt Serial Port (adicionar referência)
- Qt WebSockets (adicionar referência)
- Qt Webview (adicionar referência)

Com isso, resta apenas avançar no diálogo de instalação, esperar o download, instalação depois finalizar. Com isso, poderemos utilizar todas essas bibliotecas nos projetos em Qt e partimos para a criação dos projetos!