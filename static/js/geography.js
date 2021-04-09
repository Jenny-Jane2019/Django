
fn();
//生成柱状图
function fn(){
    //二次重绘前清空图表
    var main = document.getElementById('Geographic');
    var existInstance = echarts.getInstanceByDom(main);
    if(existInstance){
        if(true){
            echarts.dispose(existInstance);
        }
    }
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('Geographic'));
    // 指定图表的配置项和数据

var option = {
    tooltip : {//鼠标悬浮时显示的提示框
        trigger: 'item',//触发类型,'item' 数据项图形触发
        formatter: function(params) {//分别显示多个值
             var res = params.name+'<br/>';
             var my_series = option.series;
             for (var i = 0; i < my_series.length; i++) {
                for(var j=0;j<my_series[i].data.length;j++){
                    if(my_series[i].data[j].name==params.name){
                        res+=' '+my_series[i].name +' : '+my_series[i].data[j].value+' people'+'</br>';
                    }
                }
             }
             return res;
            }
    },
    dataRange: {
        min: 0,
        max: 10,
        x: 'left',
        y: 'bottom',
        text:['high','low'],           // 文本，默认为数值文本
        calculable : true,
        inRange: {
            color: ['#e0ffff', '#58aaeb'],
            symbolSize: [30, 100]
        }
    },
    roamController: {
        show: true,
        x: 'right',
        mapTypeControl: {
            'china': true
        }
    },
    series : [
        {
            name: 'male',
            type: 'map',
            mapType: 'china',
            // 是否开启鼠标缩放和平移漫游 默认不开启 如果只想要开启缩放或者平移，可以设置成 'scale' 或者 'move' 设置成 true 为都开启
            roam: false,
            // 自定义名称映射
            nameMap: {
                '北京':'Beijing',
                '天津':'Tianjin',
                '上海':'Shanghai',
                '重庆':'Chongqing',
                '河北':'Hebei',
                '河南':'Henan',
                '云南':'Yunnan',
                '辽宁':'Liaoning',
                '黑龙江':'Heilongjiang',
                '湖南':'Hunan',
                '安徽':'Anhui',
                '山东':'Shandong',
                '新疆':'Xinjiang',
                '江苏':'Jiangsu',
                '浙江':'Zhejiang',
                '江西':'Jiangxi',
                '湖北':'Hubei',
                '广西':'Guangxi',
                '甘肃':'Gansu',
                '山西':'Shanxi',
                '内蒙古':'Inner Mongolia',
                '陕西':'Shaanxi',
                '吉林':'Jilin',
                '福建':'Fujian',
                '贵州':'Guizhou',
                '广东':'Guangdong',
                '青海':'Qinghai',
                '西藏':'Tibet',
                '四川':'Sichuan',
                '宁夏':'Ningxia',
                '海南':'Hainan',
                '台湾':'Taiwan',
                '香港':'Hong Kong',
                '澳门':'Macao',
                '南海诸岛':' South China Sea Islands'
            },
            itemStyle:{
                normal:{label:{show:true}},
                emphasis:{label:{show:true}}
            },
            data:[
                {name: 'Beijing',value: MyViewVar.var_2[0]},
                {name: 'Tianjin',value: MyViewVar.var_2[1]},
                {name: 'Shanghai',value: MyViewVar.var_2[2]},
                {name: 'Chongqing',value: MyViewVar.var_2[3]},
                {name: 'Hebei',value: MyViewVar.var_2[4]},
                {name: 'Henan',value: MyViewVar.var_2[5]},
                {name: 'Yunnan',value: MyViewVar.var_2[6]},
                {name: 'Liaoning',value: MyViewVar.var_2[7]},
                {name: 'Heilongjiang',value: MyViewVar.var_2[8]},
                {name: 'Hunan',value: MyViewVar.var_2[9]},
                {name: 'Anhui',value: MyViewVar.var_2[10]},
                {name: 'Shandong',value: MyViewVar.var_2[11]},
                {name: 'Xinjiang',value: MyViewVar.var_2[12]},
                {name: 'Jiangsu',value: MyViewVar.var_2[13]},
                {name: 'Zhejiang',value: MyViewVar.var_2[14]},
                {name: 'Jiangxi',value: MyViewVar.var_2[15]},
                {name: 'Hubei',value: MyViewVar.var_2[16]},
                {name: 'Guangxi',value: MyViewVar.var_2[17]},
                {name: 'Gansu',value: MyViewVar.var_2[18]},
                {name: 'Shanxi',value: MyViewVar.var_2[19]},
                {name: 'Inner Mongolia',value: MyViewVar.var_2[20]},
                {name: 'Shaanxi',value: MyViewVar.var_2[21]},
                {name: 'Jilin',value: MyViewVar.var_2[22]},
                {name: 'Fujian',value: MyViewVar.var_2[23]},
                {name: 'Guizhou',value: MyViewVar.var_2[24]},
                {name: 'Guangdong',value: MyViewVar.var_2[25]},
                {name: 'Qinghai',value: MyViewVar.var_2[26]},
                {name: 'Tibet',value: MyViewVar.var_2[27]},
                {name: 'Sichuan',value: MyViewVar.var_2[28]},
                {name: 'Ningxia',value: MyViewVar.var_2[29]},
                {name: 'Hainan',value: MyViewVar.var_2[30]},
                {name: 'Taiwan',value: MyViewVar.var_2[31]},
                {name: 'Hong Kong',value: MyViewVar.var_2[32]},
                {name: 'Macao',value: MyViewVar.var_2[33]}
            ]
        },
        {
            name: 'female',
            type: 'map',
            mapType: 'china',
            itemStyle:{
                emphasis:{label:{show:true}}
            },
            data:[
                {name: 'Beijing',value: MyViewVar.var_1[0]},
                {name: 'Tianjin',value: MyViewVar.var_1[1]},
                {name: 'Shanghai',value: MyViewVar.var_1[2]},
                {name: 'Chongqing',value: MyViewVar.var_1[3]},
                {name: 'Hebei',value: MyViewVar.var_1[4]},
                {name: 'Henan',value: MyViewVar.var_1[5]},
                {name: 'Yunnan',value: MyViewVar.var_1[6]},
                {name: 'Liaoning',value: MyViewVar.var_1[7]},
                {name: 'Heilongjiang',value: MyViewVar.var_1[8]},
                {name: 'Hunan',value: MyViewVar.var_1[9]},
                {name: 'Anhui',value: MyViewVar.var_1[10]},
                {name: 'Shandong',value: MyViewVar.var_1[11]},
                {name: 'Xinjiang',value: MyViewVar.var_1[12]},
                {name: 'Jiangsu',value: MyViewVar.var_1[13]},
                {name: 'Zhejiang',value: MyViewVar.var_1[14]},
                {name: 'Jiangxi',value: MyViewVar.var_1[15]},
                {name: 'Hubei',value: MyViewVar.var_1[16]},
                {name: 'Jiangxi',value: MyViewVar.var_1[17]},
                {name: 'Gansu',value: MyViewVar.var_1[18]},
                {name: 'Shanxi',value: MyViewVar.var_1[19]},
                {name: 'Inner Mongolia',value: MyViewVar.var_1[20]},
                {name: 'shaanxi',value: MyViewVar.var_1[21]},
                {name: 'Jilin',value: MyViewVar.var_1[22]},
                {name: 'Fujian',value: MyViewVar.var_1[23]},
                {name: 'Guizhou',value: MyViewVar.var_1[24]},
                {name: 'Guangdong',value: MyViewVar.var_1[25]},
                {name: 'Qinghai',value: MyViewVar.var_1[26]},
                {name: 'Tibet',value: MyViewVar.var_1[27]},
                {name: 'Sichuan',value: MyViewVar.var_1[28]},
                {name: 'Ningxia',value: MyViewVar.var_1[29]},
                {name: 'Hainan',value: MyViewVar.var_1[30]},
                {name: 'Taiwan',value: MyViewVar.var_1[31]},
                {name: 'Hong Kong',value: MyViewVar.var_1[32]},
                {name: 'Macao',value: MyViewVar.var_1[33]}
            ]
        }
    ]
};

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);

}