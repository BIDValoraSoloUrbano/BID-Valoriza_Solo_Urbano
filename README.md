### MODELOS DE VALORIZAÇÃO DA INTERVENÇÃO PÚBLICA A NÍVEL MUNICIPAL

---

O modelo desenvolvido prediz a valorização continua de terrenos próximos a uma obra pública a partir de amostras de preços de mercado. 

Para o desenvolvimento foram utilizados dados dos observatórios de mercado imobiliário levantados antes e depois da obra, utilizando dados próximos e até o limite da evidencia de sua influência.
Depois de realizar o tratamento dos dados brutos, procedeu-se o cálculo do semivariograma e as superfícies de variação para cada época, representando-as em formato RASTER. 

A partir dos dois mapas, determinou-se o “mapas das diferenças”, identificando-se os píxeis com alteração no valor. Foram estabelecidas faixas de valores em função da distância dos imóveis até a obra e estes valores foram introduzidos no plugin para permitir que outros municípios tenham condições de efetuar ou prever a valorização dos imóveis em torno de uma obra similar.

### Guía de usuário

---

1) Para os cálculos, deverão estar na pasta, os dados referentes a MALHA_URBANA, OBRA_PAVIM_LINHA e o arquivo LOTES.QML (que define automaticamente as cores do temático);

2) Quando o arquivo de MALHA_URBANA contiver muitos lotes, acima de 30.000, recomenda selecionar os lotes próximos a obra, cuidando
	 para a seleção exceder os 300m, afim de diminuir a massa de dados a processar e salvar a seleção como LOTES.SHP;

> #### IMPORTANTE: Os arquivos deverão ter o mesmo Sistema de Referencia Cartográfica - SRC.

Após a copia dos arquivos para os devidos locais, carregar o QGIS e abrir o projeto CALCULO_VALORIZA_SOLO.qgs contido na pasta  c:\BID_Valoriza_Solo_Urbano. Serão mostrados os arquivos conforme figura abaixo. Seguir os próximos passos.

![SLIDE_101](https://user-images.githubusercontent.com/60671104/74444983-69f36680-4e54-11ea-920c-1e256ccce5f6.png)

Ao salvar o arquivo de MALHA_URBANA como LOTES, as cores do temático serão definidas, conforme figura abaixo. 

![SLIDE_201](https://user-images.githubusercontent.com/60671104/74446463-afb12e80-4e56-11ea-9b2f-1461cdf89657.png)

Para o cálculo, chamar o plugin:

![SLIDE_301](https://user-images.githubusercontent.com/60671104/74447992-f738ba00-4e58-11ea-83e4-9ce4f540c8ea.png)

a) Selecionar o tipo de OBRA ( como ainda tem-se somente um tipo de obra valorada, então já estará selecionada).

b) Selecionar o arquivo da OBRA.

c) Selecionar o arquivo de LOTES.

d) Dar OK (aguardar resultado do cálculo).

#### Primeiro Resultado - Resumo dos totais envolvidos: 

> - número de lotes, área dos lotes, incremento na valorização e de tributo para uma alíquota de 2%.

![SLIDE_401](https://user-images.githubusercontent.com/60671104/74448430-b55c4380-4e59-11ea-9cf9-0c0919eb0586.png)

#### Segundo Resultado - Mapa temático com os intervalos de valores. 

![SLIDE_501](https://user-images.githubusercontent.com/60671104/74449594-89da5880-4e5b-11ea-8ee2-cdfbf84828cf.png)

#### Terceiro Resultado - Tabela com campos e dados calculados. 

![SLIDE_601](https://user-images.githubusercontent.com/60671104/74449985-26045f80-4e5c-11ea-86eb-7069dd5cd3c3.png)

> Campos:

> - INDFISC : Índice Fiscal do lote.

> Serão gerados:

> - AREA : Área do lote.

> - DISTOBRA : distancia do lote até a obra.

> - VALOR : valor da faixa.

> - VALTOT : incremento do valor do lote após a materialização da obra (a ser acrescido ao valor cadastral).

#### Nota dos autores:

O usuário poderá efetuar a simulação de valorização do solo urbano em qualquer malha de lotes, para tanto basta inserir sua malha neste mesmo projeto e salva-la como LOTES, conforme descrito no manual. Editar a linha do local da obra, no arquivo OBRA_PAVIM_LINHA, para sua área de interesse e executar o plugin.

> Lembrete: Ficar atento a recomendação de numero 2 do Guia do Usuário.

### Guía de instalação

---

O roteiro contendo informações com relação ao ambiente e software necessário para a utilização do plugin desenvolvido tambem encontra-se descrito (em SLIDE) no arquivo MANUAL_BID_VALORIZA.PDF. 
[Manual:aqui](https://github.com/JOAODESTRO1484/BID-Valoriza_Solo_Urbano/blob/master/MANUAL_BID_VALORIZA.pdf)

i) Baixar o arquivo “BID_VALORIZA_DADOS.rar” para o HD:

ii) Extrair a pasta “BID_Valoriza_Solo_Urbano” para o HD;

iii) Extrair a pasta “ValorizaSoloUrbano” para o HD na pasta destino c:\usuarios\<nome>\.qgis2\python\plugins”. Em algumas maquinas a pasta destino dos plugins poderá ser diferente.

iiii) Carregar o QGIS e ativar o plugin “_Valoriza Solo Urbano”, conforme figura.

![SLIDE_100](https://user-images.githubusercontent.com/60671104/74443077-58f52600-4e51-11ea-96d2-17a4815c04dd.png)

Lembrete 1: A pasta com dados para a simulação de cálculo e a pasta com plugin estão contidos no arquivo "BID_VALORIZA_DADOS.rar".


> #### IMPORTANTE : Plugin roda no QGIS versão 2.18.26.


### Instituições

---

#### Prefeitura Municipal de Aracaju, Belo Horizonte e Fortaleza.

#### Universidade Federal de Santa Catarina - Florianópolis - Brasil

### Autores

---

•	João Norberto Destro - joaodestro@gmail.com

•	Diego Alfonso Erbas - diegoerba@gmail.com

•	Everton da Silva - everton.silva@ufsc.br

### Licença

---
O código fonte é liberado sob uma licença GNU GPL v3. Por favor, consulte 
[LICENSE.md](https://github.com/JOAODESTRO1484/BID-Valoriza_Solo_Urbano/blob/master/LICENSE.md) para mais informações.

---

## Bom proveito!
