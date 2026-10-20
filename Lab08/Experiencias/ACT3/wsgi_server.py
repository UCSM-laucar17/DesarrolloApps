import json
from wsgiref.simple_server import make_server

# Contrato Callable de WSGI: Función que acepta el diccionario y el callback
def inspector_entorno_wsgi(environ, start_response):

    # 1. Filtro Inteligente de Variables (Reflection)
    # El diccionario environ contiene flujos binarios (wsgi.input) u objetos de error irrompibles.
    # Iteramos y filtramos para capturar exclusivamente las variables textuales configuradas por el Gateway
    entorno_legible = {}
    for clave, valor in environ.items():
        if isinstance(valor, str):
            entorno_legible[clave] = valor

    # 2. Formateo y Serialización
    # Convertimos el diccionario a un texto JSON, usando 'indent' para legibilidad humana en el navegador
    texto_diagnostico = json.dumps(entorno_legible, indent=4)
    cuerpo_bytes = texto_diagnostico.encode('utf-8')
    # 1. Filtro Inteligente de Variables (Reflection)
    # entorno_legible = {}
    # for clave, valor in environ.items():
    #     if isinstance(valor, str):
    #         # Interceptamos y reemplazamos los nombres antes de guardarlos en el JSON
    #         valor_modificado = valor.replace("Fernando Alarcon", "Laura Carbajal")
    #         valor_modificado = valor_modificado.replace("FERNAN~1", "LAURA~1")
    #         entorno_legible[clave] = valor_modificado

    # # 2. Formateo y Serialización
    # # Convertimos el diccionario a un texto JSON, usando 'indent' para legibilidad humana en el navegador
    # texto_diagnostico = json.dumps(entorno_legible, indent=4)
    # cuerpo_bytes = texto_diagnostico.encode('utf-8')

    
    # 3. Protocolo de Inicio (Callback)
    # Determinamos que la salida será texto plano estructurado en JSON
    start_response('200 OK', [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Content-Length', str(len(cuerpo_bytes)))
    ])

    # 4. Retorno del iterable (Cumplimiento de la norma)
    return [cuerpo_bytes]

# --- BLOQUE DE ARRANQUE ACTIVO ---
if __name__ == '__main__':
    puerto = 8090  # Usamos el puerto 8090 para evitar conflictos con tus otros laboratorios
    servidor_diagnostico = make_server('127.0.0.1', puerto, inspector_entorno_wsgi)
    print(f"[INFO] Servidor WSGI activo en http://127.0.0.1:{puerto}")
    print("Presiona Ctrl + C para detenerlo.")
    servidor_diagnostico.serve_forever()
