//  KeeChaw
//  2022.09.16

$(function () {
    map();
    function map() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('china'));
var data = [
     {name: '{{content[2][0]}}', value: '{{content[2][1]}}/2'},
     {name: '{{content[3][0]}}', value: '{{content[3][1]}}/2'},
     {name: '{{content[4][0]}}', value: '{{content[4][1]}}/2'},
     {name: '{{content[5][0]}}', value: '{{content[5][1]}}/2'},
     {name: '{{content[6][0]}}', value: '{{content[6][1]}}/2'},
     {name: '{{content[7][0]}}', value: '{{content[7][1]}}/2'},
     {name: '{{content[8][0]}}', value: '{{content[8][1]}}/2'},
     {name: '{{content[9][0]}}', value: '{{content[9]}}/2'},
     {name: '{{content[10][0]}}', value: '{{content[10][1]}}/2'},
     {name: '{{content[11][0]}}', value: '{{content[11][1]}}/2'},
     {name: '{{content[12][0]}}', value: '{{content[12][1]}}/2'},
     {name: '{{content[13][0]}}', value: '{{content[13][1]}}/2'},
     {name: '{{content[14][0]}}', value: '{{content[14][1]}}/2'},
     {name: '{{content[15][0]}}', value: '{{content[15][1]}}/2'},
     {name: '{{content[16][0]}}', value: '{{content[16][1]}}/2'},
     {name: '{{content[17][0]}}', value: '{{content[17][1]}}/2'},
     {name: '{{content[18][0]}}', value: '{{content[18][1]}}/2'},
     {name: '{{content[19][0]}}', value: '{{content[19][1]}}/2'},
     {name: '{{content[20][0]}}', value: '{{content[20][1]}}/2'},
     {name: '{{content[21][0]}}', value: '{{content[21][1]}}/2'},
     {name: '{{content[22][0]}}', value: '{{content[22][1]}}/2'},
     {name: '{{content[23][0]}}', value: '{{content[23][1]}}/2'},
     {name: '{{content[24][0]}}', value: '{{content[24][1]}}/2'},
     {name: '{{content[25][0]}}', value: '{{content[25][1]}}/2'},
     {name: '{{content[26][0]}}', value: '{{content[26][1]}}/2'},
     {name: '{{content[27][0]}}', value: '{{content[27][1]}}/2'},
     {name: '{{content[28][0]}}', value: '{{content[28][1]}}/2'},
     {name: '{{content[29][0]}}', value: '{{content[29][1]}}/2'},
     {name: '{{content[30][0]}}', value: '{{content[30][1]}}/2'},
     {name: '{{content[31][0]}}', value: '{{content[31][1]}}/2'},
     {name: '{{content[32][0]}}', value: '{{content[32][1]}}/2'}
];
var geoCoordMap = {
        '四川':[104.06667,30.66667],
        '海南':[110.35000,20.01667],
        '广东':[113.23333,23.16667],
        '西藏':[91.00000,30.60000],
        '内蒙古':[111.670801, 41.818311],
        '上海':[121.55333,31.20000],
        '吉林':[125.35000,43.88333],
        '北京': [116.41667,39.91667],
        '福建':[118.30000,26.08333],
        '山东':[117.000923, 36.675807],
        '天津':[117.20000,39.13333],
        '黑龙江':[127.63333,47.75000],
        '广西':[108.320004, 22.82402],
        '辽宁':[123.38333,41.80000],
        '陕西':[108.95000,34.26667],
        '贵州':[106.71667,26.56667],
        '云南':[102.73333,25.05000],
        '河南':[113.65000,34.76667],
        '青海':[96.75000,36.56667],
        '重庆':[106.45000, 29.56667],
        '江西':[115.90000,28.68333],
        '新疆':[87.68333,43.76667],
        '江苏':[119.78333,32.05000],
        '湖南':[113.00000,28.21667],
        '浙江':[120.20000,30.26667],
        '山西':[112.53333,37.86667],
	    '河北':[115.48333,38.03333],
	    '甘肃':[103.73333,36.03333],
	    '湖北':[114.298572, 30.584355],
	    '宁夏':[106.26667,37.46667],
	    '安徽':[117.283042, 31.86119]
};
var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option = {
    tooltip : {
        trigger: 'item',
		formatter: function (params) {
              if(typeof(params.value)[2] == "undefined"){
              	return params.name + ' : ' + params.value;
              }else{
              	return params.name + ' : ' + params.value[2];
              }
            }
    },
  
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        roam: false,//禁止其放大缩小
        itemStyle: {
            normal: {
                areaColor: '#4c60ff',
                borderColor: '#002097'
            },
            emphasis: {
                areaColor: '#293fff'
            }
        }
    },
    series : [
        {
            name: '消费金额',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(data),
            symbolSize: function (val) {
                return val[2] / 15;
            },
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: false
                },
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#ffeb7b'
                }
            }
        }
		
    ]
};
		
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

})

