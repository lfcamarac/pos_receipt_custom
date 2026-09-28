/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { GeneratePrinterData } from "@point_of_sale/app/utils/printer/generate_printer_data";

// Puerto v19 → v20 del recibo Tecnosoft. En 19 el detalle de ventas se
// heredaba como template OWL (point_of_sale.SaleDetailsReport) sobre los
// datos crudos de get_sale_details; en 20 ese template ya no existe y el
// X/Z sale del QWeb servidor point_of_sale.pos_sale_details_receipt con los
// datos que arma GeneratePrinterData.generateSaleDetailsData().
//
// processData() agrupa los productos por product_id y descarta `uom` y
// `discount`, que el diseño Tecnosoft sí imprimía en v19 (cantidad + UdM y
// sub-línea "Descuento N%"). Este patch los vuelve a adjuntar a las secciones
// sold/refund/cancel para que el QWeb de ts_pos_receipt_custom los pinte
// igual que en v19. El recibo del cliente no necesita patch: su única
// customización (footer "powered by tecnosoft") es solo de plantilla.
//
// Mismo patrón que pos_dual_currency/receipt_data_igtf.js (patch del
// generador + template QWeb que consume extra_data).
patch(GeneratePrinterData.prototype, {
    generateSaleDetailsData(saleDetails) {
        const data = super.generateSaleDetailsData(saleDetails);

        // Adjunta uom/discount del dato crudo a las líneas ya agrupadas.
        // El crudo y el procesado comparten el orden de categorías; dentro
        // de cada categoría se une por nombre de producto (product_id no
        // sobrevive al agrupado de processData).
        const carry = (processedSections, rawSections) => {
            (processedSections || []).forEach((category, index) => {
                const rawCategory = (rawSections || [])[index];
                if (!rawCategory) {
                    return;
                }
                const rawByProduct = new Map(
                    rawCategory.products.map((product) => [
                        product.product_name,
                        { uom: product.uom || false, discount: product.discount || 0 },
                    ])
                );
                for (const line of category.products) {
                    const extra = rawByProduct.get(line.name);
                    line.uom = extra?.uom || false;
                    line.discount = extra?.discount || 0;
                }
            });
        };

        carry(data.extra_data.sold, saleDetails.products);
        carry(data.extra_data.refund, saleDetails.refund_products);
        carry(data.extra_data.cancel, saleDetails.cancelled_products);
        return data;
    },
});
