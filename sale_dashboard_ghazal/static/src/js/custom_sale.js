/** @odoo-module **/
//import { registry } from '@web/core/registry';
//import { Dialog } from "@web/core/dialog/dialog";
//
//const { Component } = owl;
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";
import { onWillStart, useState, onWillUpdateProps, Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
console.log('Hi ghazal %',Component)

class CustomSale extends Component {
    // Override the method to handle the click
    async triggerWizard() {
            console.log('triggerWizard');
            // Use jsonrpc or any other necessary Odoo RPC call here if needed.
             this.env.services.action.doAction({
                name: _t("Sale Wizard"),
                type: 'ir.actions.act_window',
                res_model: 'custom.sale.wizard',
                view_mode: 'form',
                views: [[false, 'list'], [true, 'form']],
                target: 'new',
            });
        }

    setup() {
    console.log('Hi 1')

     this.action = useService("action");
     onWillStart(async () => {
			console.log('Hi 2')
//             this.triggerWizard();
		});
//		onMounted(() => {
//                  this.triggerWizard();;
//               });

    }
//    onAppClick(app) {
//        if (app.xmlid === "sale.sale_menu_root") {
//            console.log("Sales icon clicked via AppSwitch component!");
//        }
//        // Call the parent method to maintain normal behavior
//        super.onAppClick(app);
//    }

}

// Register the customized AppSwitch
CustomSale.template = "CustomSale";
registry.category("actions").add("custom_sale", CustomSale);
