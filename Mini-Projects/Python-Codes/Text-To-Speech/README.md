# Exemplo de Texto para Fala (TTS, do inglês Text-To-Speech)

<!--
    Colocar aqui Thumbnail com link p/ o vídeo do YouTube quando tiver.
-->

> **Descrição da funcionalidade TTS:**
> O TTS é uma tecnologia que utiliza como base um texto, que pode vir de uma String ou até de um arquivo de texto, por exemplo, para transformar em fala, que pode ser executada a partir de um arquivo de áudio.

## Pré-requisitos

### Python 3.6+

> Utilizado em todos os exemplos

Esses projetos foram testados em dois ambientes diferentes, com Python 3.10.2 e Python 3.8.5. Portanto, é bom ter uma versão atualizada não só para que possamos usurfruir das novidades mas para que também tenhamos certeza de que o próprio Python não será um problema na execução dos exemplos.

Caso não tenha o Python instalado ainda, você pode baixar e seguir as instruções no próprio [site deles](SiteAqui)

### Pacote gTTS

> Utilizado em todos os exemplos

Esse pacote para Python é o responsável por realizar a "mágica" de transformar o texto para fala. É essencial que tenha ele instalado para a execução dos exemplos. Você pode encontrar as instruções [nesse site](ColocarAquiSiteDoPypi) ou simplesmente executar o comando:

`pip install gTTS`

### Pacote Pygame

> Utilizando apenas em '2_play_tts.py'

A instalação do pygamme não é obrigatória. Esse pacote é bem famoso e bastante utilizado em diversos tipos de projetos em Python, como criação de jogos e até interfaces simples. Utilizaremos ele apenas para executar os sons de falas gerados pelo exemplo do TTS. Ele possui diversos módulos internos e um deles é o Mixer, que permite que arquivos de áudio possam ser executados. Você pode encontrar mais informações [nesse site](ColocarAqui) ou simplesmente instalar com o comando:

`pip install pygame`

Caso tenha algum problema com a instalação, recomendo que olhe o [repositório oficial do projeto](ColocarRepositorioAqui), que possui mais detalhes relacionados a dependências e do que o pacote pode precisar a mais para funcionar.

## Mini Projetos

Os códigos poderão ser encontrados nesta pasta no github e possuem comentários em inglês e português, pois foram feitos para serem facilmente entendidos. Caso tenha encontrado algum problema ou tenha alguma dúvida, fique a vontade para abrir uma issue nesse repositório!

<details>
<summary>1_simple_tts.py</summary>

Esse exemplo possui o exemplo mais básico para utilizar o tts, onde você só precisa especificar apenas o texto e língua, tendo um arquivo mp3 salvo no final.

```python
    # Colocar o código aqui
```

</details>

<details>
<summary>2_play_tts.py</summary>

Esse exemplo é semelhante ao anterior, no entanto possui algumas linhas a mais, para que o áudio seja executado depois de ser gerado, para que o usuário consiga executar o programa e escutar diretamente.

```python
    # Colocar o código aqui
```

</details>

<details>
<summary>3_class_tts.py</summary>

Esse exemplo é apenas para mostrar um exemplo de código um pouco mais organizado, para que usuários iniciantes tenham uma noção de como podem organizar melhor o código para melhorar a qualidade dos seus projetos. O código necessariamente não possui nada novo, apenas reestruturado de uma forma simples e organizada.

```python
    # Colocar o código aqui
```

</details>
