/** @odoo-module **/

import { registry } from '@web/core/registry';
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { useService } from "@web/core/utils/hooks";

const { onWillStart } = owl

class ResPartnerKanbanController extends KanbanController {
    setup() {
        super.setup();
        console.log("Working kanban");
        this.action = useService("action")
        this.orm = useService("orm")

        onWillStart(async ()=>{
            this.customerLocations = await this.orm.readGroup("res.partner", [], ['state_id'], ['state_id'])
            console.log(this.customerLocations)
        })
    }

    openSalesView(){
        console.log("Working sale kanban");
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Customer Sales",
            res_model: "sale.order",
            views: [[false, "list"], [false, "form"]]
        })
    }

    selectLocations(state){
        const id = state[0]
        const name = state[1]
        // setDomainParts is not working in odoo 17
        this.env.searchModel.setDomainParts({
            state: {
                domain: [['state_id', '=', id]],
                facetLabel: name
            }
        })
    }
};

ResPartnerKanbanController.template = "owl_inheritance.ResPartnerKanbanView";

export const resPartnerKanbanView = {
    ...kanbanView,
    Controller: ResPartnerKanbanController,
    buttonTemplate: "owl_inheritance.ResPartnerKanbanView.Buttons",
};

registry.category("views").add("res_partner_kanban_view", resPartnerKanbanView);