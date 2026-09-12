# ts_pos_receipt_custom

Recibo personalizado para el Punto de Venta (POS) de Odoo 18 — estilo Tecnosoft.

Misma información que el recibo nativo, pero en un **formato compacto y neutro**
que aprovecha mejor el espacio de impresión.

## El problema

Al imprimir el recibo desde Windows, las líneas se solapan. Desde Android se ve bien.

**Causa:** el interlineado del recibo depende del navegador. En Windows colapsa
y las líneas se pisan.

## Cómo funciona

En Odoo 18 el recibo del POS **no es un report de servidor**: es un componente
OWL (`point_of_sale.OrderReceipt`) que se renderiza en el navegador. Este módulo
por tanto es 100% client-side:

1. **CSS** (`static/src/css/receipt_compact.css`) en el bundle `point_of_sale._assets_pos`:
   - `font-family: 'Courier New', monospace` → rendering uniforme en todos los navegadores
   - `font-size: 12px`, `line-height: 1.15` → compacto, sin overlap
   - Negro puro, sin colores decorativos

2. **Herencia OWL** (`static/src/xml/order_receipt.xml`) con `t-inherit="point_of_sale.OrderReceipt"`:
   - Cambia "Powered by Odoo" por **"powered by tecnosoft"**

3. **Logo**: ya es nativo (`ReceiptHeader` usa `res.company.logo`) — no se toca.

**No toca** impuestos, pagos ni lógica de servidor.

## Compatibilidad

- Odoo 18.0 (community y enterprise)
- Odoo 17/19: pendiente de validar (el xpath del footer difiere en 19)

## Instalación

```bash
# Opción A: clonar el repo y apuntar el addons_path al módulo
cd /opt/odoo/addons
git clone git@github.com:lfcamarac/pos_receipt_custom.git

# Opción B: copiar solo el módulo
git clone git@github.com:lfcamarac/pos_receipt_custom.git /tmp/prc
cp -r /tmp/prc/ts_pos_receipt_custom /opt/odoo/addons/
```

En **CloudPepper**: Add GitHub repository → `lfcamarac/pos_receipt_custom` → rama `v18/main`.

Luego: Apps → **POS Receipt Custom (Tecnosoft)** → Instalar.

## Estructura

```
pos_receipt_custom/            ← repo
├── README.md
└── ts_pos_receipt_custom/     ← módulo Odoo
    ├── __init__.py
    ├── __manifest__.py        ← assets en point_of_sale._assets_pos
    └── static/src/
        ├── css/receipt_compact.css
        └── xml/order_receipt.xml
```

## Versión

- 18.0.1.1.0

## Autor

Tecnosoft — https://tecnosoft.dev
