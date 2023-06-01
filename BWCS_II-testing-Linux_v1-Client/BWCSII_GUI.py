# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainframe
###########################################################################

class mainframe ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cloud Sensor Monitoring", pos = wx.DefaultPosition, size = wx.Size( 900,470 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 900,470 ), wx.Size( 1200,470 ) )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Kodaikanal Solar Observatory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		self.m_staticText27.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer7.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText28 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Cloud Monitor/ Weather station", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer7.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel8.SetSizer( bSizer7 )
		self.m_panel8.Layout()
		bSizer7.Fit( self.m_panel8 )
		bSizer6.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText29 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Date/Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText29, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel6, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.text_dateTime = wx.StaticText( self.m_panel6, wx.ID_ANY, u"12:00hrs, 07 February 2023, Tuesday", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_dateTime.Wrap( -1 )

		self.text_dateTime.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer5.Add( self.text_dateTime, 1, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_socketStatus = wx.Button( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 15,15 ), 0 )
		self.button_socketStatus.SetMaxSize( wx.Size( 15,15 ) )

		bSizer5.Add( self.button_socketStatus, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel3 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Ambient Temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_temperature = wx.StaticText( self.m_panel3, wx.ID_ANY, u"+16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_temperature.Wrap( -1 )

		self.text_temperature.SetFont( wx.Font( 8, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1.Add( self.text_temperature, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Sky Temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer1.Add( self.m_staticText16, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self.m_panel3, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer1.Add( self.m_staticText17, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_skyTemp = wx.StaticText( self.m_panel3, wx.ID_ANY, u"-16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_skyTemp.Wrap( -1 )

		gSizer1.Add( self.text_skyTemp, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Humidity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer1.Add( self.m_staticText7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer1.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )

		self.text_humidity = wx.StaticText( self.m_panel3, wx.ID_ANY, u"75%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_humidity.Wrap( -1 )

		gSizer1.Add( self.text_humidity, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Wind Speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer1.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer1.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_windspeed = wx.StaticText( self.m_panel3, wx.ID_ANY, u"2.5KM/hr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_windspeed.Wrap( -1 )

		gSizer1.Add( self.text_windspeed, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText381 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Dew Point", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText381.Wrap( -1 )

		gSizer1.Add( self.m_staticText381, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText391 = wx.StaticText( self.m_panel3, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )

		gSizer1.Add( self.m_staticText391, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_dewpoint = wx.StaticText( self.m_panel3, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_dewpoint.Wrap( -1 )

		gSizer1.Add( self.text_dewpoint, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( gSizer1 )
		self.m_panel3.Layout()
		gSizer1.Fit( self.m_panel3 )
		bSizer2.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Sky" ), wx.VERTICAL )

		self.text_skyCondition = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_skyCondition.Wrap( -1 )

		self.text_skyCondition.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer1.Add( self.text_skyCondition, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer1, 1, wx.EXPAND, 2 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Wind" ), wx.VERTICAL )

		self.text_windCondition = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Calm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_windCondition.Wrap( -1 )

		self.text_windCondition.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer2.Add( self.text_windCondition, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer2, 1, wx.EXPAND, 2 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Moisture" ), wx.VERTICAL )

		self.text_humCondition = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Dry", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_humCondition.Wrap( -1 )

		self.text_humCondition.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer3.Add( self.text_humCondition, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 2 )

		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Rain" ), wx.VERTICAL )

		self.text_rainCondition = wx.StaticText( sbSizer6.GetStaticBox(), wx.ID_ANY, u"No Rain", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_rainCondition.Wrap( -1 )

		self.text_rainCondition.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer6.Add( self.text_rainCondition, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( sbSizer6, 1, wx.EXPAND, 2 )


		self.m_panel4.SetSizer( bSizer3 )
		self.m_panel4.Layout()
		bSizer3.Fit( self.m_panel4 )
		bSizer71.Add( self.m_panel4, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText32 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Sensor Unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		gSizer2.Add( self.m_staticText32, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self.m_panel6, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		gSizer2.Add( self.m_staticText33, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText34 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Boltwood Cloud Sensor II", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		gSizer2.Add( self.m_staticText34, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText35 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Serial Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer2.Add( self.m_staticText35, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText36 = wx.StaticText( self.m_panel6, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		gSizer2.Add( self.m_staticText36, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_serialNum = wx.StaticText( self.m_panel6, wx.ID_ANY, u"05198", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_serialNum.Wrap( -1 )

		gSizer2.Add( self.text_serialNum, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText38 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Firmware Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		gSizer2.Add( self.m_staticText38, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText39 = wx.StaticText( self.m_panel6, wx.ID_ANY, u":", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		gSizer2.Add( self.m_staticText39, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_firmwareVer = wx.StaticText( self.m_panel6, wx.ID_ANY, u"v73", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_firmwareVer.Wrap( -1 )

		gSizer2.Add( self.text_firmwareVer, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer71.Add( gSizer2, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer71, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.panel_portSelect = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_portSelect.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText45 = wx.StaticText( self.panel_portSelect, wx.ID_ANY, u"Server IP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.m_staticText45, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_host_IP = wx.TextCtrl( self.panel_portSelect, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer9.Add( self.text_host_IP, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText382 = wx.StaticText( self.panel_portSelect, wx.ID_ANY, u"Port No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText382.Wrap( -1 )

		bSizer9.Add( self.m_staticText382, 0, wx.ALL|wx.EXPAND, 5 )

		self.text_host_portNo = wx.TextCtrl( self.panel_portSelect, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.text_host_portNo.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.text_host_portNo, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_comConnect = wx.Button( self.panel_portSelect, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.Size( 90,20 ), 0 )
		bSizer9.Add( self.button_comConnect, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.button_exit = wx.Button( self.panel_portSelect, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 90,20 ), 0 )
		bSizer9.Add( self.button_exit, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.panel_portSelect.SetSizer( bSizer9 )
		self.panel_portSelect.Layout()
		bSizer9.Fit( self.panel_portSelect )
		bSizer8.Add( self.panel_portSelect, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel61 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.text_lastUpdate = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Waiting for data...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_lastUpdate.Wrap( -1 )

		bSizer10.Add( self.text_lastUpdate, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel61.SetSizer( bSizer10 )
		self.m_panel61.Layout()
		bSizer10.Fit( self.m_panel61 )
		bSizer8.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )

		self.m_staticText41 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Developed by", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText42 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Anand M N (Research Assistant)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer6.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText44 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"anand.mn@iiap.res.in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer6.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel6.SetSizer( bSizer6 )
		self.m_panel6.Layout()
		bSizer6.Fit( self.m_panel6 )
		bSizer1.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.mainFrame_OnClose )
		self.button_comConnect.Bind( wx.EVT_BUTTON, self.button_comConnect_OnClick )
		self.button_exit.Bind( wx.EVT_BUTTON, self.button_exit_OnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def mainFrame_OnClose( self, event ):
		event.Skip()

	def button_comConnect_OnClick( self, event ):
		event.Skip()

	def button_exit_OnClick( self, event ):
		event.Skip()


