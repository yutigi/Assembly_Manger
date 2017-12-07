import maya.cmds as cmds
#import os
#import pymel.core as pm

#print cmds.ls(type='assemblyDefinition')
print cmds.ls(selection=True,showType=True) #Check type form list selcetion
#cmds.assembly(name='MyAssembly')
#cmds.assembly('myAssembly', edit=True, createRepresentation='Locator',repName="myLocator", input=cmds.Locator())
'''
ls_import = cmds.ls(selection=True)
print ls_import
'''
############ Process #####################

def CreateAssemblyDefinition_Def(*args):
	nameAs = cmds.textField('CreateAsName',query=True,text=True)
	#print nameAs
	cmds.assembly(name=str(nameAs))
	print nameAs
	cmds.assembly(nameAs, edit=True, createRepresentation='Locator',repName=("myLocator"+'_'+nameAs), input=nameAs)
	AssemblySet_Selection(0)
	


def importMayaScene(*args):
	ls_import = cmds.ls(selection=True)
	print ls_import
	inputScene = cmds.fileDialog()
	print inputScene
	cmds.assembly(ls_import[0],edit=True,createRepresentation='Scene',input=inputScene)
	

def importCacheAlembic(*args):
	ls_import = cmds.ls(selection=True)
	print ls_import
	inputScene = cmds.fileDialog()
	print inputScene
	cmds.assembly(ls_import[0],edit=True,createRepresentation='Cache',input=inputScene)
	


#myinput = int(raw_input())

def AssemblySet_Selection(val):
	
	myinput = int(val)
	print myinput
	Assembly_set = cmds.ls(selection=True)
	#print Assembly_set
	As_position = 0
	for i in Assembly_set:
		#print i
	
		print (Assembly_set[As_position])
		#As_position = (As_position+1)
		As_Check = cmds.assembly(Assembly_set[As_position], query=True, listRepresentations=True) #check list of Representations
		print As_Check[myinput]
		cmds.assembly(Assembly_set[As_position],edit=True,active=As_Check[myinput])
		As_position = As_position + 1
		

def AssemblylistAll_check(*args):

	#cmds.ls(type='assemblyDefinition')
	Assemblyls_Nodetype = cmds.ls(type='assemblyDefinition')
	print Assemblyls_Nodetype
	cmds.select(Assemblyls_Nodetype)
	
def AssemblyReferencelistAll_check(*args):

	#cmds.ls(type='assemblyDefinition')
	Assemblyls_Nodetype = cmds.ls(type='assemblyReference')
	print Assemblyls_Nodetype
	cmds.select(Assemblyls_Nodetype)

def AssemblyShow_None(*args):
	AssemblySet_Selection(0)
	
def AssemblyShow_MainScene(*args):
	AssemblySet_Selection(1)
	
def AssemblyShow_PreviewScene(*args):
	AssemblySet_Selection(2)
	


def saveSceneAssembly(*args):

	'''
	sel=cmds.ls(sl=True)
	multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)"
	filename=cmds.fileDialog2(fileFilter=multipleFilters, dialogStyle=2)
	print filename
	'''
	cmds.SaveScene() # That is the answer what I search a long long time. 
	'''
	cmds.file(rename=filename)
	cmds.file(save=True,type="Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb);;All Files (*.*)")
	'''
	'''
	basicFilter = "*.mb"
	SavePath = cmds.fileDialog2(fileFilter=basicFilter, dialogStyle=2)
	print SavePath
	print SavePath[1:]
	'''
	#cmds.file(rename = SavePath_As)
	#cmds.file(save=True,f=True,type='mayaBinary')
	#pm.saveAs(SavePath, f=True)
	#print (os.path.exists(SavePath))
	#cmds.file(rename = str(SavePath))
	#cmds.file(save=True, type='mayaBinary' )

#saveSceneAssembly()


def NewSceneDef(*args):
	cmds.NewScene()


def CreateAssemblyReference(*args):
	'''
	multipleFilters = "All Files (*.*)"
	filename_AsDeifintion = cmds.fileDialog2(fileFilter=multipleFilters,fileMode=1, dialogStyle=2) #fileMode = 1 is	Indicate what the dialog is to return.( A single existing file.)
	print filename_AsDeifintion
	'''
	nameAsRef = cmds.textField('CreateAssemblyReference',query=True,text=True)
	cmds.assembly(name=(nameAsRef+'Reference'), type='assemblyReference')



def importAssemblyDeifinition(*args):
	multipleFilters = "All Files (*.*)"
	filename_AsDeifintion = cmds.fileDialog2(fileFilter=multipleFilters,fileMode=1, dialogStyle=2) #fileMode = 1 is	Indicate what the dialog is to return.( A single existing file.)
	print filename_AsDeifintion[0]
	SetAsseblyDeiginition = cmds.ls(selection=True)
	print str(SetAsseblyDeiginition[0])
	cmds.setAttr((str(SetAsseblyDeiginition[0])+'.definition'),str(filename_AsDeifintion[0]),type='string')

	

#############################################





############# Window #####################
'''
if cmds.window( 'AssemblyManager', exists=True):
	cmds.deleteUI('AssemblyManager')

window = cmds.window('AssemblyManager',wh=[300,600])

cmds.columnLayout()
#cmds.text(label='AssemblyManager')
cmds.text(label='1.First Step')
cmds.textField(text='Create Name')
cmds.button(label='Create Assembly Definition')
cmds.text(label='2.')
cmds.rowLayout(nc=3)


cmds.showWindow(window)

'''
'''
if cmds.dockControl('AssemblyManager',exists=True):
	print 'dock is enable'
	cmds.deleteUI('AssemblyManager')
'''

AssemblyManager = cmds.window()
#buttonForm = cmds.formLayout( parent = AssemblyManager )
cmds.columnLayout()
#cmds.text(label='AssemblyManager')
cmds.text(label='----------------------------------------')
cmds.text(label='1.First Step')
cmds.text(label='----------------------------------------')
cmds.textField('CreateAsName',text='Create Name')
cmds.button(label='Create Assembly Definition',command = CreateAssemblyDefinition_Def)
cmds.text(label='----------------------------------------')
cmds.text(label='2.import Maya Scene')
cmds.text(label='----------------------------------------')
cmds.button(label='import Maya Scene',command = importMayaScene)
cmds.button(label='import Cache Alembic',command = importCacheAlembic)
cmds.text(label='----------------------------------------')
cmds.text(label='3.View')
cmds.text(label='----------------------------------------')
cmds.checkBox('checkSelection',label='All', changeCommand = AssemblylistAll_check)
cmds.checkBox('checkReferenceSelection',label='All_Reference', changeCommand = AssemblyReferencelistAll_check)

cmds.button(label='None', command = AssemblyShow_None)
cmds.button(label='Main_Scene', command = AssemblyShow_MainScene)
cmds.button(label='Preview_Scene', command = AssemblyShow_PreviewScene)
cmds.text(label='by the way, you must save Scene and new file')
cmds.button(label= 'Save Scene assemblyDefinition', command = saveSceneAssembly)
cmds.text(label='----------------------------------------')
cmds.text(label='4.Create Assembly Reference')
cmds.button(label='NewScene',command = NewSceneDef)
cmds.textField('CreateAssemblyReference',text='CreateAssemblyReference_Name')
cmds.button(label='CreateAssemblyReference',command = CreateAssemblyReference)
cmds.button(label='import AssemblyDefinition',enable=True,command = importAssemblyDeifinition)

cmds.rowLayout(nc=3)

allowedAreas = ['right', 'left']
cmds.dockControl(label='AssemblyManager', area='right', content=AssemblyManager, allowedArea=allowedAreas ,w=400,)

##########################################################################################