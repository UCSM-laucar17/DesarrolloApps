import json
from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

# 1. COMPONENTE MIDDLEWARE
class MiddlewareTokenSeguridad:
    
    def __init__(self, aplicacion_interior):
        self.aplicacion_interior = aplicacion_interior
        self.token_valido = "Bearer TOKEN_SECRETO_2026"
    def __call__(self, environ, start_response):
        token_recibido = environ.get('HTTP_AUTHORIZATION', '')
        if token_recibido != self.token_valido:
            payload_error = b'{"error": "401 Unauthorized - Token invalido o ausente"}'
            start_response('401 Unauthorized', [
                ('Content-Type', 'application/json; charset=utf-8'),
                ('Content-Length', str(len(payload_error)))
            ])
            return [payload_error]

        return self.aplicacion_interior(environ, start_response)


# 2. MOTOR DE INGESTA POLIMÓRFICA Y VALIDACIÓN DE ESQUEMAS
class AplicacionInscripcionesWSGI:
    def __call__(self, environ, start_response):
        ruta_solicitada = environ.get('PATH_INFO', '/')
        metodo_http = environ.get('REQUEST_METHOD', '')

        if ruta_solicitada != '/api/inscripciones':
            payload = b'{"error": "404 Not Found - Endpoint huerfano o no mapeado"}'
            start_response('404 Not Found', [('Content-Type', 'application/json'), ('Content-Length', str(len(payload)))])
            return [payload]

        if metodo_http != 'POST':
            payload = b'{"error": "405 Method Not Allowed - El endpoint exige mutacion via POST"}'
            start_response('405 Method Not Allowed', [('Content-Type', 'application/json'), ('Content-Length', str(len(payload)))])
            return [payload]

        tamano_buffer = int(environ.get('CONTENT_LENGTH', '0') or '0')
        if tamano_buffer == 0:
            payload = b'{"error": "400 Bad Request - Payload vacio (Zero Bytes)"}'
            start_response('400 Bad Request', [('Content-Type', 'application/json'), ('Content-Length', str(len(payload)))])
            return [payload]

        cuerpo_bytes = environ['wsgi.input'].read(tamano_buffer)
        metadato_formato = environ.get('CONTENT_TYPE', '')

        try:
            if 'application/json' in metadato_formato:
                dto_diccionario = json.loads(cuerpo_bytes.decode('utf-8'))

            elif 'application/x-www-form-urlencoded' in metadato_formato:
                diccionario_listas = parse_qs(cuerpo_bytes.decode('utf-8'))
                dto_diccionario = {k: v[0] for k, v in diccionario_listas.items()}

            else:
                payload = b'{"error": "415 Unsupported Media Type - Ingesta exige JSON o URL-Encoded"}'
                start_response('415 Unsupported Media Type', [('Content-Type', 'application/json'), ('Content-Length', str(len(payload)))])
                return [payload]

        except (json.JSONDecodeError, ValueError):
            payload = b'{"error": "400 Bad Request - Corrupcion detectada en el flujo binario"}'
            start_response('400 Bad Request', [('Content-Type', 'application/json'), ('Content-Length', str(len(payload)))])
            return [payload]

        llaves_obligatorias = {'dni', 'correo_electronico', 'programa_academico'}
        llaves_faltantes = llaves_obligatorias - dto_diccionario.keys()

        if llaves_faltantes:
            error_esquema = {"error": f"Violacion del contrato de datos. Faltan propiedades obligatorias: {list(llaves_faltantes)}"}
            payload = json.dumps(error_esquema).encode('utf-8')
            start_response('400 Bad Request', [('Content-Type', 'application/json; charset=utf-8'), ('Content-Length', str(len(payload)))])
            return [payload]

        respuesta_exitosa = {
            "estado": "Inscripcion procesada, estandarizada y auditada exitosamente",
            "datos_registrados": dto_diccionario
        }
        payload_ok = json.dumps(respuesta_exitosa).encode('utf-8')
        start_response('201 Created', [
            ('Content-Type', 'application/json; charset=utf-8'),
            ('Content-Length', str(len(payload_ok)))
        ])
        return [payload_ok]


# 3. LEVANTAMIENTO DE LA INFRAESTRUCTURA DE RED
if __name__ == '__main__':
    puerto = 8110
    aplicacion_base = AplicacionInscripcionesWSGI()
    aplicacion_protegida = MiddlewareTokenSeguridad(aplicacion_base)
    
    servidor_academico = make_server('127.0.0.1', puerto, aplicacion_protegida)
    print(f"[INFO] Servidor Academico UCSM activo en http://127.0.0.1:{puerto}")
    print("Presiona Ctrl + C para detenerlo.")
    servidor_academico.serve_forever()
