
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

Dim objFso, debugfile
Set objFso = CreateObject("Scripting.FileSystemObject")
debugfile="c:\Sonion\debug.txt" 'name of sorting_Machine file


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
	
	' start from BBBBBB
	a1=66
	a2=66
	a3=66
	a4=66
	a5=66
	a6=66
	
	text1 = mo_Data
	decode(text1)
	
	k = 0
		For i = 0 To Fixture_Rows - 1
			For j = 0 To Fixture_Columns	- 1
				sp.angle = MarkingOrientation
				sp.x = MainPosition_X + i*Spacing_X
				sp.y = MainPosition_Y + j*Spacing_Y
				SN()
				
				Mo_Data.Value = "S"&Chr(a1)&Chr(a2)&Chr(a3)&Chr(a4)&Chr(a5)&Chr(a6)
				k = k + 1

				lasermarker.scriptutils.message " "			 'htn
				lasermarker.scriptutils.message "Ban dang khac san pham o vi tri hang " & i + 1 & " cot " & j + 1'htn
				lasermarker.scriptutils.message "Toa do x = " & sp.x	'htn
				lasermarker.scriptutils.message "Toa do y = " & sp.y	'htn
				lasermarker.scriptutils.message " "	'htn

				'lasermarker.scriptutils.message "Angle ° = " & Angle
				'lasermarker.scriptutils.message "Pos x = " & sp.x
				'lasermarker.scriptutils.message "Pos y = " & sp.y
				'lasermarker.scriptutils.message "  "
		
				mo_Data.sizepos = sp
				'mo_Data.mark
				WriteToFile Date() & " " & Time() & " ROWS " & i &" Column "& j&" " & Mo_Data.Value , debugfile	


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
Function SN() 
			a6 = a6 + 1
			'a6 customize
			If a6 = 69 Or a6 = 73 Or a6 = 79 Or a6 = 81 Or a6 = 85 Then 
				a6 = a6 + 1
			End If
			 
			If a6 = 88 Or a6 = 89 Then
				a6 = 90
			End If

			If a6 >= 91 Then
				a6 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 <> 57 Then
				a6 = 66
				a5 = a5 + 1
			End If


			' a5 customize
			If a5 = 69 Or a5 = 73 Or a5 = 79 Or a5 = 81 Or a5 = 85 Then 
				a5 = a5 + 1
			End If
		
			If a5 = 88 Or a5 = 89 Then
				a5 = 90
			End If

			If a5 >= 91 Then
				a5 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 = 57 And a4 <> 57 Then
				a6 = 66
				a5 = 66
				a4 = a4 + 1
			End If
				
				
			' a4 customize
			If a4 = 69 Or a4 = 73 Or a4 = 79 Or a4 = 81 Or a4 = 85 Then 
				a4 = a4 + 1
			End If
			
			If a4 = 88 Or a4 = 89 Then
				a4 = 90
			End If
			
			If a4 >= 91 Then
				a4 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 = 57 And a4 = 57 And a3 <> 57 Then
				a6 = 66
				a5 = 66
				a4 = 66
				a3 = a3 + 1
			End If
			
			
			'a3 customize
			If a3 = 69 Or a3 = 73 Or a3 = 79 Or a3 = 81 Or a3 = 85 Then 
				a3 = a3 + 1
			End If
			
			If a3 = 88 Or a3 = 89 Then
				a3 = 90
			End If
			
			If a3 >= 91 Then
				a3 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 = 57 And a4 = 57 And a3 = 57 And a2 <> 57 Then
				a6 = 66
				a5 = 66
				a4 = 66
				a3 = 66
				a2 = a2 + 1
			End If


			 'a2 customize
			If a2 = 69 Or a2 = 73 Or a2 = 79 Or a2 = 81 Or a2 = 85 Then 
				a2 = a2 + 1
			End If
			
			If a2 = 88 Or a2 = 89 Then
				a2 = 90
			End If
			
			If a2 >= 91 Then
				a2 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 = 57 And a4 = 57 And a3 = 57 And a2 = 57 And a1 <> 57 Then
				a6 = 66
				a5 = 66
				a4 = 66
				a3 = 66
				a2 = 66
				a1 = a1 + 1
			End If
			
			
			'a1 customize
			If a1 = 69 Or a1 = 73 Or a1 = 79 Or a1 = 81 Or a1 = 85 Then 
				a1 = a1 + 1
			End If
			
			If a1 = 88 Or a1 = 89 Then
				a1 = 90
			End If
			
			If a1 >= 91 Then
				a1 = 48
			End If
			
			If a6 >= 58 And a6 < 66 And a5 = 57 And a5 = 57 And a4 = 57 And a3 = 57 And a2 = 57 And a1 = 57 Then
				a6 = 66
				a5 = 66
				a4 = 66
				a3 = 66
				a2 = 66
				a1 = 66
			End If
 						
End Function

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
Sub WriteToFile (StrText, StrFileName)
  Dim objFileHandle
  Dim p As New Process()
	'if the file exist open it in append mode, otherwise create a new file
	If (objFso.FileExists(strFileName)) Then
		Set ObjFileHandle = objFso.OpenTextFile(strFileName,8)
	Else
		Set ObjFileHandle = objFso.OpenTextFile(strFileName,2,"True")
	End If
	objFileHandle.WriteLine StrText
	'Close debug text file
	objFileHandle.Close()
	'DAQ add exe file
	p.StartInfo.FileName = "C:\\Sonion\\main.exe"
	p.Start()
End Sub 


