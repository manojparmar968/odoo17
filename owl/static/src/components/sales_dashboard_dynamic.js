/** @odoo-module **/

import { registry } from "@web/core/registry";
import { KpiCardDynamic } from "./kpi_card/kpi_card_dynamic";
import { ChartRendererDynamic } from "./chart_renderer/chart_renderer_dynamic";
import { loadJS } from "@web/core/assets";
import { useService } from '@web/core/utils/hooks';
const { Component, onWillStart, useRef, onMounted, useState } = owl

export class OwlSalesDashboardDynamic extends Component {
    setup(){
        this.state = useState({
            quotations: {
                value: 10,
                percentage: 6,
            },
            period: 90,
        })
        this.orm = useService("orm")

        onWillStart(async ()=>{
            // this.getDates()
            await this.getQuotations()
        })
    }

    async onChangePeriod(){
        console.log(this.state.period);
    }

    // momentsjs is not working odoo 17
    getDates(){
        this.state.current_date = moment().subtract(this.state.period, 'days').format('YYYY-MM-DD')
        this.state.previous_date = moment().subtract(this.state.period * 2, 'days').format('YYYY-MM-DD')
    }

    async getQuotations(){
        let domain = [['state', 'in', ['sent','draft']]]
        // if (this.state.period > 0){
        //     domain.push(['date_order','>',this.state.period])
        // }
        const data = await this.orm.searchCount("sale.order", domain)
        
        this.state.quotations.value = data
    }
}

OwlSalesDashboardDynamic.template = "owl.OwlSalesDashboardDynamic"
OwlSalesDashboardDynamic.components = { KpiCardDynamic, ChartRendererDynamic };

registry.category("actions").add("owl.sales_dashboard_dynamic", OwlSalesDashboardDynamic);