# Resultados tirados

## Respostas DW

### Análise Descritiva

1. Como está destribuido o stress pelos diferentes trabalhos, localizações, idade e grupos?

R: Nota-se que as pessoas com maior nível de stress são pessoas adultas entre os 29 e 50 anos. Designer parece ser o trabalho onde existe mais pessoas com um nível de stress alto. Quanto ao work location não existe uma conclusão.

2. Qual tipo de trabalho (Remoto, Hibrido e onsite) mostram maior nível de produtividade?

R: Pelo DW nota-se que o trabalho onde existem maior número de pessoas em que o nível de produtividade aumentou foi em trabalho Remoto.

3. Quais fatores especificos de regiões podem influenciar no nível de stress ?

R: A região onde existe maior número de pessoas com um nível de stress alto é no continente Africano. Isto pode ser relacionado com o alto valor de total tax rate, uma baixa média esperança de vida e o gdp mais baixo dentro das regiões.

### Análise Diagonóstico

1. Quais fatores estão mais associados a altos níveis de stress ?

Não existe relação entre as horas trabalhadas por semana e pela qualidade sono mas nota-se que pessoas com uma atividade fisíca diária, surpreendentemente tem um nível de stress alto.

2. Porque que certos trabalhos e locais de trabalho tem maior níveis de insatisfação do remote work ?

Nas pessoas que trabalham de forma remota, denota-se existem muitas pessoas insatisfeitas. Relativaente ao tipo de trabalho, não existe grande relação.

## Respostas do Tableau

-> Trabalho remoto é a onde existe maior nível de stress contrariamente com on-site

-> Pessoas entre os 30 e os 40 tendem a ter maior níveis de stress

-> Os trabalhos com maior nível de stress é em Sales, Project Management e Design

-> Pessoas que trabalham de forma remoto estão insastifeitos devido à falta de socialização

-> Tipos de empresa do tipo "Finance" e "Healthcare" é a onde existe maior número de pessoas insastisfeitias com trabalho remoto

-> Ásia e Africa tem o maior número de pessoas com high stress level. Oceania e Europa é a onde existe o maior número de pessoas com low stress level.

-> Regiões foi o que disse anteriormente na pergunta 3 da análise descritiva

-> Maior stress level tem tendencia a menor produtividade, especialmente em remote

-> Pessoas com low stress level maior é a sua produtividade

## Respostas do Data Mining

Criámos esta tabela tendo em conta o clustering obtido:

| Cluster    | Employee Satisfaction          | Productivity   | Stress Levels | Sleep Quality      | Work Hours per Week | Work Experience (Years) | Work-life Balance | Isolation   | Virtual Meetings | Issues                                |
|------------|--------------------------------|----------------|---------------|--------------------|----------------------|-------------------------|-------------------|-------------|------------------|---------------------------------------|
| Cluster 0  | High satisfaction             | Increased      | High          | Poor               | 45 hours (highest)  | 11 years (lowest)       | High              | Lowest      | 5 meets          | Anxiety due to high stress and poor sleep |
| Cluster 1  | Highest satisfaction          | Decreased      | Medium        | Good               | 38 hours            | 19 years                | Lowest rating     | Highest     | 7 meets          | Burnout                               |
| Cluster 2  | Lowest satisfaction           | Highest decrease | High        | Average to poor    | 34 hours            | 23 years (Highest)      | Highest           | Low         | 10 meets (Highest) | Depression and anxiety               |
