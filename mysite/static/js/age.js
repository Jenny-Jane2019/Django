fn();
function fn(){
    //二次重绘前清空图表
    var main = document.getElementById('Age');
    var existInstance = echarts.getInstanceByDom(main);
    if(existInstance){
        if(true){
            echarts.dispose(existInstance);
        }
    }
    //初始化echarts实例
    var myChart = echarts.init(document.getElementById('Age'));

    //设置图表的配置项
    var option = {
        tooltip : {//鼠标悬浮时显示的提示框
            trigger: 'item'
        },
        legend:{
            data: ['Female', 'Male'],
            left:'right'
        },
        xAxis: {
            name: 'years old',
            type: 'category',
            data: ['<20', '20-30', '30-40', '40-50', '>50']
        },
        yAxis: {
            name: 'people',
            type: 'value',
            itemStyle:{
                normal:{label:{show:true}},
                emphasis:{label:{show:true}}
            }
        },
        series: [
        {
            name: 'Female',
            type: 'bar',
            data: MyViewVar.var_1,
        },
        {
            name: 'Male',
            type: 'bar',
            data: MyViewVar.var_2,
        },
        {
            name: '占比',
            type: 'pie',
            center: ['70%', '35%'],
            radius: '28%',
            z: 100,
            label: {
                    formatter: '{b}: ({d}%)'
            },
            data: [
                    {name: 'Female', value: MyViewVar.var_3},
                    {name: 'Male', value: MyViewVar.var_4},
            ]
        }
    ]
    };
     myChart.setOption(option);
}