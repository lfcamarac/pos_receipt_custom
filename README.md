# ts_pos_receipt_custom

Recibo personalizado para el Punto de Venta (POS) — estilo Tecnosoft.

Misma información que el recibo nativo, pero en un **formato compacto y neutro**
que aprovecha mejor el espacio de impresión, con footer
"powered by tecnosoft" y detalle de ventas (X/Z) rediseñado.

## Qué hace

1. **Interlineado uniforme + anti-solape**: hereda el estilo nativo del recibo
   (`pos_order_receipt_style`) con `line-height` fijo, montos sin envolver y
   nombres con wrap seguro. Es el mismo fix que en 18/19 contra el montado de
   líneas al imprimir desde Windows.
2. **Logo proporcional**, sin distorsión.
3. **Footer** "powered by tecnosoft" en lugar de "Powered by Odoo".
4. **Detalle de ventas (X/Z)** rediseñado: Ventas / Devoluciones / Pagos /
   Impuestos / Total, con cantidad + UdM y sub-línea de descuento por producto.

## Cómo funciona en Odoo 20

En Odoo 20 el recibo del POS **ya no es un componente OWL**: el pipeline es

```
GeneratePrinterData.generateReceiptData() / generateSaleDetailsData()
        → iframe renderiza el QWeb servidor point_of_sale.pos_order_receipt
          (o pos_sale_details_receipt para el X/Z)
        → ticketPrinter.printOrderReceipt()
```

El componente OWL `OrderReceipt` y el `ReceiptScreen` fueron eliminados. Este
módulo por tanto es:

1. **QWeb servidor** (`views/pos_order_receipt_custom.xml`), heredando los
   templates nativos `receipt/*.xml` por xpath (mismo patrón que
   `pos_dual_currency.pos_order_receipt_igtf`):
   - `pos_order_receipt_footer` → footer tecnosoft.
   - `pos_sale_details_receipt` → layout ts-sales del X/Z.
   - `pos_order_receipt_style` → CSS del recibo. En 20 el recibo se renderiza
     en un iframe (srcdoc): el CSS del bundle `_assets_pos` (enfoque v19) no
     llega al iframe; el estilo vive en este template.
2. **Un patch JS** (`static/src/app/receipt_data_custom.js`) sobre
   `GeneratePrinterData.generateSaleDetailsData()`: re-adjunta `uom` y
   `discount` a las líneas agrupadas del X/Z para mantener el output v19.

**Sizing**: en v19 la referencia era 14.5px sobre un recibo DOM de 266px
(ratio ~0.055). En 20 el tamaño lo fija el perfil de impresora (22px sobre
380/512px, ratio ~0.055), así que la densidad v19 se conserva sin pisar el
sizing nativo.

No toca impuestos, pagos ni lógica de servidor.

## Compatibilidad

- Odoo 20.0 (community y enterprise)

## Instalación

```bash
cd /opt/odoo/addons
git clone git@github.com:lfcamarac/pos_receipt_custom.git

# o copiar solo el módulo
git clone git@github.com:lfcamarac/pos_receipt_custom.git /tmp/prc
cp -r /tmp/prc/ts_pos_receipt_custom /opt/odoo/addons/
```

Luego: Apps → **POS Receipt Custom (Tecnosoft)** → Instalar, y verificar
visualmente el recibo (vista web y impresora térmica).

## Estructura

```
pos_receipt_custom/            ← repo
├── README.md
└── ts_pos_receipt_custom/     ← módulo Odoo
    ├── __init__.py
    ├── __manifest__.py
    ├── static/src/app/receipt_data_custom.js   ← patch GeneratePrinterData
    └── views/pos_order_receipt_custom.xml      ← herencias QWeb receipt/*
```

## Versión

- 20.0.1.2.0 (rama `v20/main`)

## Autor

Tecnosoft — https://tecnosoft.dev
