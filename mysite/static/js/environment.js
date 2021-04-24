fn();
function fn(){
    //二次重绘前清空图表
    var main = document.getElementById('Environment');
    var existInstance = echarts.getInstanceByDom(main);
    if(existInstance){
        if(true){
            echarts.dispose(existInstance);
        }
    }
    //初始化echarts实例
    var myChart = echarts.init(document.getElementById('Environment'));
    //设置图表的配置项
    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
        },
        yAxis: {
            type: 'category',
            data: ['living room', 'dormitory', 'bedroom', 'study','other']
        },
        series: [
            {
                type: 'bar',
                data: MyViewVar.var_1
            }
        ]
    };
     myChart.setOption(option);
}