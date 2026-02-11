from ..externos import clientes as cli
from ..externos import proveedores as pro
import articulos as art

type t_factura = dict[str, str | int | float]

def generar_facturas() -> list[t_factura]:
    facturas: list[t_factura] = []
    for cliente in cli.clientes:
        for proveedor in pro.proveedores:
            for articulo in art.articulos:
                factura: t_factura = {
                    'cliente': cliente['id'],
                    'proveedor': proveedor['id'],
                    'articulo': articulo['id'],
                    'cantidad': 1,
                    'total': articulo.get('precio', 0)
                }
                facturas.append(factura)
    return facturas

facturas_generadas = generar_facturas()
print(facturas_generadas)
