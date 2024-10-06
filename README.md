Este port scanning funciona do seguinte modo, voce deve ir na pasta onde instalou o arquivo ponto py, por exemplo:

$cd Downloads

dentro da pasta voce roda o programa da seguinte maneira:

$python3 escanearPortas.py [ip do alvo] [porta de inicio] [porta do final]

A porta de inicio e porta de final servem como um filtro, existem 65535 portas na pilha TCP/IP, assim voce pode escolher por qual porta o programa inicia a varredura e ate onde ela vai

a resposta pode ser duas, ou a porta esta aberta ou esta fechada, alem de motsrar o servico que etsa rodando em cada uma, caso o programa nao saiba o servico ele sera colocado como desconhecido
