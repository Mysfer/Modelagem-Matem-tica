## come�a o programa limpando as variaveis
clear

## Quantidade de classes
n = input("Digite a quantidade de classes: ");

## Valores de g
g = [];
for i = 1:(n-1)
  fprintf("Digite o valor de g%d: ",i);
  aux = input("");
  g = [g; aux];
endfor

## Inversos de g, usado para facilitar nas contas
invg = [];

for i = 1:(n-1)
  invg = [invg; 1/g(i,1)];
endfor

##Variavel com rela��o dos pre�os, assumindo P2 como 1
p = [0; 1];

## Estrutura de repeti��o para realizar a rela��o de p3 at� pn
##Variavel para somatoria
sum = [];

for i = 3:n
  
  sum = 0;
  
  ## Estrutura de repi��o para fazer a somatoria do inverso dos valores de g
  for j = 1:(i-1)
    sum += invg(j,1);    
  endfor
  
  p = [p; sum/invg(1,1)];
endfor

## Estrutura para formatar a saida de dados
printf("A propor��o � de: 0");
for i = 2:n
  printf(":%f", p(i,1));
endfor

printf("\n");
disp(p);

 bar(p);
 title("Rela��o entre pre�os");
 xlabel("Classe");

 

