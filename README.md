### MODELOS DE VALORIZAÇÃO DA INTERVENÇÃO PÚBLICA A NÍVEL MUNICIPAL

O modelo desenvolvido prediz a valorização continua de terrenos próximos a uma obra pública a partir de amostras de preços de mercado. 

Para o desenvolvimento foram utilizados dados dos observatórios de mercado imobiliário levantados antes e depois da obra, utilizando dados próximos e até o limite da evidencia de sua influência.
Depois de realizar o tratamento dos dados brutos, procedeu-se o cálculo do semivariograma e as superfícies de variação para cada época, representando-as em formato RASTER. 

A partir dos dois mapas, determinou-se o “mapas das diferenças”, identificando-se os píxeis com alteração no valor. Foram estabelecidas faixas de valores em função da distância dos imóveis até a obra e estes valores foram introduzidos no plugin para permitir que outros municípios tenham condições de efetuar ou prever a valorização dos imóveis em torno de uma obra similar.

### Guía de usuario

1) Para os cálculos, deverão estar na pasta, os dados referentes a 	MALHA_URBANA, OBRA_PAVIM_LINHA e o arquivo LOTES.QML (que 	define automaticamente as cores do temático);

2) Quando o arquivo de MALHA_URBANA contiver muitos lotes, acima de 	30.000, recomenda selecionar os lotes próximos a obra, cuidando
	 para a seleção exceder os 300m, afim de diminuir a massa de dados
 	a processar e salvar a seleção como LOTES.SHP;

#### IMPORTANTE: Os arquivos deverão ter o mesmo Sistema de Referencia 	Cartográfica - SRC.

Após a copia dos arquivos para seus devidos locais, carregar o QGIS e seguir os passos abaixo para ativar o plugin “_Valoriza Solo Urbano”.


### Guía de instalação

O roteiro contendo informações com relação ao ambiente e software necessário para a utilização do plugin desenvolvido encontra-se descrito no arquivo MANUAL_BID_VALORIZA.PDF. 
https://github.com/JOAODESTRO1484/BID-Valoriza_Solo_Urbano/blob/master/MANUAL_BID_VALORIZA.pdf

O arquivo BID_VALORIZA_DADOS.rar contem a pasta do plugin e a pasta com dados para a simulação de cálculo.

O plugin roda no QGIS versão 2.18.26.

### Instituições
Prefeitura Municipal de Aracaju, Belo Horizonte e Fortaleza.
Universidade Federal de Santa Catarina - Florianópolis - Brasil

### Autores

•	João Norberto Destro - joaodestro@gmail.com

•	Diego Alfonso Erbas - diegoerba@gmail.com

•	Everton da Silva - everton.silva@ufsc.br
