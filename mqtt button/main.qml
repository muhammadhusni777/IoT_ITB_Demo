import QtQuick 2.12
import QtQuick.Window 2.13
import QtQuick.Controls 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0


Window {
	id : root
	width: 400
	maximumWidth : width
	minimumWidth : width
    height: 400
	maximumHeight : height
	minimumHeight : height
	title:"membuat windows"
	color : "#000080"
    visible: true
    flags: Qt.Dialog
	
	
	Text{
	x:10
	y:5
	width: 400
	text : " IoT Button"
	color : "white"
	font.pixelSize : 24
	verticalAlignment: Text.AlignVCenter
	}
	
	
	Text{
	id : text1
	x:10
	y:50
	text : ""
	color : "white"
	font.pixelSize : 24
	visible : true
	}
	
	Button {
		id: button1
		anchors.horizontalCenter: parent.horizontalCenter
		y :200
		width : 150
		height : 150
		text: "LAMPU"
		checkable : true
		checked : true
		palette {
        button: "#00FF00"
		buttonText: "black"
		}
		
		onClicked:{
			if(button1.checked == true){
				backend.button1("OFF")
			}
			
			if(button1.checked == false){
				backend.button1("ON")
			}
		}
		
	}
	
	
	Timer{
		id:tmgauge
		interval: 50
		repeat: true
		running: true
		onTriggered: {
		text1.text = backend.test_message()
		
		}
	}
	
	
	
}













