fn();
function fn(){
    //二次重绘前清空图表
    var main = document.getElementById('Phone');
    var existInstance = echarts.getInstanceByDom(main);
    if(existInstance){
        if(true){
            echarts.dispose(existInstance);
        }
    }
    //初始化echarts实例
    var myChart = echarts.init(document.getElementById('Phone'));
    //设置图表的配置项
    var option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left',
        },
        series: [
            {
                name: 'Phone Type',
                type: 'pie',
                radius: '50%',
                data: [
                    {value: MyViewVar.var_1[0], name: 'Huawei'},
                    {value: MyViewVar.var_1[1], name: 'Iphone'},
                    {value: MyViewVar.var_1[2], name: 'Samsung'},
                    {value: MyViewVar.var_1[3], name: 'Oppo'},
                    {value: MyViewVar.var_1[4], name: 'Vivo'},
                    {value: MyViewVar.var_1[5], name: 'Other'}
                ],
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };
     myChart.setOption(option);
}