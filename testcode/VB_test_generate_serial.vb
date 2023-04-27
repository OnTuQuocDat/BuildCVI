
Const MainPosition_X    = 15.95
Const MainPosition_Y    = 9.73

Const MainCircleRadius_R  		 = 50
Const Z_AXIS 							 = 17
Const ProductHight					 = 82
Const MarkingOrientation		 = 180

Const Fixture_Rows		= 8
Const Fixture_Columns	= 10
Const Spacing_X				= 12.05
Const Spacing_Y		 		= 	10.06


'**************************************************************************
Const Debug_msgbox_active    	= 0
Const lmosMORootId						= 100

Const Pi    = 3.1415926535897932384626433832795
'*************************************************************************
Dim a1
Dim a2
Dim a3
Dim a4
Dim a5
Dim a6
Dim serial_string
Dim lastLine
Dim objFso
Dim objFile
Dim index As Integer

Set objFso = CreateObject("Scripting.FileSystemObject")


Sub LaserMarker_ScriptBegin ()

  Dim mo_Data
  Dim mo_MainCircleRadius
  Dim sp
  Dim wrad
  Dim Angle
  Dim dActPos
  Dim Myaxis
	
  If Debug_msgbox_active=1 Then
		'Set mo_MainCircleRadius = lasermarker.drawing.getmosbyname("MainCircleRadius").item(1)
		'Set sp = mo_MainCircleRadius.sizepos
		'Set MyAxis = LaserMarker.Axis
		'sp.x = MainCirclePosition_X
		'sp.y = MainCirclePosition_Y
		'sp.width = 2*MainCircleRadius_R
		'sp.height = sp.width
		'mo_MainCircleRadius.sizepos = sp
	Else 
		Set mo_MainCircleRadius = lasermarker.drawing.getmosbyname("Main").item(1)
		Set sp = mo_MainCircleRadius.sizepos
		Set MyAxis = LaserMarker.Axis
		sp.x = 0.1
		sp.y = 0.1
		sp.width = 0.1
		sp.height = sp.width
		mo_MainCircleRadius.sizepos = sp
  End If

	
	Set mo_Data = lasermarker.drawing.getmosbyname("Data").item(1)
	
	Set sp = mo_Data.sizepos
	
	Set MyAxis = LaserMarker.Axis
	
	'Hight = MyAxis.GetPos(Z_AXIS, True)
	'If Hight<> ProductHight Then
		'MyAxis.NewPos Z_AXIS, ProductHight,True
		'.MoveAxes
	'End If

	Dim text1
	Dim i
	Dim j
	Dim k
	Dim test		
	
	
	text1 = mo_Data
	decode(text1)
	
	k = 0
        'Đọc nội dung bắt đầu trong file temp txt
        Read_final_serial_from_txt()
        find_index()
		For i = 0 To Fixture_Rows - 1
			For j = 0 To Fixture_Columns	- 1
				sp.angle = MarkingOrientation
				sp.x = MainPosition_X + i*Spacing_X
				sp.y = MainPosition_Y + j*Spacing_Y
				
				'Read data from txt file to print Value 
                Generate_serial()
                serial_string = 123

				Mo_Data.Value = "S"&serial_string
				k = k + 1

				lasermarker.scriptutils.message " "			 'htn
				lasermarker.scriptutils.message "Ban dang khac san pham o vi tri hang " & i + 1 & " cot " & j + 1'htn
				lasermarker.scriptutils.message "Toa do x = " & sp.x	'htn
				lasermarker.scriptutils.message "Toa do y = " & sp.y	'htn
				lasermarker.scriptutils.message " "	'htn

		
				mo_Data.sizepos = sp
				'mo_Data.mark


				'Do
				'Loop While lasermarker.waitoniobit("ShutterOpen",0,10) = True

				'lasermarker.synchronize
				
				If Debug_msgbox_active=1 Then
					msgbox "Press F5 in MarkingArea Window" & vbCrLf & " Loop Number: " & i & vbCrLf & "Select 'OK' to continue"
				End If
			Next		
		Next
lasermarker.scriptutils.message "Ban dang khac tong cong " & i * j & " con hang. Qua trinh khac ma da hoan tat"

End Sub

Function find_index()
    'Find index of lastLine of serial file
    Dim text As String = File.ReadAllText("test_generate_serial.txt")
    index = text.IndexOf(lastLine)
    If index >= 0 Then
        msgbox "OK index"
    Else
    msgbox "Cannot find the index for this serial in file"

End Sub



Function Generate_serial()
    'Use index to khắc 80 con tiếp theo
    Set objFile = objFso.OpenTextFile("test_generate_serial.txt")
    index = index + 1
	'Tìm nội dung text của index thứ i
	objFile(3)


End Sub

Function Read_final_serial_from_txt()
    Set objFile  = objFso.OpenTextFile("temp.txt",1)
    Do Until objFile.AtEndOfStream 
        lastLine = objFile.ReadLine
    Loop
    objFile.Close
End Sub


Function decode(txt) 
	Dim txt1,txt2,txt3,txt4,txt5,txt6
				txt1=Mid(txt,1,1)
				txt2=Mid(txt,2,1)
				txt3=Mid(txt,3,1)
				txt4=Mid(txt,4,1)
				txt5=Mid(txt,5,1)
				txt6=Mid(txt,6,1)
			
				a1 = asc(txt1)
				a2 = asc(txt2)
				a3 = asc(txt3)
				a4 = asc(txt4)
				a5 = asc(txt5)
				a6 = asc(txt6) 
			
End Function



