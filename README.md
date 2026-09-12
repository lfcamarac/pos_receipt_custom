# ts_pos_receipt_custom

Recibo personalizado para el Punto de Venta (POS) de Odoo 18 — estilo Tecnosoft.

Misma información que el recibo nativo, pero en un **formato compacto y neutro**
que aprovecha mejor el espacio de impresión.

## El problema

Al imprimir el recibo desde Windows (Edge/Chrome), las líneas se solapan.
Desde Android (Chrome mobile) se ve bien.

**Causa:** el template nativo de Odoo no fuerza `line-height` ni `font-family`,
así que cada navegador renderiza el recibo a su manera. En Windows el
interlineado colapsa y las líneas se pisan.

## La solución

CSS explícito e `!important` que elimina la dependencia del navegador:

| Propiedad | Nativo | Este módulo |
|---|---|---|
| `font-family` | la del navegador | `'Courier New', monospace` (uniforme en todos) |
| `font-size` | 3mm | 2.6mm (~13% más compacto) |
| `line-height` | indefinido | `1.0em` (sin aire extra entre líneas) |
| `color` | heredado | `#000` negro puro |
| márgenes | ~3mm | ~1mm entre secciones |

## Qué añade

- **Logo de la compañía** arriba, centrado (usa `res.company.logo`, mismo
  patrón `image_data_uri()` que el nativo; se oculta si la compañía no tiene logo).
- **Footer "powered by tecnosoft"** al final, con línea divisoria.
- Todo lo demás es **idéntico al nativo**: encabezado de compañía, datos
  fiscales, líneas con impuestos, totales, métodos de pago discriminados,
  códigos de barras/QR y pie ORIGINAL/COPIA.

**No toca** impuestos, pagos ni lógica de Odoo: solo CSS y dos bloques
visuales (logo + footer) vía herencia de la plantilla `point_of_sale.report_saleorder`.

## Compatibilidad

- Odoo 18.0 (community y enterprise)
- Odoo 19: pendiente de validar

## Instalación

El repo es autocontenido: el módulo vive en `ts_pos_receipt_custom/`.

```bash
# Opción A: clonar directo en el addons_path
cd /opt/odoo/addons   # o tu addons_path
git clone git@github.com:lfcamarac/pos_receipt_custom.git
# → queda en /opt/odoo/addons/pos_receipt_custom/ts_pos_receipt_custom
#   (asegúrate de que el addons_path incluya ese directorio)

# Opción B: copiar solo el módulo
git clone git@github.com:lfcamarac/pos_receipt_custom.git /tmp/prc
cp -r /tmp/prc/ts_pos_receipt_custom /opt/odoo/addons/
```

Luego:

1. Reiniciar Odoo: `sudo systemctl restart odoo`
2. Apps → Actualizar lista de apps
3. Buscar **"POS Receipt Custom (Tecnosoft)"** → Instalar
4. Imprimir un ticket desde el POS para verificar

## Estructura

```
pos_receipt_custom/            ← repo
├── README.md                  ← este archivo
└── ts_pos_receipt_custom/     ← módulo Odoo
    ├── __init__.py
    ├── __manifest__.py
    └── views/
        └── pos_templates.xml  ← herencia del template nativo
```

## Versión

- 18.0.1.0.0

## Autor

Tecnosoft — https://tecnosoft.dev
