import os
import json
import mimetypes
from urllib.parse import parse_qs, urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer

base_datos_inventario = [
    {"id": i, "nombre": f"Componente Electronico {i}", "categoria": "Sensores" if i % 2 == 0 else "Actuadores", "precio": round(i * 1.5, 2)}
    for i in range(1, 501)
]
class ServidorHibridoAvanzado(BaseHTTPRequestHandler):

    def do_GET(self):
        url_parseada = urlparse(self.path)
        ruta_limpia = url_parseada.path
        if ruta_limpia.startswith('/api/inventario'):
            self.procesar_api_dinamica(url_parseada.query)
        else:
            self.procesar_archivo_estatico(ruta_limpia)

    # 1. GESTOR DE ARCHIVOS ESTÁTICOS CON BLINDAJE DE RUTAS PATH
    def procesar_archivo_estatico(self, ruta_cruda):
        directorio_publico = os.path.abspath(os.path.join(os.getcwd(), 'public'))
        ruta_limpia = ruta_cruda.lstrip('/')
        if not ruta_limpia or ruta_limpia == '':
            ruta_limpia = 'index.html'

        ruta_resuelta = os.path.abspath(os.path.join(directorio_publico, ruta_clean := ruta_limpia))

        if not ruta_resuelta.startswith(directorio_publico) or not os.path.isfile(ruta_resuelta):
            self.send_error(404, "Recurso no encontrado o acceso estrictamente denegado.")
            return

        tipo_mime, _ = mimetypes.guess_type(ruta_resuelta)

        try:
            with open(ruta_resuelta, 'rb') as archivo_fisico:
                contenido = archivo_fisico.read()

            self.send_response(200)
            self.send_header('Content-Type', tipo_mime or 'application/octet-stream')
            self.send_header('Content-Length', str(len(contenido)))
            self.end_headers()
            self.wfile.write(contenido)
        except IOError:
            self.send_error(500, "Error de Entrada/Salida al acceder al archivo físico.")

    # 2. MOTOR DE FILTRADO, BÚSQUEDA Y PAGINACIÓN POR QUERY STRING
    def procesar_api_dinamica(self, cadena_consulta):
        parametros = parse_qs(cadena_consulta)

        try:
            limite = int(parametros.get('limite', ['10'])[0])
            pagina = int(parametros.get('pagina', ['1'])[0])
            filtro_texto = parametros.get('filtro', [''])[0].strip().lower()
        except ValueError:
            self.emitir_json_error(400, "Error de Casting: Los parametros 'limite' y 'pagina' deben ser enteros.")
            return

        if limite > 100:
            limite = 100
        if limite <= 0 or pagina <= 0:
            self.emitir_json_error(400, "Los valores de paginacion deben ser mayores a cero.")
            return
        coleccion_filtrada = base_datos_inventario
        if filtro_texto:
            coleccion_filtrada = [
                item for item in base_datos_inventario
                if filtro_texto in item['nombre'].lower()
            ]
        indice_desplazamiento = (pagina - 1) * limite
        indice_corte = indice_desplazamiento + limite
        datos_paginados = coleccion_filtrada[indice_desplazamiento:indice_corte]
        respuesta_json = {
            "metadatos": {
                "pagina_actual": pagina,
                "limite_solicitado": limite,
                "total_coincidencias": len(coleccion_filtrada),
                "total_base_datos": len(base_datos_inventario)
            },
            "registros": datos_paginados
        }

        payload = json.dumps(respuesta_json).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def emitir_json_error(self, codigo_http, mensaje_error):
        payload = json.dumps({"error": mensaje_error}).encode('utf-8')
        self.send_response(codigo_http)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


# 3. LEVANTAMIENTO DEL SERVIDOR HÍBRIDO NATIVO
if __name__ == '__main__':
    puerto = 8120
    servidor_hibrido = HTTPServer(('127.0.0.1', puerto), ServidorHibridoAvanzado)
    print(f"[INFO] Servidor Hibrido Activo en http://127.0.0.1:{puerto}")
    print("Presiona Ctrl + C para detenerlo.")
    servidor_hibrido.serve_forever()
