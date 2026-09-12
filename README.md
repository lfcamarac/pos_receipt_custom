# POS Receipt Custom v18

Fix de CSS + logo + footer para el recibo del POS en Odoo 18.

## Problema

Las líneas del recibo se solapan al imprimir desde Windows
(Edge/Chrome), pero NO desde Android (Chrome mobile).

Causa: el navegador Windows renderiza el CSS del recibo con un
line-height distinto al de Android. El template nativo de Odoo no
fuerza el espaciado de línea, así que depende del navegador.

## Solución

CSS explícito que elimina la dependencia del navegador:

- `font-family: 'Courier New', monospace` (rendering uniforme)
- `font-size: 2.6mm` (vs 3mm nativo, más compacto)
- `line-height: 1.0em !important` (sin espacio extra)
- `color: #000 !important` (negro puro)
- Márgenes mínimos (1mm entre secciones)

## Features

- Logo de la empresa (de `res.company.logo`) al inicio
- "powered by tecnosoft" como footer
- Mismo formato compacto y neutro que el template nativo
- No modifica líneas, impuestos, ni pagos
- Compatibilidad: Odoo 18.0 (community + enterprise)
- Compatible con Odoo 19 pendiente validar

## Instalación

```bash
# 1. Copiar a tu addons_path
cp -r pos_receipt_customv18 /opt/odoo/addons/

# 2. Reiniciar Odoo
sudo systemctl restart odoo

# 3. Apps → Actualizar lista → "POS Receipt Custom v18" → Install
# 4. Imprimir un ticket desde el POS
```

## Versión

- 18.0.1.0.0
