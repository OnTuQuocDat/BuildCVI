
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
	
  

    Dim text1
    Dim i
    Dim j
    Dim k
    Dim test		

    Read_final_serial_from_txt()
    find_index()
	
End Sub	


Function find_index()
    'Find index of lastLine of serial file
    Dim text As String = File.ReadAllText("test_generate_serial.txt")
    index = text.IndexOf(lastLine)
    If index >= 0 Then
        msgbox "OK index"
    Else
    msgbox "Cannot find the index for this serial in file"

End Function



Function Generate_serial()
    'Use index to khắc 80 con tiếp theo
    Set objFile = objFso.OpenTextFile("test_generate_serial.txt")
    index = index + 1
	'Tìm nội dung text của index thứ i
	objFile(3)

End Function

Function Read_final_serial_from_txt()
    Set objFile  = objFso.OpenTextFile("temp.txt",1)
    Do Until objFile.AtEndOfStream 
        lastLine = objFile.ReadLine
    Loop
    objFile.Close
End Function





