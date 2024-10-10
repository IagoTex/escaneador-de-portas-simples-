Este port scanner funciona do seguinte modo, você deve ir na pasta onde instalou o arquivo ponto py, por exemplo:

$cd Downloads

dentro da pasta voce roda o programa da seguinte maneira:

$python3 escanearPortas.py [ip do alvo] [porta inicial] [porta final]

porta inicial é a porta por onde você irá começar a varredura
porta final é a porta onde irá acabar a varredura

O programa pode retornar:

[+]Aberta - para portas que estão abertas
[-]Fechada - para portas que estão fechadas

O programa fala os serviços que estão rodando naquela porta, esta função é feita pela biblioteca, os serviços que ela não identifica é colocado como Desconhecido, porém basta pesquisar no google o número da porta para saber o possível serviço rodando na mesma
