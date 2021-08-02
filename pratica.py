from collections import Counter

def analisa_frequencia_de_letras(texto):
    contador_texto = Counter(texto.lower())
    total_letras = sum(contador_texto.values())

    proporcoes = [(letra, frequencia / total_letras) for letra, frequencia in contador_texto.items()]
    proporcoes = Counter(dict(proporcoes))

    for letra, proporcao in proporcoes.most_common(10):
        print(f'{letra}: {round(proporcao * 100, 2)} %')

    print()

texto1 = """O mês de julho começou com uma novidade que 
assustou criadores de conteúdo, social medias e empresários que
 usam o Instagram para divulgar os seus produtos e serviços. 
 O diretor da plataforma, Adam Mosseri, divulgou uma série de atualizações e o novo rumo 
 que o Instagram deve seguir no futuro breve.

Mosseri trouxe, em um vídeo publicado em sua própria conta, que entre 
as mudanças da plataforma consta a priorização da entrega de
 conteúdos em vídeo, e segundo o próprio diretor, o Instagram não é mais apenas 
 uma app de compartilhamento de fotos, e sim de entretenimento."""

texto2 = """Geralmente, utilizamos componentes aninhados para compor as partes da 
nossa aplicação. É uma prática comum e super encorajada. Porém, em alguns casos, queremos 
]que alguns componentes estejam agrupados logicamente, 
mas que sejam renderizados em outro lugar do DOM. Como, por exemplo, uma modal 
que cubra toda a tela (normalmente com aquele fundo preto opaco tradicional).

É exatamente isso que o Teleport nos oferece de forma extremamente simples 
(repare que o nome mudou, ele era chamado de Portal nas primeiras versões). Basta 
envolver o trecho html que queremos teleportar num componente chamado, pasme, <teleport>.
 Esse mesmo componente espera uma prop chamada to, que é o destino do teleport."""

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)
# counter_texto1 = Counter(texto1.lower())
# counter_texto2 = Counter(texto2.lower())
#
# total_caracteres1 = sum(counter_texto1.values())
# total_caracteres2 = sum(counter_texto2.values())
# print(counter_texto1)
# print(sum(counter_texto1.values()))
#
# proporcoes = [(letra, frequencia / total_caracteres1) for letra, frequencia in counter_texto1.items()]
# proporcoes = Counter(dict(proporcoes))
# dez_mais_comuns = proporcoes.most_common(10)
# print(proporcoes)
# print(dez_mais_comuns)
