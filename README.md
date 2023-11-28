
# Fome Zero! :fork_and_knife:

<p align="left">
  <img src="img/fome_zero.png" title="Fome Zero!">
</p>

# 1. Problema de negócio
    
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações. 
  
O projeto consiste em responder algumas perguntas do CEO da empresa disponibilizando um dashboard para que ele possa acompanhar os principais indicadores da empresa.
  
Geral
  
  1. Quantos restaurantes únicos estão registrados?
  2. Quantos países únicos estão registrados?
  3. Quantas cidades únicas estão registradas?
  4. Qual o total de avaliações feitas?
  5. Qual o total de tipos de culinária registrados?
  
País
  
  1. Qual o nome do país que possui mais cidades registradas?
  2. Qual o nome do país que possui mais restaurantes registrados?
  3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
  4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
  5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
  6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
  7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
  8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
  9. Qual o nome do país que possui, na média, a maior nota média registrada?
  10. Qual o nome do país que possui, na média, a menor nota média registrada?
  11. Qual a média de preço de um prato para dois por país?
  
Cidade
  
  1. Qual o nome da cidade que possui mais restaurantes registrados?
  2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
  3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
  4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
  5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
  6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
  7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
  8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
  
Restaurantes
  
  1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
  2. Qual o nome do restaurante com a maior nota média?
  3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
  4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
  5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
  6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
  7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
  8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
  
Tipos de Culinária
  
  1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
  2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
  3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
  4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
  5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
  6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
  7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
  8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
  9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
  10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
  11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
  12. Qual o tipo de culinária que possui a maior nota média? 
  13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
    
# 2. Premissas do negócio
  1. Foi considerado apenas um tipo de culinária por restaurante.
  2. Foram desconsiderados os tipos de culinárias: “Drinks Only” e “Mineira”.
  3. Foram desconsideradas as linhas duplicadas e faltantes.
    
# 3. Estratégia da solução
    
  O painel foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
  
  1. Visão por país
  2. Visão por cidade
  3. Visão por tipo de culinária
  
  Cada visão é representada pelo seguinte conjunto de métricas.
  
  1. Visão por país
      1. Quantidade de restaurantes por país.
      2. Quantidade de cidades por país.
      3. Média de avaliações por país.
      4. Preço médio de um prato para 2 pessoas por país.
  2. Visão por cidade
      1. Top 10 cidades com mais restaurantes registrados.
      2. Top 10 cidades com restaurantes com média de avaliação acima de 4.
      3. Top 10 cidades com restaurantes com média de avaliação abaixo de 2.5.
      4. Top 10 cidades com mais restaurantes com tipos de culinária distintos.
  3. Visão por tipo de culinária
      1. Melhores restaurantes dos principais tipos culinários.
      2. Top 10 melhores e piores avaliações pelos tipos de culinárias.
      3. Top 10 restaurantes melhores avaliados.
        
# 4. Top 3 Insights de dados
  1. A Indonésia é o país com a maior média de avaliações feitas e o país com o preço médio mais alto para um prato para duas pessoas.
  2. Londres é a cidade que possui o maior número de restaurantes com classificação média superior à 4.
  3. Birmingham é a cidade com o maior número de tipos de culinária distintos.
    
# 5. O produto final do projeto    
  Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.  
  O painel pode ser acessado através desse link: https://fome-zero-restaurantes.streamlit.app/
    
# 6. Conclusão    
  O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam métricas da melhor forma possível para o CEO.
    
# 7. Próximo passos
  1. Considerar outros tipos de culinárias por restaurante.
  2. Criar novos filtros.
  3. Adicionar novas visões de negócio.
