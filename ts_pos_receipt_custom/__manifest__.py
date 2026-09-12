{
    'name': 'POS Receipt Custom (Tecnosoft)',
    'version': '18.0.1.1.0',
    'category': 'Tecnosoft/Localización',
    'summary': 'Recibo POS compacto y neutro: interlineado uniforme (fix overlap Windows), footer powered by tecnosoft.',
    'description': """
Recibo personalizado para el POS de Odoo 18.

- CSS uniforme (monospace + line-height fijo): corrige el solapado
  de líneas al imprimir desde Windows.
- Formato compacto y neutro: aprovecha mejor el espacio de impresión.
- Footer "powered by tecnosoft" en lugar de "Powered by Odoo".
- El logo del recibo es el nativo (ReceiptHeader usa res.company.logo).

100% client-side: hereda el componente OWL point_of_sale.OrderReceipt
y añade CSS al bundle point_of_sale._assets_pos. No toca impuestos,
pagos ni lógica de servidor.
""",
    'author': 'Tecnosoft',
    'depends': ['point_of_sale'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'ts_pos_receipt_custom/static/src/**/*',
        ],
    },
    'installable': True,
    'license': 'OEEL-1',
    'website': 'https://tecnosoft.dev',
}
