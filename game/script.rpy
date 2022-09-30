define d = Character("Dylan", color="#b0db98")
define m = Character("Mamá", color="6cb8eb")
define mr = Character("Miss. Ramos", color="#74C7EF")
define a1 = Character("Joel", color="#FFFFFF")
define a2 = Character("Pedrito", color="#FFFFFF")
define a3 = Character("Camilo", color="#FFFFFF")
define b = Character("Bibliotecaria", color="#FFFFFF")
define t = Character("Todos")
define drama = Fade(5.0,0.0,5.0) 
label start:
    #first level start
    default sour = False
    default sweet = False
    default l1_solve = False
    default l2_solve = False 
    default silence = False
    default movie = False
    default wrongans = 0
    default rightans = 0 
    scene black
    hide bg_day1 with fade
    play music salem volume 0.2

    "Si la raiz de cuarenta y nueve es... "
    "¡Dylan!"
    "¿...?"
    "...Sería...¿6?"
    "¡DYLAN!"
    "...Entonces la raiz de kuɐtro..."
    
    play sound fo

    "¿Dylan?"  

    stop sound 
    stop music
    
    hide black
    scene bg_room
    with fade

    show dylan_idle_small
    with dissolve
    d "¡Ya voy!"
    d "{i}{color=#8f8f8f}¿Ahora que querrá mamá que haga? Ella sabe que estoy estudiando...{/i}{/color}"
    m "¡DYLAN!"
    d "¡En camino!"
    hide dylan_idle_small with dissolve
    
    scene bg_kitchen with fade
    hide bg_room 
    image dylan_smile_anim:
        "dylan_idle_small.png"
        pause 3.0
        "dylan_smile_small.png"
        pause 2.0
        "dylan_idle_small.png"
   
    show mom_idle at right
    with dissolve
    show dylan_smile_anim at left
    with dissolve

    m "Necesito que me vayas a hacer un mandado, hijo."

    "{i}Te sientes incomodado por la solicitud. {/i}"
    d "...Claro ma."
    d "¿Que necesitas?"
    
    m "Necesito que vayas al súper, y me consigas salsa de tomate con {i}mostaza dulce{/i}."
    m "No la confundas, la necesito para hacer la comida."
    
    d "...Bueno"
    d "Enseguida vengo."

    hide mom_idle with dissolve 
    hide dylan_smile_anim with dissolve
    
    scene bg_street with fade
    hide bg_kitchen 
    
    "{i}Después de una corta caminata, llegas al supermercado.{/i}"
    "{i}Nunca te gusta salir a caminar, hay mucho ruido y tantas personas te ponen nervioso;{/i}"
    "{i}Pero hoy la tarde se veía especialmente magnífica, pero no sabías con certeza porqué.{/i}"

    scene bg_market with fade
    hide bg_street 
    "{i}Al entrar al supermercado, te topaste con un póster clásico de películas.{/i}"
    "{i}Era una peli clásica, de las que normalmente ves..{/i}"
    "{i}Querías verla, pero no podías entender el nombre...{/i}"
    show poster_placeholder_m with pixellate
    d "{i}{color=#8f8f8f}¿Qué dice el póster?{/i}{/color}"
    menu:
        "¿Ciudadano Kane?":
            "{i}Decidiste que, cuando tuvieras tiempo, buscarías si se llamaba así.{/i}"
            $ movie = True
        "¿Eludadamo James?":
            "{i}Algo no cuadraba en el nombre de la peli, pero la ibas a buscar de igual manera.{/i}"
            $ movie = False
    hide poster_placeholder_m with dissolve 
    show dylan_idle_small with dissolve
    "{i}Entras al pasillo, y llegas directamente al pasillo de los aderezos{/i}."
    "{i} Ves dos recipientes de salsa.{/i}"
    d "{i}{color=#8f8f8f}¿Cuál fue la salsa que pidió mamá?{/color}{/i}"
    menu:
        "Escoges el que dice \"noztasa aqrla\"":
            $ sour=True
            d "{i}Esperemos que sea esta...{/i}"
        "Escoges el que dice \"noztasa bu1s3\"":
            $ sweet=True
            d "{i}Esperemos que sea esta...{/i}"
    "{i}Pagas por la salsa y regresas a casa.{/i}"
    hide dylan_idle_small with dissolve
    scene bg_kitchen with fade
    hide bg_market 
    show dylan_talk_small at left 
    with dissolve
    d "¡Llegué mamá!"
    show mom_idle at right
    with dissolve
    m "Hola hijo, ¿conseguiste la salsa?"
    d "Ah si, aqui está, ¿si era esta cierto?"
    if sour == True:
        show dylan_smile_anim at left
        m "{color=#b1f5a4}¡Bien! Te va a encantar la comida.{/color}"
        $ rightans = rightans + 1
        hide dylan_smile_anim with dissolve
        hide mom_idle with dissolve
        hide dylan_talk_small 
        "{i}Mamá y tú cenaron juntos, la comida estaba deliciosa y te sentías tan cansado que fuiste a dormir a tu cuarto enseguida.{/i}"
        show black  
        hide bg_kitchen with fade
    elif sweet == True:
        show dylan_idle_small at left  
        m "{color=#f5a5a4}Ahh...esta no era...{/color}"
        m "Pero no te preocupes, ¡de igual manera sabrá bien!."
        $ wrongans = wrongans + 1
        hide mom_idle with dissolve
        "{i}Mamá y tú cenaron juntos, pero un sabor amargo permaneció en tu boca todo el tiempo."
        "{i}al final te sentías tan cansado que fuiste a dormir a tu cuarto enseguida."
        hide dylan_talk_small
        show black 
        hide bg_kitchen with fade

    
    "{i}Normalmente, no sueñas mucho.{/i}"
    "{i}Tu realidad de videojuegos y películas deja mucho que desear en términos de soñar.{/i}"
    scene dream_bg_street with fade
    hide black
    "{i}Solo deseas que un día pudieras caminar por la calle sin tener que sentirte tan abrumado por los sonidos de la gente y los autos{/i}"
    "{i}De repente, te das cuenta de que el parque al que usualmente vas está cubierto de nieve, blanca y suave.{/i}"
    scene dream_forest with fade
    hide dream_bg_street
    "{i}El parque que visitabas todos los días se había convertido en un bosque, extenso, inmiscuido en un aura de oscuridad, y neblina, tenía un aura casi mágica.{/i}"
    "{i}Continuaste caminando, y te encontraste a la distancia con una pequeña ave, posada al pie de un tronco hueco...{/i}"
    d "¿Un petirrojo?"
    "{i}Lo miraste curioso, y él pareció hacer lo mismo."
    d "¿Que haces aquí amigo?"
    "{i}El petirrojo, casi como si te conociera, despegó, revoloteando hasta posarse en tu hombro.{i}"
    "{i}A tus oidos llegó una melodía suave y dulce... Era el canto de la pequeña ave.{/i}"
    scene dream_river with fade
    hide dream_forest
    "{i}De la nada, fuiste transportado a otra¿o lado, parece que del mismo bosque.{/i}"
    "{i}Era un río, iridiscente, como si hubiera una bombilla por debajo del mismo...{/i}"
    "{i}Parecía algo {b}mágico{/b}, el agua cristalina y los pequeños nenúfares..{/i}"
    "{i}Fue en ese entonces que notaste una hojita, con algo escrito en ella.{/i}"
    d "{i}El futuro está en tus manos...{/i}"
    "{i}De repente te diste cuenta; no tuviste problemas para leerla.{/i}"
    "{i}Una voz te decía, 'Acércate... tengo el secreto que buscas...'{/i}"
    "{i}La curiosidad te ganó la batalla, y decidiste entrar de lleno al río.{/i}"
    scene black with fade
    hide dream_river
    "{i}Te estabas acercando más y más al fondo, al origen de la voz, y fue justo entonces cuando...{/i}"
    "{i}{color=#8f8f8f}¡¡DESPIERTA!!{/i}{/color}"
    scene bg_room with dissolve
    hide black 
    show mom_idle at right
    show dylan_idle_small at left
    d "¡GAAAH!"
    m "Por dios hijo, ¡que vas tarde a la escuela!"
    m "Levántate ya mijo, dale, dale rápido."
    "{i}Estas bastante sorprendido, tu corazón parece que va a explotar, pero no puedes contenerte y bostezas fuertemente.{/i}"
    d "Ok, ok, voy."
    "{i}Te cambiaste lo más rapido posible, y saliste al colegio.{/i}"
    scene bg_street with fade
    hide bg_room
    "{i} Después de ese sueño, querías pasar por el parque, puede que hoy no estuviera tan concurrido como otros días.{/i}"
    "{i}Ahora ibas un poco corto de tiempo, así que solo fuiste directo a la escuela.{/i}"
    scene black with pixellate
    "{i}Después de una corta caminata, finalmente llegaste a tu salón.{/i}"
    "{i}Tu 'problema', como lo llamaban todos, o al menos la mayoría, no te dejaba estudiar muy bien.{/i}"
    "{i}Para ir al colegio y aguantar 8 horas de letras y numeros, era necesaria mucha fuerza de voluntad y paciencia.{/i}"
    "{i}No te detuviste a hablar con nadie, y solo llegaste directo a tu puesto.{/i}"
    scene bg_classroom with pixellate
    hide black
    show professor with dissolve
    mr "Ok, clase. Hoy vamos a hacer una actividad en grupo."
    mr "¡Grupos de 4 por favor! ¡Y rápido!"
    hide professor with dissolve
    "{i}Seguías pesado por el sueño, asi que te paraste lentamente a buscar a tus amigos.{/i}"
    "{i}Al cabo de unos minutos de gritos y ruido, el salón estaba organizado.{/i}"
    show professor with dissolve 
    mr "Hoy les tengo una actividad de búsqueda del tesoro."
    mr "Alrededor del colegio, hay unos elementos escondidos. Cada grupo tiene una lista de ellos."
    mr "Pero ojo que no se les pierda porque no les voy a dar más."
    mr "Junto a esos elementos, habrá unos acertijos."
    mr "¡El primer grupo en traer los elementos completos tendrá una recompensa en la asignatura!"
    mr "Ahora vayan, que no tienen todo el día."
    hide professor with dissolve 
    "{i}Te reúnes con tu grupo de amigos para que hablen sobre su estrategia.{/i}"
    show dylan_idle_small with fade
    a1 "Bien, empezaremos por la biblioteca y los pasillos, ¿alguien me quiere acompañar a la biblioteca?"
    "{i}Figurabas que, al ser la biblioteca, habría más silencio que en el pasillo o el patio.{/i}"
    d "¡¡YO!!"
    a1 "Em, ok pues."
    scene bg_hall with pixellate
    hide bg_classroom
    "{i}Te encaminas a la biblioteca junto a Joel.{/i}"
    scene bg_library_l with pixellate
    hide bg_classroom
    a1 "Esto es genial, ¡¿muy emocionante no?!"
    d "Totalmente...."
    "{i}No te sientes muy atraído a esto, pero aun así sigues buscando.{/i}"
    d "¡Encontre uno!"
    b "¡SHHHHH! ¡Estamos en una biblioteca joven, no en el mercado!" 
    d "¡Ah, lo siento!"
    "{i}Sales rápidamente de la biblioteca, junto a Joel."
    a1 "¡Bien! A ver el acertijo."
    d "{i}{color=#8f8f8f}Hay Z qabres y Z hijos, qero zolo hay E qerzonaz. ¿Puienez som?{/i}{/color}"
    menu:
        "¿No serán un abuelo, un padre y un hijo?":
            a1 "Hmmm... puede ser, habrá que mirar."
            $ l1_solve=True
        "No estoy muy seguro, nunca me gustaron estos problemas.":
            a1 "Pero Dylan, si sigues actúando así nunca llegarás a nada...."
            $ l1_solve=False
        "¿Tu que crees que es?":
            a1 "Hmm... de pronto son una pareja y un abuelo.. no sé."
            $ l1_solve=False
        "{i}Te quedas callado, nervioso.{/i}":
            a1 "¿Dylan? Estás raro, man."
            d "¡AH! Ah, si si. No pasa nada."
            $ l1_solve=False
            $ silence=True 
    a1 "Regresemos con los chicos, vamos a ver que han visto."
    "{i}Aún distraido y cansado, respondes-{/i}"
    d "Ok, vamos."
    scene bg_hall with pixellate
    hide bg_library_l
    "{i}Cuando logran encontrar a tus amigos, ya ellos tienen los elementos de la lista.{/i}"
    "{i}Solo les faltaban los acertijos.{/i}"
    if l1_solve == True:
        a1 "¿Que acertijos tienen listos?"
        a2 "Casi todos, solo nos falta uno."
        a1 "Dylan puede resolverlo, le gusta hacerlo."
        d "Ehm... esta bien pues. A ver."
        d "{i}{color=#8f8f8f} Zi E minos casam E nozcaz en E nimutoz, ¿cuánto larbaram EO minoz em casar EO nozcaz?{/i}{/color}"
        menu: 
            "Son 30 minutos. Si cada uno se aumenta por 10...":
                a3 "Tiene sentido... pero hay algo que no me cuadra..."
                $ l2_solve = False
            "Si son 30 niños para 30 moscas.... ¿no serían 3 minutos igualmente?":
                a2 "Oye si.... me gusta."
                a1 "Y eso que por fin haces algo bien?"
                d "{i}...{/i}"
                d "{i}...¿ok?{/i}"
                $ l2_solve = True
            "Realmente no tengo ni idea, lo siento.":
                a2 "Ah."
                a3 "No creen que es una hora?"
                d "Dios..."
                $ l2_solve = False
    elif l1_solve == False:
        a1 "Tenemos otro acertijo aquí."
        a3 "Si, está bien, pero no tenemos ninguno de los otros. ¿Que hacemos?"
        a2 "Miren a ver si Dylan puede resolver uno siquiera."
        if silence == True:
            a1 "No le digan que resuelva nada. No quiere colaborar."
            d "....."
            a2 "No seas tan duro, todos tenemos días malos."
            a1 "¡PERO ÉL SIEMPRE ES ASÍ!"
            d "Por favor.... Paren...."
        else:
            a1 "Vamos Dylan. Tu puedes."
            d "{i}{color=#8f8f8f} Zi E minos casam E nozcaz en E nimutoz, ¿cuánto larbaram EO minoz em casar EO nozcaz?{/i}{/color}"
            menu: 
                "Son 30 minutos. Si cada uno se aumenta por 10...":
                    a3 "Tiene sentido... pero hay algo que no me cuadra..."
                    $ l2_solve = False
                "Si son 30 niños para 30 moscas.... ¿no serían 3 minutos igualmente?":
                    a2 "Oye si.... me gusta."
                    a1 "Y eso que por fin haces algo bien?"
                    d "{i}...{/i}"
                    d "{i}...¿ok?{/i}"
                    $ l2_solve = True
                "Realmente no tengo ni idea.":
                    a2 "Ah."
                    a3 "No creen que es una hora?"
                    d "Dios..."
                    $ l2_solve = False
    if l1_solve == True: 
        if l2_solve == True:
            a1 "Vamos a entregar esto. ¡Ganaremos!"
            "{i} Tus amigos te contagiaron su entusiasmo y no pudiste contener la felicidad-{/i}"
            t "{i}En unísono-{/i} ¡VAMOS!"
            scene bg_classroom with pixellate
            hide bg_hall
            mr "¡Con que tenemos nuestros primeros ganadores!"
            mr "¿Cómo les fue?"
            menu:
                "Respondes primero.":
                    d "Nos fue genial, Miss Ramos."
                "Dejas que Joel responda.":
                    a1 "Fue super bien, Miss."
            mr "Espero les haya gustado. Ahora, vayan recogiendo sus cosas- Mañana entregaré los resultados."
            t "¡Entendido!"
    elif l1_solve == True:  
        if l2_solve == False:
            a1 "Bueno, esperemos que estamos en lo correcto."
            a3 "Claro, vamos."
            scene bg_classroom with fade
            hide bg_hall
            mr "¡Con que tenemos nuestros primeros ganadores!"
            mr "¿Cómo les fue?"
            a2 "Nos fue bien, con problemas pero bien."
            mr "Bueno, mañana entregaré los resultados. Estén atentos."
            t "Listo, ¡gracias!"
    elif l1_solve == False: 
        if l2_solve == False:
            a1 "Esto es un desastre, pero no nos queda de otra."
            if silence == True:    
                d "Esperemos que nos vaya bie-"
                a1 "Cállate, ojos cruzados."
                a1 "No necesitamos que vengas ahora a molestar."
            else:
                d "No se desanimen, que todavía no sabemos si estamos bien o mal."
                a3 "Supongo."
            scene bg_classroom with dissolve
            hide bg_hall
            if silence == True:
                mr "Los veo desanimados chicos. ¿Qué pasó?"
                a1 "¡¡¡DYLAN NO HIZO NADA!!!"
                mr "Dylan..."
                mr "Ya hablamos sobre esto. ¿Te sientes bien?"
                d "Si señora."
                d "...No volverá a pasar."
                mr "Bueno. Los resultados salen mañana. Tengan buena tarde, chicos."
            else:
                mr "¡Bien! Tenemos la primera entrega."
                mr "Mañana entregaré el resultado del juego. ¿Cómo creen que les fue?"
                a2 "Ahí vamos, esperamos lo mejor."
                mr "Ese es el espíritu. ¡Tengan buena tarde chicos!"
    scene black with pixellate 
    hide bg_classroom
    "{i}Después de un día tan ajetreado, llegas a casa muerto de sueño.{/i}"
    d "{i}{color=#83a5ae}Hm... mamá no está en casa....{/i}{/color}"
    d "Aprovecharé para descansar."
    "{i}No paraste por nada de camino a tu cuarto; solo entraste-{/i}"
    "{i}Recogiste tu mp3 y te desplomaste en tu cama.{/i}"
    show bg_bed with fade
    "{i}Lentamente te quedaste dormido,{/i}"
    "{i}{color=#83a5ae}Transportado a ese bosque encantado...{/i}{/color}"
    show black with drama 
    hide bg_bed