import pandas as pd
#import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
from django.core.files import File
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='files')
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
def send_receipt(receipt):
    df = pd.DataFrame()
    df['Question'] = ["Q1", "Q2", "Q3", "Q4"]
    df['Charles'] = [3, 4, 5, 3]
    df['Mike'] = [3, 3, 4, 4]


    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "Listing about the details of the order", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    pdf.cell(50, 10, 'Question', 1, 0, 'C')
    pdf.cell(40, 10, 'Charles', 1, 0, 'C')
    pdf.cell(40, 10, 'Mike', 1, 2, 'C')
    pdf.cell(-90)
    pdf.set_font('arial', '', 12)
    for i in range(0, len(df)):
        pdf.cell(50, 10, '%s' % (df['Question'].iloc[i]), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(df.Mike.iloc[i])), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(df.Charles.iloc[i])), 1, 2, 'C')
    pdf.cell(-90)
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-30)
    #pdf.image('https://secure.ce-tescoassets.com/assets/HU/032/5998817312032/ShotType1_540x540.jpg', x = None, y = None, w = 0, h = 0, type = '', link = '')
    path=fs.location+'/receipts/'+str(receipt.order.id)+'.pdf'
    pdf.output(path, 'F')
    #f=open(path,'r')
    receipt.recepit_file=str(receipt.order.id)+'.pdf'
    receipt.save()

#SENDING EMAIL----------
    plaintext = get_template('email.txt')
    htmly     = get_template('email.html')

#    d = Context({ 'username': receipt.user.email })
    d= { 'username': receipt.user.email }
    subject, from_email, to = 'Receipt', 'kovszasz@gmail.com',receipt.user.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file(path) #,receipt.recepit_file.read(),receipt.recepit_file.contet_type)
    msg.send()
    #f.close()
"""
def Segmentation():
    masterVolumeNode=slicer.util.loadVolume('/Users/kovszasz/Downloads/I0000044-1.nrrd')
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

    segmentsFromHounsfieldUnits = [["fetal",58.24,198.24]]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Create segment
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID)
    # Fill by thresholding
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))
    effect.self().onApply()
"""