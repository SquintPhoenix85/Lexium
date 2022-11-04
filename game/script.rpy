define d = Character("Dylan", color="#b0db98")
define m = Character("Mamá", color="6cb8eb")
define mr = Character("Miss. Ariza", color="#74C7EF")
define a1 = Character("Alejo", color="#FFFFFF")
define a2 = Character("Pedro", color="#FFFFFF")
define a3 = Character("Tomás", color="#FFFFFF")
define b = Character("Bibliotecaria", color="#FFFFFF")
define t = Character("Todos")
define dramain = Fade(2.5,0.0,0.0)
define dramaout = Fade(0.0,0.0,2.5) 
default sour = False
default sweet = False
default l1_solve = False
default l2_solve = False 
default silence = False
default movie = False
define suspicion = 0
default wrongans = 0
default rightans = 0 
default problem_cc = 0
default sugar = 0
default flour = 0
default butter = 0
label start:
    #first level start
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
    show mom_idle at right
    with dissolve
    show dylan_smile_small at left
    with easeinleft 

    m "Necesito que me vayas a hacer un mandado, hijo."

    hide dylan_smile_small
    show dylan_idle_small at left

    "{i}Te sientes incomodado por la solicitud. {/i}"
    d "...Claro ma."
    d "¿Que necesitas?"
    
    m "Necesito que vayas al súper, y me consigas salsa de tomate con {i}mostaza dulce{/i}."
    m "No la confundas, la necesito para hacer la comida."
    
    d "..bueno."
    d "Enseguida vengo."

    hide dylan_talk_small with dissolve
    hide mom_idle with dissolve 
    scene bg_street with fade
    hide bg_kitchen 
    "{i}Después de una corta caminata, llegas al supermercado.{/i}"
    "{i}Nunca te gusta salir a caminar, hay mucho ruido y tantas personas te ponen nervioso;{/i}"
    "{i}Pero hoy la tarde se veía especialmente magnífica, pero no sabías con certeza porqué.{/i}"
    scene bg_market with fade
    hide bg_street 
    "{i}Al entrar al supermercado, te topaste con un póster de cine en una de las paredes.{/i}"
    "{i}Parecía una peli clásica, de las que normalmente ves..{/i}"
    "{i}Querías verla, pero no podías entender el nombre...{/i}"
    show poster_placeholder_m with pixellate
    d "{i}{color=#8f8f8f}¿Qué dice el póster?{/i}{/color}"
    menu:
        "¿Ciudadano Kane?":
            "{i}Decidiste que, cuando tuvieras tiempo, buscarías si realmente se llamaba así.{/i}"
            $ movie = True
        "¿Eludadamo James?":
            "{i}Algo no cuadraba en el nombre de la peli, pero buscarías más tarde de igual manera.{/i}"
            $ movie = False
    hide poster_placeholder_m with dissolve 
    show dylan_idle_small with easeinleft
    "{i}Entras al súpermercado, y llegas directamente al pasillo de los aderezos{/i}."
    "{i}Ves dos recipientes de salsa.{/i}"
    d "{i}{color=#8f8f8f}¿Cuál fue la salsa que pidió mamá?{/color}{/i}"
    menu:
        "Escoges el que dice \"noztasa aqrla\"":
            $ sour=True
            d "{i}Esperemos que sea esta...{/i}"
        "Escoges el que dice \"noztasa bu1s3\"":
            $ sweet=True
            d "{i}Esperemos que sea esta...{/i}"
    "{i}Pagas por la salsa y regresas a casa.{/i}"
    hide dylan_idle_small with moveoutleft
    scene bg_kitchen with fade
    hide bg_market 
    show dylan_talk_small at left 
    with easeinleft
    d "¡Llegué mamá!"
    show mom_idle at right
    with easeinright
    m "Hola hijo, ¿conseguiste la salsa?"
    d "Ah si, aqui está, ¿si era esta cierto?"
    if sour == True:
        show dylan_smile_small at left
        hide dylan_talk_small
        m "{color=#b1f5a4}¡Bien! Te va a encantar la comida.{/color}"
        $ rightans = rightans + 1
        hide mom_idle with dissolve
        hide dylan_smile_small with dissolve
        "{i}Mamá y tú cenaron juntos- ¡la comida estaba deliciosa! Justo como lo había dicho ella.." 
        "{i}Al terminar, te sentías tan cansado que fuiste a dormir a tu cuarto enseguida.{/i}"
        show black  
        hide bg_kitchen with fade
    elif sweet == True:
        show dylan_idle_small at left
        hide dylan_talk_small  
        m "{color=#f5a5a4}Ahh...esta no era...{/color}"
        m "Pero no te preocupes, ¡de igual manera sabrá bien!."
        $ wrongans = wrongans + 1
        hide mom_idle with dissolve
        hide dylan_idle_small with dissolve
        "{i}Mamá y tú cenaron juntos, pero un sabor amargo permaneció en tu boca todo el tiempo-{/i}"
        "{i}Al terminar, te sentías tan cansado que fuiste a dormir a tu cuarto enseguida.{/i}"
        show black 
        hide bg_kitchen with fade

    #noche-dia1
    "{i}Normalmente, no sueñas mucho.{/i}"
    "{i}Tu realidad de música y películas deja mucho que desear en términos de soñar.{/i}"
    "{i}Aunque hoy sería {color=#7fb8c3}diferente..{/color}{/i}"
    "{i}Por un instante sentiste el viento-{/i}"
    "{i}Estabas cayendo.{/i}"
    d "¡AHHHH!"
    scene black with vpunch
    d "Ouch..."
    "{i}Era una oscuridad completa.{/i}"
    "{i}A lo lejos, veías una {color=#7fb8c3}luz{/color}...{/i}"
    "{i}-que llamaba a ti.{/i}"
    "{color=#8f8f8f}Dylan....{/i}"
    scene dream_forest with dramain 
    "{i}Lentamente te acercaste, curioso de lo que podría ser.{/i}"
    d "¿Un petirrojo?"
    "{i}Lo miraste curioso, y él pareció hacer lo mismo.{/i}"
    d "¿Que haces aquí amigo?"
    "{i}El petirrojo, casi como si te conociera, despegó, revoloteando hasta posarse en tu hombro.{i}"
    "{i}A tus oidos llegó una melodía suave y dulce... Era el canto de la pequeña ave.{/i}"
    scene dream_river with fade
    hide dream_forest
    "{i}De la nada, fuiste transportado a otro lado, parece que del mismo bosque.{/i}"
    "{i}Era un río, iridiscente, como si hubiera una bombilla por debajo..{/i}"
    "{i}Parecía algo {b}mágico{/b}, el agua cristalina y los pequeños nenúfares..{/i}"
    "{i}Fue en ese entonces que notaste una hojita, con algo escrito en ella.{/i}"
    d "{i}El futuro está en tus manos...{/i}"
    "{i}De repente te diste cuenta; no tuviste problemas para leerla.{/i}"
    "{i}Una voz te decía, 'Acércate... tengo el secreto que buscas...'{/i}"
    "{i}La curiosidad te ganó la batalla, y decidiste entrar de lleno al río.{/i}"
    scene black with fade
    hide dream_river
    "{i}Te estabas acercando más y más al fondo, al origen de la voz, y fue justo entonces cuando...{/i}"
    "{i}{color=#FFFFFF}¡¡DESPIERTA!!{/i}{/color}"

    scene bg_room with dissolve
    hide black
    with vpunch 
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
    "{i}Después de ese sueño, querías pasar por el parque, puede que hoy no estuviera tan concurrido como otros días.{/i}"
    "{i}...pero ibas un poco corto de tiempo, así que solo fuiste directo a la escuela.{/i}"
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
    a1 "Ok... Esta es la lista."
    show list_hunt
    scene bg_hall with pixellate
    hide bg_classroom
    "{i}Te encaminas a la biblioteca junto a Joel.{/i}"
    scene bg_library_l with pixellate
    hide bg_classroom
    a1 "Esto es genial, ¡¿muy emocionante no?!"
    d "Totalmente...."
    "{i}No te sientes muy atraído a esto, pero aun así sigues buscando.{/i}"
    d "¡Encontré uno!"
    b "¡SHHHHH! ¡Estamos en una biblioteca joven, no en el mercado!" 
    d "¡Ah, lo siento!"
    "{i}Sales rápidamente de la biblioteca, junto a Joel."
    scene bg_hall with pixellate
    hide bg_library_l
    d "Es el borrador rojo, y tiene un papel pegado."
    d "Tiene algo escrito en el..."
    a1 "¡Es un acertijo!"
    a1 "Vamos a ver que dice...."
    d "{i}Sin ser bestia un buen lomo...{/i}"
    d "{i}Sin ser árbol, tengo hojas...{/i}"
    d "{i}Solo adultos pueden entrar....{/i}"
    d "{i}Pero no te confundas...{/i}"
    d "{i}Y mi nombre en cada tomo...{/i}"
    d "{i}Bordeado de otros como yo me encontrarás...{/i}"
    d "{i}Rodeados de cuatro patas en las que descansar...{/i}"
    a1 "Hm..."
    a1 "¿Tú que crees que es?"
    menu problem_1:
        "¿No estará hablando sobre el libro que escribió el profesor?":
            a1 "Con el narcisismo que se manda ese señor..."
            a1 "No me sorprendería."
            d "Y si solo adultos pueden entrar..."
            d "...el salón de profesores sería."
            a1 "¡Genial!"
            a1 "Volvamos con los chicos, a ver que tienen."
        "Ni idea, de ser honesto.":
            a1 "Hm... pensemos más a fondo..."
            a1 "Si tiene hojas y no es un árbol..."
            a1 "¡Un libro!"
            d "Pero.. adonde estará..."
            d "Si solo adultos pueden entrar..."
            a1 "¿Quizás en la sala de profesores?"
            a1 "Pero la cosa es cual sería ese libro..."
            d "Si su nombre está en cada tomo..."
            a1 "¡El libro que escribió el profesor!"
            d "¡Si! Con el narcisismo que se lleva, encaja perfectamente."
            a1 "Ahora la cosa es como conseguir el bendito libro."
            a1 "Miremos si alguien lo tiene."
    "{i}Aún distraido y cansado, respondes-{/i}"
    d "Ok, vamos."
    scene bg_hall with pixellate
    hide bg_library_l
    a1 "¡Oigan!"
    a1 "¡Ya sabemos cual es uno de los elementos!"
    a2 "¿Si? ¿Qué es?"
    d "Es el libro que escribió el profesor."
    d "La cosa es que está en sala de profesores."
    a3 "¡No se preocupen!"
    a3 "En el salón tengo una copia de ese chisme."
    a2 "Perfecto."
    a2 "Mientras ustedes estaban en eso- "
    a2 "Nosotros encontramos el libro de economía y la regla."
    a1 "Entonces solo haría falta el bloc de notas, ¿verdad?"
    a3 "En efecto."
    a3 "Además el libro tenía una notita pegada al reverso con un acertijo."
    a1 "¿Y que dice el acertijo?"
    scene black with dissolve
    hide bg_hall
    show doctors_note_s 
    with fade
    a2 "No logro ver que dice..."
    a3 "Ni yo..."
    menu problem_h:
        "{i}¿Tomar 8 veces al dia durante 8 horas?{/i}":
            d "No entiendo muy bien que dice, pero parece una nota médica."
            a1 "Oye si.... ¡La enfermería!"
            a3 "¡Bien hecho!"
        "{i}Diablos... tampoco logro entender... Mejor me quedo callado.{/i}":
            a1 "Agh... Creo que es una nota de pasillo..."
            a2 "Hmm.... Pero no puede ser el baño-"
            a2 "Un bloc de notas en el baño no tiene sentido."
            d "¿En la parte de arriba dice hospital?"
            a3 "Hmm.... podría ser la enfermería.."
            a1 "No perdemos nada en buscar.... vamos para allá."
    scene black with pixellate
    scene bg_infirmary with fade 
    hide black
    a3 "Busquen en los casilleros del fondo, ahi puede estar."
    d "Yo buscaré en el escrito-"
    a2 "Lo encontré!"
    scene black with dissolve
    hide bg_infirmary
    scene bg_classroom with fade
    mr "¡Tenemos los primeros en llegar!"
    mr "¿Cómo les fue, chiquillos?"
    menu: 
        "{i}Dejas que alguien más responda.{/i}":
            a1 "¡Muy bien!"
            mr "Me alegra mucho, ya vayan."
            mr "¡Que tengan una muy buena tarde!"
        "¡Genial, profesor!":
            a1 "{i}{color=#8f8f8f}Dylan está actuando diferente..."
            mr "Eso es bueno. Pero ya vayan a recoger sus cosas."
            mr "¡Que tengan sol y lluvia para cuando lo necesiten!"
    "{i}Después de un día tan ajetreado, llegas a casa muerto de sueño.{/i}"
    d "{i}{color=#83a5ae}Hm... mamá no está en casa....{/i}{/color}"
    d "Aprovecharé para descansar."
    "{i}No paraste por nada de camino a tu cuarto; solo entraste-{/i}"
    "{i}Recogiste tu mp3 y te desplomaste en tu cama.{/i}"
    show bg_bed with fade
    "{i}Lentamente te quedaste dormido,{/i}"
    "{i}{color=#83a5ae}Transportado a ese bosque encantado...{/i}{/color}"
    show black with dramain 
    show dream_river with dramaout
    hide bg_bed
    hide black 
    "{i}Esta vez te levantaste al lado del río...{/i}"
    "{i}Con el petirrojo posado en una piedra cerca a ti...{/i}"
    d "Hola amiguito...."
    d "¿De donde viniste?"
    "{i}El petirrojo, como si entendiera lo que dijeras, levantó el vuelo.{/i}"
    "{i}Se dirigió al río, y desapareció en una nube de polvo iridiscente.{/i}"
    "{i}De nuevo, la voz llamaba a ti desde adentro del río..."
    "{i}{color=#8f8f8f}Ven aquí, niño.....{/i}{/color}"
    "{i}{color=#8f8f8f}Tanto talento....{/i}{/color}"
    "{i}{color=#8f8f8f}Tanto potencial....{/i}{/color}"
    "{i}{color=#8f8f8f}Tan malgastado.....{/i}{/color}"
    "{i}{color=#8f8f8f}Acércate.....{/i}{/color}"
    "{i}{color=#8f8f8f}Y cumple tus sueños....{/i}{/color}"
    "{i}La voz penetró en tu alma....{/i}"
    "{i}Y sin pensarlo, saltaste en el río-"
    show black 
    hide dream_river
    show bg_room with vpunch
    hide black2
    d "¡¡OUCH!!"
    d "Ayayay.... mi cabeza..."
    d "Dios.... "
    "{i}Sin darte cuenta, saltaste de tu cama.{/i}"
    show dylan_idle_small with dissolve
    d "Solo fue una pesadilla...."
    d "Que asco."
    hide dylan_idle_small with dissolve
    "{i}Tuviste suerte- mamá aún no había llegado.{/i}"
    "{i}Se hubiera armado la de las grandes si hubiera visto esto...{/i}"
    "{i}Decidiste intentar hacer los problemas de matemáticas de nuevo.{/i}"
    d "{color=#8f8f8f}A ver.... el problema dice-{/color}"
    show black with fade
    hide bg_room 
    d "{color=#8f8f8f}Zi qara qreqarar um qazte1 mecezitaz:{/color}"
    show sugar_bag
    d "{color=#8f8f8f}l/E de 7S0g be asucar-{/color}"
    show yeast_bag
    d "{color=#8f8f8f}E/A kuartoz be un cilo de narima-{/color}"
    show butter_bar
    d "{color=#8f8f8f}y E/S be uma darra de namtepuilla be 200 qranoz-{/color}"
    d "{color=#8f8f8f}¿Qué cantidades ({b}en gramos{/b}) requieres para cada uno?{/color}"
    menu problem_c:
        "l/E de TS0g be asucar...":
            menu problem_s:
                "Ehh.... 720 sobre 3..... ¡son 240g!":
                    $ sugar = 240
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
                "Hmm.... 750 sobre 3..... ¿no serían 250g?":
                    $ sugar = 250
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c 
                "Agh... 920 sobre 3.... ¡No da!":
                    $ sugar = 0
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
        "E/A kuartoz de un cilo de harima...":
            menu problem_f:
                "Ehm... Si un kilo es 1000g... ¡750g!":
                    $ flour = 750
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
                "Uh.... ¿Serían solo 3/4 y ya no?":
                    $ flour = 0
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
                "... Si un kilo es 1000g.... ¡son 250g!":
                    $ flour = 250
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
        "E/S de una barra de mantequilla de 200g...":
            menu problem_b:
                "¿3/2 de 200?.... ¡¿es 300?! Ni idea...":
                    $ butter = 300
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
                "Mm.. ¿1/5 de 200?.. ¡40!":
                    $ butter = 40
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c 
                "3/5 de 200.. ¡Eureka! ¡120!":
                    $ butter = 120 
                    $ problem_cc = problem_cc + 1
                    if problem_cc >= 3:
                        jump break_1
                    else:
                        jump problem_c
    label break_1:
        d "Por fin..."
    "{i}Después de resolver los problemas revisaste tu cuadernillo por las respuestas.{/i}"
    $ solve_c = sugar + flour + butter 
    if solve_c == 1120:
        "{i}{color=#b1f5a4}La solución te dió justo como lo indicaba el libro-{/i}{/color}"
        "{i}¡Una definitiva mejora!{/i}"
        d "¡Si!"
        $ rightans = rightans + 1
    elif solve_c < 1120:
        "{i}{color=#8f8f8f}Hubo uno o dos datos que te salieron mal, pero igual mejoraste-{i}{/color}"
        "{i}Aunque no quedaste satisfecho con esto- otro mal sabor de boca.{i}"
        $ wrongans = wrongans + 1
    elif solve_c > 1120 or solve_c < 530:
        "{i}{color=#f5a5a4}El resultado que decía tu cuadernillo era absolutamente diferente a lo que tu hallaste-{/i}{/color}"
        "{i}Te sentías como un tonto, tanto esfuerzo por poco resultado..{/i}"
        $ wrongans = wrongans + 2
    m "¡Llegué!"
    "{i}Saliste de tu cuarto a saludar a mamá.{/i}"
    scene bg_kitchen
    hide bg_room
    show mom_idle at left
    if rightans >= 1:
        show dylan_smile_small at right
        with moveinleft
        d "¡Hola ma!"
        m "¿Cómo te va, mijito?"
        d "¿Bien ma, y a ti?"
        m "Muy bien... ¡gracias!"
        m "Hoy te noto diferente, hijo."
        m "¿Que ha pasado?"
        d "Me ha ido bien en la escuela, he mejorado en matemáticas..."
        m "Me alegro hijo."
        m "Recuerda lo que siempre te digo---"
        m "Persevera..."
        d "..y obtendrás buenos resultados."
        m "Ese es el ánimo!"
    elif wrongans >= 2:
        show dylan_idle_small at right
        with moveinleft
        d "¡Hola ma!"
        m "¿Como te fue hoy hijo?"
        d "Bien, bien."
        d "¿y a ti como te ha ido ma?"
        m "Muy bien, igualmente."
        m "¿Que has hecho mientras yo llegaba?"
        d "Nada... estaba intentando resolver ejercicios de matemáticas, pero se me dificultó un poco."
        m "¿Quieres que te ayude, hijo?"
        menu dilemma_1:
            "¡Si!, por favor.":
                m "Ok, vamos a ello."
                hide mom_idle with fade
                hide dylan_idle_small with fade 
                "{i}Después de pasar varias horas estudiando, sientes que realmente has hecho progreso.{/i}"
                "{i}Te vas a dormir con una sensación de satisfacción.{/i}"
            "Mm no, pero gracias de igual manera.":
                m "Ok, estoy aqui pendiente si quieres que te ayude."
                d "Gracias ma."
            "Gracias, pero no. Yo me las arreglo.":
                m "Hmm... ok. Si necesitas ayuda aquí estoy."
                show notice_r
                $ suspicion = 1

