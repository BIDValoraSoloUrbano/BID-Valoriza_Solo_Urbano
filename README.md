## Modelo de Valorização da Intervenção Pública a Nível Municipal

---

O [modelo desenvolvido](https://user-images.githubusercontent.com/60671104/74605560-03ff1d00-50a8-11ea-91dd-e32921332822.png)
 prediz a valorização continua de terrenos próximos a uma obra pública a partir de amostras de preços de mercado. 

Para o desenvolvimento foram utilizados dados dos observatórios de mercado imobiliário levantados [antes e depois](https://user-images.githubusercontent.com/60671104/74605557-019cc300-50a8-11ea-9187-296c13e45b3f.png) da obra, utilizando dados próximos e até o limite da evidencia de sua influência.
Depois de realizar o tratamento dos dados brutos, procedeu-se o cálculo do [semivariograma](https://user-images.githubusercontent.com/60671104/74606810-239b4300-50b2-11ea-86e5-b81dcd58573a.png)
 e as [superfícies](https://user-images.githubusercontent.com/60671104/74606715-88a26900-50b1-11ea-8982-e557c920f08d.png)
 de variação para cada época, representando-as em formato RASTER. 

A partir dos dois mapas, determinou-se o [“mapas das diferenças”](https://user-images.githubusercontent.com/60671104/74605558-02355980-50a8-11ea-8945-6f5cad648637.png), identificando-se os píxeis com alteração no valor e transferindo-o para os [centróides dos lotes](https://user-images.githubusercontent.com/60671104/74605561-0497b380-50a8-11ea-836c-06944b3f6afb.png)
. Foram estabelecidas [faixas de valores](https://user-images.githubusercontent.com/60671104/74605559-02cdf000-50a8-11ea-9b32-958869719785.png)
 em função da distância dos imóveis até a obra e estes valores foram introduzidos no código do [plugin](https://user-images.githubusercontent.com/60671104/74605562-0497b380-50a8-11ea-9ede-fb74850e713e.png) para permitir que outros municípios tenham condições de efetuar ou prever a [valorização](https://user-images.githubusercontent.com/60671104/74605563-05304a00-50a8-11ea-8353-6d56edf7cc20.PNG) dos imóveis em torno de uma obra similar. 
 
Obra utilizada como base de cálculo na qual foi executada a pavimentação do trecho da [Avenida José Jatahy](https://user-images.githubusercontent.com/60671104/74606993-be485180-50b3-11ea-91c6-1796521ca7be.png), Municipio de Fortaleza, Ceará.

### Guía de usuário

---

1) Para os cálculos, deverão estar na pasta, os dados referentes a MALHA_URBANA, OBRA_PAVIM_LINHA e o arquivo LOTES.QML (que define automaticamente as cores do temático);

2) Quando o arquivo de MALHA_URBANA.SHP contiver muitos lotes, acima de 30.000, recomenda selecionar os lotes próximos a obra, cuidando
 para a seleção exceder os 300m, afim de diminuir a massa de dados a processar, salvar a seleção como LOTES.SHP;

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

O roteiro contendo informações com relação ao ambiente e software necessário para a utilização do plugin desenvolvido tambem encontra-se descrito (em SLIDE) no arquivo [MANUAL_BID_VALORIZA.PDF](https://github.com/BIDValoraSoloUrbano/BID-Valoriza_Solo_Urbano/blob/master/MANUAL_BID_VALORIZA.pdf).

i) Baixar o arquivo [“BID_VALORIZA_DADOS.rar”](https://github.com/BIDValoraSoloUrbano/BID-Valoriza_Solo_Urbano/blob/master/BID_VALORIZA_DADOS.rar) para o HD:

ii) Extrair a pasta “BID_Valoriza_Solo_Urbano” para o HD;

iii) Extrair a pasta “ValorizaSoloUrbano” para o HD na pasta destino c:\usuarios\<nome>\.qgis2\python\plugins”. Em algumas maquinas a pasta destino dos plugins poderá ser diferente.

iiii) Carregar o QGIS e ativar o plugin “_Valoriza Solo Urbano”, conforme figura.

![SLIDE_100](https://user-images.githubusercontent.com/60671104/74443077-58f52600-4e51-11ea-96d2-17a4815c04dd.png)


> #### IMPORTANTE : O [Plugin](https://user-images.githubusercontent.com/60671104/74605555-006b9600-50a8-11ea-85a9-a51eddcd9ac0.png) roda no QGIS versão 2.18.26.


Lembrete: A pasta denominada "BID_Valoriza_Solo_Urbano" com dados para a simulação de cálculo estão no arquivo "BID_VALORIZA_DADOS.rar", a pasta do plugin denominada "ValorizaSoloUrbano" tambem está disponivel neste arquivo.



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
[LICENSE.md](https://github.com/BIDValoraSoloUrbano/BID-Valoriza_Solo_Urbano/blob/master/LICENSE.md) para mais informações.

---

## Bom proveito!
