{
    'name': 'POS Receipt Custom (Tecnosoft)',
    'version': '20.0.1.2.0',
    'category': 'Tecnosoft/Localización',
    'summary': 'Recibo POS compacto y neutro: interlineado uniforme, footer powered by tecnosoft y detalle de ventas rediseñado.',
    'description': """
Recibo personalizado para el POS de Odoo 20 (Tecnosoft).

- Interlineado uniforme y guards anti-solape (herencia del estilo nativo
  del recibo, mismo fix que en 18/19 contra el montado de líneas).
- Logo proporcional, sin distorsión.
- Footer "powered by tecnosoft" en lugar de "Powered by Odoo".
- Detalle de ventas (X/Z) rediseñado: Ventas / Devoluciones / Pagos /
  Impuestos / Total, con cantidad + UdM y sub-línea de descuento.

100% QWeb + un patch JS sobre GeneratePrinterData. En Odoo 20 el recibo
se renderiza en un iframe a partir del template servidor
point_of_sale.pos_order_receipt (el componente OWL OrderReceipt y el
ReceiptScreen ya no existen), así que la personalización vive en la
herencia QWeb de los templates receipt/* y en el estilo incrustado
pos_order_receipt_style: el CSS del bundle _assets_pos NO llega al iframe.
No toca impuestos, pagos ni lógica de servidor.
""",
    'author': 'Tecnosoft',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_order_receipt_custom.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'ts_pos_receipt_custom/static/src/app/receipt_data_custom.js',
        ],
    },
    'installable': True,
    'license': 'OEEL-1',
    'website': 'https://tecnosoft.dev',
}
