import QtQuick 2.12
import QtQuick.Window 2.13
import QtQuick.Controls 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0
import QtQuick 2.15

Window {
	id : root
	width: 800
	maximumWidth : 800
	minimumWidth : 800
    height: 600
	maximumHeight : 600
	minimumHeight : 600
	title:"mancing"
	color : "#4590BF"
    visible: true
    //flags: Qt.WindowMaximized //Qt.Dialog
	
	property color plotColordown : "blue"
	onPlotColordownChanged: down_canv.requestPaint()
	
	
	property color plotColorup : "blue"
	onPlotColorupChanged: up_canv.requestPaint()
	
	
	property color plotColorleft : "blue"
	onPlotColorleftChanged: left_canv.requestPaint()
	
	
	property color plotColorright : "blue"
	onPlotColorrightChanged: right_canv.requestPaint()
	
	
	
	
	
	Rectangle{
		
		anchors.horizontalCenter: parent.horizontalCenter
		y:140
		width : parent.width
		height : 480
		color : "#204F8C"
		border.color: "transparent"
		border.width: 0
		
		
		Image{
		id : tuna1
		x : 40
		y : 10
		width : 150
		height : 120
		source : "tuna.png"
		mirror : true
		
		
		
		}
		
		
		
		
		}
	
	
	
	Rectangle{
		
		anchors.horizontalCenter: parent.horizontalCenter
		y:20
		width : 420
		height : 120
		color : "#122e55"
		border.color: "white"
		border.width: 5
		visible: false
	
	Text{
		
		anchors.horizontalCenter: parent.horizontalCenter
		y: 5
		//anchors.verticalCenter: parent.verticalCenter
		width : 400
		text : "Ardumeka PyGame Joystick Benchmark"
		wrapMode: Text.WordWrap 
		horizontalAlignment: Text.AlignHCenter//Text.AlignJustify
		color : "white"
		font.pixelSize : 25
	}
	
	Text{
		
		anchors.horizontalCenter: parent.horizontalCenter
		y: 80
		//anchors.verticalCenter: parent.verticalCenter
		width : 400
		text : "By : Muhammad Husni"
		wrapMode: Text.WordWrap 
		horizontalAlignment: Text.AlignHCenter//Text.AlignJustify
		color : "white"
		font.pixelSize : 20
	}
	
	
	
	}
	
	Rectangle {
	x:10
	y:170
	color : "transparent"
	
	Rectangle{
		//L2
		id : l2
		x: 60
		y: 140
		width : 210
		height : 50
		color : "#d84860"
		border.color: "white"
		border.width: 5
	visible: false
	
		Text{
		y : 10
		width : parent.width
		horizontalAlignment: Text.AlignHCenter
		text : "L2"
		color : "white"
		font.pixelSize : 24
	}
	
	}
	
	Rectangle{
		//L1
		id : l1
		x: 60
		y: 210
		width : 210
		height : 50
		color : "#122e55"
		border.color: "white"
		border.width: 5
	visible: false
	
		Text{
		y : 10
		width : parent.width
		horizontalAlignment: Text.AlignHCenter
		text : "L1"
		color : "white"
		font.pixelSize : 24
	}
	
	}
	
	
	
	
	Rectangle{
		//atas
		x: 130
		y: 280
		width : 70
		height : 70
		color : "transparent"
		border.color: "transparent"
		border.width: 5
		
		visible: false
		
		Canvas {
		id : up_canv
        width: parent.width ; height: parent.height
        anchors.centerIn: parent
        onPaint: {
            var ctx = getContext("2d")

            // the equliteral triangle
            ctx.beginPath();
            ctx.moveTo((width )/2, 10);
            ctx.lineTo(10, 60);
            ctx.lineTo(width - 10 , 60);
            ctx.closePath();

            // outline
            ctx.lineWidth = 10;

            // outline color
            ctx.strokeStyle = 'white';
            ctx.stroke();

            // fill color
            ctx.fillStyle = plotColorup;
            ctx.fill();
        }
    
	
	
	}
		
	}
	
	Rectangle{
		//kiri
		x: 60
		y: 350
		width : 70
		height : 70
		rotation : -90
		color : "transparent"
		
		
		
		
		Canvas {
		id : left_canv
        width: parent.width ; height: parent.height
        anchors.centerIn: parent
        onPaint: {
            var ctx = getContext("2d")

            // the equliteral triangle
            ctx.beginPath();
            ctx.moveTo((width )/2, 10);
            ctx.lineTo(10, 60);
            ctx.lineTo(width - 10 , 60);
            ctx.closePath();

            // outline
            ctx.lineWidth = 10;

            // outline color
            ctx.strokeStyle = 'white';
            ctx.stroke();

            // fill color
            ctx.fillStyle = plotColorleft;
            ctx.fill();
        }
    
	
	
	}
		
		
	}
	
	Rectangle{
		//kanan
		x: 200
		y: 350
		width : 70
		height : 70
		color : "transparent"
		border.color: "transparent"
		rotation : 90
		
		
		
		
		Canvas {
		id : right_canv
        width: parent.width ; height: parent.height
        anchors.centerIn: parent
        onPaint: {
            var ctx = getContext("2d")

            // the equliteral triangle
            ctx.beginPath();
            ctx.moveTo((width )/2, 10);
            ctx.lineTo(10, 60);
            ctx.lineTo(width - 10 , 60);
            ctx.closePath();

            // outline
            ctx.lineWidth = 10;

            // outline color
            ctx.strokeStyle = 'white';
            ctx.stroke();

            // fill color
            ctx.fillStyle = plotColorright;
            ctx.fill();
        }
    
	
	
	}
		
		
		
		
	}
	
	Rectangle{
		//bawah
		x: 130
		y: 420
		width : 70
		height : 70
		color : "transparent"
		rotation  : 180
	
		visible: false
		
		
		
		Canvas {
		id : down_canv
        width: parent.width ; height: parent.height
        anchors.centerIn: parent
		
		
        onPaint: {
            var ctx = getContext("2d")

            // the equliteral triangle
            ctx.beginPath();
            ctx.moveTo((width )/2, 10);
            ctx.lineTo(10, 60);
            ctx.lineTo(width - 10 , 60);
            ctx.closePath();

            // outline
            ctx.lineWidth = 10;

            // outline color
            ctx.strokeStyle = 'white';
            ctx.stroke();

            // fill color
            ctx.fillStyle = plotColordown;
            ctx.fill();
        }
    
	
	
	}
		
	
	
	
	}
	
	Rectangle {
	 id : axis1
     width: 50
     height: 50
     color: "#122e55"
     border.color: "white"
     border.width: 2
     radius: width*0.5
	 visible: false
    
}
	
	
	}
	
	
	
	
	
	Rectangle {
	x:450
	y:50
	color : "transparent"
	
	Rectangle{
		//R2
		id : r2
		x: 60
		y: 140
		width : 210
		height : 50
		color : "#122e55"
		border.color: "white"
		border.width: 5
	visible: false
		Text{
		y : 10
		width : parent.width
		horizontalAlignment: Text.AlignHCenter
		text : "R2"
		color : "white"
		font.pixelSize : 24
	}
	
	
	}
	
	Rectangle{
		//R1
		id : r1
		x: 60
		y: 210
		width : 210
		height : 50
		color : "#d84860"
		border.color: "white"
		border.width: 5
		visible: false
		Text{
		y : 10
		width : parent.width
		horizontalAlignment: Text.AlignHCenter
		text : "R1"
		color : "white"
		font.pixelSize : 24
	}
		
		
	}
	
	
	
	Rectangle{
		//1
		id : button1
		x: 130
		y: 280
		width : 70
		height : 70
		color : "#d84860"
		border.color: "white"
		border.width: 5
		visible: false
		Text{
		x: (parent.width-10)/2
		y: (parent.height-30)/2
		text : "1"
		color : "white"
		font.pixelSize : 24
	}
		
		
	}
	
	Rectangle{
		//4
		id : button4
		x: 100
		y: 450
		width : 210
		height : 70
		color : "#122e55"
		border.color: "white"
		border.width: 5
	
	Text{
		x: 15
		y: 15
		text : "MANCING MANIA"
		color : "white"
		font.pixelSize : 24
	}
	
	
	}
	
	Rectangle{
		//2
		id : button2
		x: 200
		y: 350
		width : 70
		height : 70
		color : "#122e55"
		border.color: "white"
		border.width: 5
	visible: false
	Text{
		x: (parent.width-10)/2
		y: (parent.height-30)/2
		text : "2"
		color : "white"
		font.pixelSize : 24
	}
	
	}
	
	Rectangle{
		//3
		id : button3
		x: 130
		y: 420
		width : 70
		height : 70
		color : "#d84860"
		border.color: "white"
		border.width: 5
	visible: false
	
	Text{
		x: (parent.width-10)/2
		y: (parent.height-30)/2
		text : "3"
		color : "white"
		font.pixelSize : 24
	}
	
	
	}
	
	Rectangle {
	 id : axis2
	 x : -30
	 y : 360
     width: 50
     height: 50
     color: "#122e55"
     border.color: "white"
     border.width: 2
     radius: width*0.5
    visible: false
}
	
	
	
	
	}
	
	
	Image{
		id : kapal
		x : 40
		y : 10
		width : 120
		height : 140
		source : "mancing.png"
		
		Rectangle{
		id : rope
		x: 0
		y: 0
		width : 10
		height : 10
		color : "white"
		rotation  : 0
		
		}
		
	}

	Text{
		id : score
		x: 350
		y: 540
		text : "SCORE : 000"
		color : "white"
		font.pixelSize : 24
	}
	
	
	Text{
		id : coordinat
		anchors.horizontalCenter: parent.horizontalCenter
		y: 500
		//anchors.verticalCenter: parent.verticalCenter
		width : 400
		text : ""
		wrapMode: Text.WordWrap 
		horizontalAlignment: Text.AlignHCenter//Text.AlignJustify
		color : "white"
		font.pixelSize : 20
	}
	
	Text{
		id : delta
		anchors.horizontalCenter: parent.horizontalCenter
		y: 450
		//anchors.verticalCenter: parent.verticalCenter
		width : 400
		text : ""
		wrapMode: Text.WordWrap 
		horizontalAlignment: Text.AlignHCenter//Text.AlignJustify
		color : "white"
		font.pixelSize : 20
	}
	
	
	
	
	Timer{
		id: gui_timer
		interval: 50
		repeat: true
		running: true
		onTriggered: {
			plotColorup = backend.up_color()
			plotColordown = backend.down_color()
			plotColorleft = backend.left_color()
			plotColorright = backend.right_color()
			
			button1.color = backend.button1_color()
			button2.color = backend.button2_color()
			button3.color = backend.button3_color()
			button4.color = backend.button4_color()
			l1.color = backend.button_L1_color()
			l2.color = backend.button_L2_color()
			r1.color = backend.button_R1_color()
			r2.color = backend.button_R2_color()
			axis1.x = parseFloat(backend.analog1_x()) + 300 
			axis1.y = parseFloat(backend.analog1_y()) + 360
			axis2.x = parseFloat(backend.analog2_x()) + -30
			axis2.y = parseFloat(backend.analog2_y()) + 360
			
			axis1.color = backend.analog1_color()
			axis2.color = backend.analog2_color()
			
			kapal.x = backend.ship_pos()
			
			tuna1.x = backend.fish1_x()
			tuna1.y = backend.fish1_y()
			
			if((tuna1.x) < 0){
			tuna1.x = 0
			}
			
			
			
			rope.height = backend.rope_length()
			score.text = "SCORE : " + backend.current_score()
			coordinat.text = tuna1.x + "," + tuna1.y + "," + kapal.x + ","  + rope.height 
			delta.text = (parseInt(backend.ship_pos()) - parseInt(backend.fish1_x())) + "," + (parseInt(backend.rope_length()) - parseInt(backend.fish1_y()))
		
			
		}
		
	}
	
	
	
	
	
}













