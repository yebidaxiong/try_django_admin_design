(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5b5a9f60"],{"0bab":function(e,t,a){"use strict";a.r(t);var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"VideoLiveStream"},[a("el-row",[a("el-col",{attrs:{span:4}},[a("div",{staticClass:"operate",attrs:{id:"operate"}},[a("el-row",[a("span",{staticClass:"label"},[e._v("监控点编号:")])]),a("el-row",[a("el-input",{attrs:{id:"cameraIndexCode",placeholder:"请输入监控点编号:",size:"small"},model:{value:e.input,callback:function(t){e.input=t},expression:"input"}})],1),a("el-row",[a("el-button",{staticClass:"btn",attrs:{id:"startPreview",size:"small",type:"danger"}},[e._v("预览")]),a("el-button",{staticClass:"btn",attrs:{id:"stopAllPreview",size:"small",type:"danger"}},[e._v("停止全部预览")])],1),a("el-row",[a("el-button",{attrs:{type:"danger",size:"small"},on:{click:function(t){e.table=!0}}},[e._v("选择摄像头")])],1)],1)]),a("el-col",{attrs:{span:20}},[a("div",{staticClass:"playWnd",attrs:{id:"playWnd"}})])],1),a("div",[a("el-drawer",{attrs:{title:"当前在线摄像头",visible:e.table,direction:"ltr",size:"30%"},on:{"update:visible":function(t){e.table=t}}},[a("el-row",[a("el-table",{attrs:{data:e.gridData}},[a("el-table-column",{attrs:{type:"selection"}}),a("el-table-column",{attrs:{property:"CameraName",label:"摄像头名称",width:"150"}}),a("el-table-column",{attrs:{property:"CameraCode",label:"摄像头编号",width:"150"}}),a("el-table-column",{attrs:{property:"category",label:"所属区域"}})],1)],1),a("el-row",[a("el-button",{attrs:{type:"primary"}},[e._v("预览")])],1)],1)],1)],1)},r=[],o={name:"VideoLiveStream",components:{},data:function(){return{input:"",table:!1,dialog:!1,loading:!1,gridData:[{CameraName:"焦炉东",CameraCode:"JL_01",category:"焦炉作业区"},{CameraName:"焦炉西",CameraCode:"JL_02",category:"焦炉作业区"},{CameraName:"回收东",CameraCode:"HS_01",category:"回收作业区"},{CameraName:"回收西",CameraCode:"HS_02",category:"回收作业区"}],formLabelWidth:"80px",timer:null,swfHeight:"",swfWidth:"",initparam:{appKey:"xxxxx",secret:"xxxxxxx",apiIp:"xxx.xxx.xxx",apiPort:8099,layout:"1x1"},pointCode:"xxxxxxx",pubKey:"",oWebControl:null,WebControl:null}},methods:{}},i=o,n=(a("ca67"),a("2877")),s=Object(n["a"])(i,l,r,!1,null,"0f33acd9",null);t["default"]=s.exports},1637:function(e,t,a){},ca67:function(e,t,a){"use strict";var l=a("1637"),r=a.n(l);r.a}}]);
//# sourceMappingURL=chunk-5b5a9f60.08802de3.js.map