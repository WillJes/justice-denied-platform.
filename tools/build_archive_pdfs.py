from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "archive"
RED = colors.HexColor("#B42217")
INK = colors.HexColor("#171513")
PAPER = colors.HexColor("#F4EDDF")
MUTED = colors.HexColor("#6C655C")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverKicker", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=12, textColor=RED, tracking=2, alignment=TA_CENTER, spaceAfter=22))
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=29, leading=34, textColor=INK, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontName="Helvetica", fontSize=11.5, leading=18, textColor=MUTED, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=INK, spaceBefore=8, spaceAfter=14))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10, leading=14, textColor=RED, spaceBefore=15, spaceAfter=7, textTransform="uppercase"))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.8, leading=15, textColor=INK, spaceAfter=10))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.5, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="Bulletx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.8, leading=14.5, leftIndent=16, firstLineIndent=-9, bulletIndent=5, spaceAfter=6))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#C8BFB1"))
    canvas.line(0.65*inch, 0.58*inch, 7.85*inch, 0.58*inch)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(0.65*inch, 0.38*inch, "JUSTICE DENIED PUBLIC ARCHIVE")
    canvas.drawRightString(7.85*inch, 0.38*inch, f"PAGE {doc.page}")
    canvas.restoreState()

def cover(title, subtitle, label):
    return [Spacer(1, 1.5*inch), Paragraph(label, styles["CoverKicker"]), Paragraph(title.replace("\\n", "<br/>"), styles["CoverTitle"]), Paragraph(subtitle, styles["CoverSub"]), Spacer(1, 0.65*inch), Table([["JD", "A FAMILY. A SYSTEM. A FIGHT FOR THE TRUTH."]], colWidths=[0.65*inch, 4.8*inch], style=TableStyle([("BACKGROUND",(0,0),(0,0),INK),("TEXTCOLOR",(0,0),(0,0),colors.white),("ALIGN",(0,0),(0,0),"CENTER"),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("FONT",(0,0),(0,0),"Helvetica-Bold",13),("FONT",(1,0),(1,0),"Helvetica-Bold",7),("TEXTCOLOR",(1,0),(1,0),MUTED),("LEFTPADDING",(1,0),(1,0),14),("BOX",(0,0),(-1,-1),0.5,colors.HexColor("#C8BFB1"))])), PageBreak()]

def para(text, style="Bodyx"): return Paragraph(text, styles[style])
def bullets(items): return [Paragraph("• " + x, styles["Bulletx"]) for x in items]
def build(path, title, story):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(path), pagesize=letter, rightMargin=.7*inch, leftMargin=.7*inch, topMargin=.7*inch, bottomMargin=.8*inch, title=title, author="Justice Denied")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)

overview = cover("Justice Denied\nCase Overview", "A public-facing introduction to the story, the family's requests, and the purpose of the archive.", "PUBLIC ARCHIVE • CASE OVERVIEW")
overview += [para("About the Case", "H1x"), para("<b>Gary Jerome Weems died on November 6, 1993, in Lowell, Massachusetts.</b> His family says they were left for decades with unresolved questions about the circumstances of his death, the handling of his remains, conflicting records, and the lack of timely family notification."), para("Justice Denied follows his daughter, filmmaker Jestina Weems-Rosenduft, as she seeks a lawful exhumation, DNA confirmation, an independent second autopsy, and the opportunity to rebury her father with dignity."), para("What the Family Is Seeking", "H2x")] + bullets(["A lawful exhumation and verified identification of the remains.", "Independent forensic review, including DNA testing and a second autopsy where possible.", "A complete and accurate accounting of how the death, remains, belongings, and notification process were handled.", "A dignified family burial and a truthful public record."])
overview += [para("Why the Archive Exists", "H2x"), para("The archive helps audiences understand the documentary's research trail without publishing every sensitive source record. It separates public summaries from private legal, medical, identifying, and death-scene materials."), para("Important Context", "H2x"), para("This document summarizes the family's position and documentary research. Questions, allegations, and disputed interpretations are identified as such; they are not presented as judicial findings. Original records should be read in full and reviewed by qualified legal and forensic professionals."), para("Film Credits", "H2x"), para("<b>Creative Director, Editor, Producer:</b> Jestina Weems-Rosenduft<br/><b>Director and Cinematographer:</b> Daphne Ostendorf<br/><b>Executive Producers:</b> Ethan Rosenduft and Denise Gordon<br/><b>Second Camera:</b> Tonia Margas"), para("Contact", "H2x"), para("Speaking, screenings, educational use, and sponsorship: <b>JesTTMI@gmail.com</b>")]
build(OUT/"case-overview"/"justice-denied-case-overview.pdf", "Justice Denied Case Overview", overview)

inventory = cover("Gary Jerome Weems\nRecords Inventory", "A category guide to the source material reviewed for the documentary and legal research.", "PUBLIC ARCHIVE • RECORDS GUIDE")
inventory += [para("How to Use This Guide", "H1x"), para("This inventory describes the types of records held in the private production and case archive. It does not reproduce restricted pages. Public releases should be redacted, contextualized, and reviewed before publication.")]
rows=[["CATEGORY","EXAMPLES IN SOURCE COLLECTION","PUBLIC STATUS"],["Medical examiner","Correspondence, autopsy report, death certificate, intake and burial-related records","Restricted / summarized"],["Police and first response","Incident reports, police reports, EMT documentation, officer records","Redacted release only"],["Witness material","Typed witness statements and proposed interview or interrogatory questions","Contextual review"],["Court and legal","Federal and state filings, decisions, attorney correspondence, claim materials","Selected public filings"],["Agency correspondence","Medical examiner, law-enforcement, FBI, and records-request correspondence","Review before release"],["News and public history","Historical newspaper coverage and related public reporting","Citation or licensed excerpt"],["Family research","Case thesis, witness list, questions, emails, notes, and investigative chronology","Private / selected summary"]]
table=Table([[para(c,"Smallx") for c in r] for r in rows],colWidths=[1.2*inch,3.55*inch,1.65*inch],repeatRows=1)
table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),INK),("TEXTCOLOR",(0,0),(-1,0),colors.white),("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),.35,colors.HexColor("#BFB5A6")),("BACKGROUND",(0,1),(-1,-1),colors.HexColor("#F2EBDD")),("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
inventory += [table, Spacer(1,18), para("Source PDFs Reviewed", "H2x")] + bullets(["Discovery.pdf - 16-page working research and discovery outline.", "staples_scan_1674138443882.pdf - 52-page mixed record scan containing first-response, police, medical examiner, news, and legal materials.", "staples_scan_1674138522685.pdf - 61-page mixed legal and correspondence scan.", "Weems, Gary 1993-3665.pdf - 85-page compiled record set containing sensitive and duplicated material."])
inventory += [para("Publication Rules", "H2x")] + bullets(["Do not publish death-scene or autopsy photographs on the open archive.", "Remove addresses, identification cards, signatures, birth dates, account numbers, private emails, and phone numbers.", "Label family theories and allegations as disputed claims, not established facts.", "Keep an unchanged private original and record every redaction made to a public copy.", "Obtain legal review before releasing sensitive court, medical, or witness material."])
build(OUT/"records-guide"/"gary-weems-records-inventory.pdf", "Gary Jerome Weems Records Inventory", inventory)

timeline = cover("Litigation and Advocacy\nTimeline", "A concise chronology of the documented campaign for answers, exhumation, independent review, and dignified reburial.", "PUBLIC ARCHIVE • LEGAL TIMELINE")
timeline += [para("Key Milestones", "H1x")]
events=[("NOVEMBER 6, 1993","Gary Jerome Weems dies in Lowell, Massachusetts. The family later raises questions about notification, record consistency, the handling of his belongings and remains, and the reported circumstances of death."),("1996-1998","Earlier federal litigation and related appellate materials become part of the family's historical record collection."),("APRIL 27, 2023","In Middlesex Superior Court matter 2381CV00130, a Rule 12(b) motion is denied, allowing the dispute to continue at that stage."),("JUNE 30, 2023","A motion concerning amendment is allowed."),("JUNE 12, 2024","A hearing is held and the matter is taken under advisement."),("SEPTEMBER 17, 2024","Dismissal motions are allowed."),("AUGUST 9, 2025","A later motion is denied for the same stated reasons."),("2025-2026","The family continues pursuing expert review, funding, documentary outreach, and options for further legal action.")]
for date,text in events: timeline += [KeepTogether([para(date,"H2x"),para(text)])]
timeline += [para("Current Public Position", "H2x"), para("The family continues to seek lawful exhumation, DNA confirmation, independent forensic examination, and dignified reburial. This timeline is informational and is not legal advice or a substitute for the official docket."), para("Verification Note", "H2x"), para("Dates should be checked against certified docket entries before use in litigation, press reporting, or formal advocacy.")]
build(OUT/"legal-timeline"/"justice-denied-litigation-timeline.pdf", "Justice Denied Litigation and Advocacy Timeline", timeline)

questions = cover("Unanswered Questions\nand Research Priorities", "A public summary of the questions guiding the documentary's continuing investigation.", "PUBLIC ARCHIVE • RESEARCH")
questions += [para("Purpose", "H1x"), para("The source archive contains proposed interrogatories, witness questions, and research notes. This public edition groups the central issues without reproducing private contact details or sensitive imagery.")]
groups=[("Identification and family notification",["How was Gary identified, and which records document that identification?","What efforts were made to locate and notify his wife, children, or other relatives?","Who authorized burial, and where is the complete authorization record?"]),("Scene and first response",["What is the verified timeline from the initial report through police and EMT arrival?","How did responders describe Gary's physical condition and possible signs of trauma?","What photographs, notes, recordings, or property logs were created and preserved?"]),("Medical examiner records",["How were the reported cause and manner of death reached?","Which findings came from direct examination and which relied on information provided by others?","Why do the family and filmmakers identify inconsistencies in numbering, descriptions, or documentation?"]),("Belongings and chain of custody",["What property was recovered, who held it, and when was it returned?","Do property records help explain how Gary was identified or why family notification was delayed?"]),("Witness accounts",["Which witnesses were interviewed, when, and by whom?","Were statements recorded, signed, or preserved in their original form?","Where accounts conflict, what independent evidence can resolve the difference?"]),("Remains and independent review",["What legal and logistical steps are required for exhumation?","Can DNA confirm identity and can modern forensic methods answer unresolved questions?","How can the family secure a dignified reburial after independent review?"])]
for title,items in groups: questions += [para(title,"H2x")] + bullets(items)
questions += [para("Editorial Standard", "H2x"), para("These are research questions, not accusations or findings. The documentary seeks records, testimony, expert analysis, and transparent review before drawing conclusions.")]
build(OUT/"research-questions"/"justice-denied-research-questions.pdf", "Justice Denied Unanswered Questions", questions)

print("Created:")
for p in sorted(OUT.rglob("*.pdf")): print(p)
