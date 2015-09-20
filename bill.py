from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
def make_pdf(consumer,units,area,region,Type,pay):
    print consumer,units,area,region,Type,pay
    x=A4[0]
    y=A4[1]
    date=str(datetime.today().date())
    filename="bill.pdf"
    c=canvas.Canvas(filename,pagesize=A4)
    c.setTitle("Bill for "+ str(consumer))
    c.drawCentredString(x/2,y-30,"Electricity Bill")
    c.drawString(40,y-70,date)
    c.line(40,y-100,x-40,y-100)
    text=c.beginText(60,y-150)
    text.textLine("Electricity Bill for "+ str(consumer) + ".")
    msg="Units Consumed : " + str(units) + " at "+ region + " in " + area +"."
    text.textLine(msg)
    msg="Bill amount calculated for " + Type + " is " + str(pay)
    text.textLine(msg)
    c.drawText(text)
    c.showPage()
    c.save()

#make_pdf("shivang",234,"Rural","R1","Commertial",23424)
