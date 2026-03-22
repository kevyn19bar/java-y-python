**Ejercicios Java** 

*Nivel 1: Frecuencia de Caracteres Analítico*
Diseñar clase AnalizadorFrecuencia. Declarar variable Map<Character, Integer>. Implementar función contarFrecuencia(List<Character> flujo). Iterar la lista mediante un ciclo. Aplicar condicional: si el carácter existe como clave en el diccionario, incrementar su valor; si no, inicializarlo en 1. Retornar el diccionario.

*Nivel 2: Depuración de Trayectorias Inmutables*
Definir Record o clase inmutable TuplaCoordenada con campos x, y. Diseñar clase MotorGrafico. Implementar función filtrarRuta(List<TuplaCoordenada> ruta). Declarar List<TuplaCoordenada> interna para ruta validada y Map<String, Integer> para conteo de cuadrantes. Iterar la lista de entrada. Evaluar coordenadas con condicionales para determinar cuadrante, añadir a la nueva lista y actualizar el diccionario de conteo.

*Nivel 3: Traductor Transaccional en Memoria*
Diseñar clase MotorTraduccion. Declarar Map<String, String> como diccionario base. Implementar función procesarLote(List<String> tokens). Declarar List<Record> (tupla: tokenOriginal, estadoError). Iterar los tokens. Condicional: si el token existe en el diccionario, procesar; si no, añadir la tupla de error a la lista correspondiente. Retornar estructura compleja con aciertos y errores.

*Nivel 4: Agrupación Clasificada de Inventario*
Diseñar clase Clasificador. Definir Record TuplaProducto (id, categoria). Implementar función agruparPorCategoria(List<TuplaProducto> inventario). Declarar Map<String, List<Integer>> (diccionario de categoría a lista de IDs). Ciclo sobre la lista de tuplas. Condicional: verificar existencia de la categoría en el diccionario. Instanciar nueva lista si es nulo, o añadir el ID a la lista existente.

*Nivel 5: Caché Estructurado con Expiración*
Diseñar clase GestorCache. Definir Record TuplaCache (valor, timestamp). Declarar variable Map<String, TuplaCache>. Implementar función limpiarExpirados(long tiempoActual). Iterar sobre el conjunto de claves del diccionario. Evaluar condicional de diferencia de tiempos. Extraer claves caducadas a una List<String>. Iterar la lista resultante para ejecutar la eliminación en el diccionario principal.

*Nivel 6: Consolidación Matricial de Ventas*
Diseñar clase Liquidador. Implementar función consolidar(List<Map<String, Double>> reportesDiarios). Declarar Map<String, Double> consolidado y List<Record> para anomalías (tupla: diaIndex, claveError). Ciclo principal sobre la lista de diccionarios. Ciclo anidado sobre las claves de cada diccionario. Condicional: si el valor es negativo, registrar tupla en lista de anomalías; de lo contrario, sumar al acumulado en el diccionario principal.

*Nivel 7: Auditoría Electoral Ponderada con Veto*
Diseñar clase AuditorElectoral. Declarar List<String> de entidades vetadas y Map<String, Integer> para escrutinio. Implementar función procesarSufragios(List<Record> votos). El Record es una tupla (entidad, peso). Ciclo iterativo sobre la lista. Condicional compuesto: verificar si la entidad está en la lista de vetados. Si no está, multiplicar peso por factor interno y actualizar el diccionario de escrutinio.

*Nivel 8: Grafo Dirigido con Mapeo de Pesos*
Diseñar clase EnrutadorNodos. Definir Record TuplaArista (destino, costo). Declarar variable Map<String, List<TuplaArista>> como matriz de adyacencia. Implementar función evaluarCaminos(String nodoOrigen). Extraer la lista de tuplas del diccionario. Ciclo sobre las aristas. Evaluar mediante condicional si el costo supera el límite global. Registrar rutas viables en un nuevo diccionario de salida.

*Nivel 9: Motor de Reglas de Pricing Dinámico*
Diseñar clase MotorPricing. Declarar List<Record> como conjunto de reglas (tupla: categoria, descuento, umbral). Implementar función aplicar(Map<String, List<Double>> carrito). El diccionario agrupa precios por categoría. Iterar diccionario. Ciclo anidado para cruzar con la lista de tuplas de reglas. Condicional estricto: si la suma de la lista de precios supera el umbral de la tupla, aplicar descuento y actualizar el valor en un diccionario de resultados.

*Nivel 10: Indexador Lexicográfico Invertido*
Diseñar clase MotorIndexacion. Definir Record TuplaAparicion (idDocumento, indicePalabra). Declarar Map<String, List<TuplaAparicion>> como índice invertido principal. Implementar función indexarCorpus(Map<Integer, List<String>> corpus). Ciclo exterior sobre las entradas del diccionario corpus. Ciclo interior sobre la lista de strings. Condicional: mutar el índice principal agregando nuevas tuplas de aparición a las listas correspondientes por cada término validado.

**Ejercicios Python**

*Nivel 1: Filtrado Discreto de Muestras*
Definir clase FiltroSenal. Implementar método limpiar_datos(muestras: list). Declarar variable dict para métricas y list de tuples para datos procesados (indice, valor). Iterar la lista de entrada. Aplicar condicional de umbral de ruido. Almacenar valores válidos como tuplas en la nueva lista y registrar el conteo de anomalías en el diccionario.

*Nivel 2: Sistema de Bitácora Estructurada*
Definir clase AuditorAcceso. Inicializar dict como registro principal. Implementar método procesar_logs(logs: list[tuple]). Tupla de entrada: (usuario, accion). Iterar la lista. Condicional evaluando la acción. Si el usuario no existe en el diccionario, inicializarlo con una lista vacía. Hacer append de la acción a la lista correspondiente dentro del diccionario de ese usuario.

*Nivel 3: Conciliador de Inventario Relacional*
Definir clase GestorAlmacen. Declarar variable de estado dict con existencias actuales. Implementar método conciliar(movimientos: list[tuple]). Tupla: (sku, operacion, cantidad). Iterar lista de movimientos. Condicionales anidados para operaciones ('IN', 'OUT'). Si es 'OUT', verificar en el diccionario si hay stock suficiente. Registrar operaciones fallidas en una nueva lista.

*Nivel 4: Agrupador de Metadatos Hash*
Definir clase ProcesadorArchivos. Implementar método clasificar(archivos: list[dict]). Cada diccionario contiene 'nombre', 'ext', 'hash'. Inicializar dict de salida. Iterar la lista de diccionarios. Condicional: si la extensión no existe en el diccionario de salida, crear la clave con una lista vacía. Extraer datos para formar una tupla (nombre, hash) y agregarla a la lista correspondiente en el diccionario.

*Nivel 5: Simulador ORM (Mapeo Objeto-Relacional)*
Definir clase MotorORM. Implementar método inner_join(tabla_a: list[dict], tabla_b: list[dict], clave_foranea: str). Retornar una list de tuples. Iterar tabla_a. Ciclo anidado iterando tabla_b. Condicional de igualdad sobre los valores de la clave foránea en ambos diccionarios. Empaquetar los registros coincidentes en una tupla de diccionarios y añadir a la lista resultante.

*Nivel 6: Validador Cíclico de Topología de Red*
Definir clase ValidadorRed. Inicializar variable dict donde las claves son nodos y los valores son listas de tuplas (nodo_destino, latencia). Implementar método verificar_bidireccionalidad(nodos_objetivo: list). Iterar la lista de nodos. Extraer la lista de conexiones del diccionario. Condicional cruzado: buscar si el nodo_destino contiene en su propio registro del diccionario una tupla de retorno hacia el nodo origen.

*Nivel 7: Máquina de Transición de Estados Compleja*
Definir clase AutomataFinito. Declarar dict de reglas: estado_origen mapeado a list de tuplas (condicion_str, estado_destino). Implementar método ejecutar_secuencia(eventos: list). Declarar variable estado_actual. Iterar la lista de eventos. Acceder a las reglas del estado_actual en el diccionario. Bucle anidado para evaluar las tuplas de transición mediante condicionales. Actualizar estado_actual.

*Nivel 8: Optimizador de Rutas Logísticas de Distribución*
Definir clase Logistica. Implementar método calcular_costos(rutas_candidatas: list[tuple], tarifas: dict). La tupla contiene secuencias de nodos (A, B, C). Iterar la lista de tuplas. Para cada tupla, iterar sus elementos generando pares. Consultar el diccionario de tarifas condicionalmente. Si el tramo no existe, invalidar ruta. Almacenar resultados válidos en un nuevo diccionario mapeando la tupla de ruta a su costo total.

*Nivel 9: Compilador de Configuración Jerárquica*
Definir clase GestorConfiguracion. Implementar método fusionar_entornos(entornos: list[dict]). Declarar diccionario resultante y lista de tuplas para rastreo de sobreescrituras (clave, valor_viejo, valor_nuevo). Iterar la lista de diccionarios. Ciclo anidado sobre claves y valores. Condicional: si la clave ya existe en el diccionario resultante, agregar la tupla de mutación a la lista, luego actualizar el diccionario.

*Nivel 10: Motor Heurístico de Detección de Fraude Transaccional*
Definir clase MotorAntiFraude. Declarar dict de perfiles históricos (id_usuario -> list de tuplas transaccionales (monto, timestamp)). Implementar método evaluar_lote(transacciones: list[dict]). Iterar el lote. Extraer datos y formar tuplas. Consultar historial en el diccionario. Ejecutar condicionales estadísticos complejos evaluando la nueva tupla contra la lista histórica del diccionario. Retornar un dict segmentando id_usuario en listas de tuplas aprobadas o rechazadas.