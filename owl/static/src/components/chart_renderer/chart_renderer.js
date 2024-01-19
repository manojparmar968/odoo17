/** @odoo-module **/

import { registry } from "@web/core/registry";
import { loadJS } from "@web/core/assets";
const { Component, onWillStart, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup(){
        this.chartRef = useRef("chart")
        onWillStart(async ()=>{
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js")
        })

        onMounted( ()=>this.renderChart())
    }

    renderChart(){
        new Chart(this.chartRef.el,
            {
                type: this.props.type,//'line',//'bar',
                data: {
                    //this show the line simple
                    // labels: data.map(row => row.year),
                    // datasets: [
                    //     {
                    //     label: 'Acquisitions by year',
                    //     data: data.map(row => row.count)
                    //     }
                    // ]
                    //this show the line color with look smart
                    labels: [
                        'Red',
                        'Blue',
                        'Yellow'
                    ],
                    datasets: [
                    {
                        label: 'My First Dataset',
                        data: [300, 50, 100],
                        // backgroundColor: [
                        //   'rgb(255, 99, 132)',
                        //   'rgb(54, 162, 235)',
                        //   'rgb(255, 205, 86)'
                        // ],
                        hoverOffset: 4
                    },
                    {
                        label: 'My Second Dataset',
                        data: [100, 40, 150],
                        hoverOffset: 4
                    }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                      legend: {
                        position: 'bottom',//'top',
                      },
                      title: {
                        display: true,
                        text: this.props.title,
                        position: 'bottom',
                      }
                    }
                },
            }
        );
    }
}

ChartRenderer.template = "owl.ChartRenderer"