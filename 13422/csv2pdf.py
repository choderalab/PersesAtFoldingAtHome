#!/usr/bin/env python3
# (C) 2017 OpenEye Scientific Software Inc. All rights reserved.
#
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of OpenEye products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. OpenEye claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable OpenEye offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED.  OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall OpenEye be
# liable for any damages or liability in connection with the Sample Code
# or its use.

#############################################################################
# Converts a CSV or a SDF file into PDF
#############################################################################

import sys
from openeye import oechem
from openeye import oedepict


def main(argv=[__name__]):

    itf = oechem.OEInterface(InterfaceData)
    oedepict.OEConfigure2DMolDisplayOptions(itf, oedepict.OE2DMolDisplaySetup_AromaticStyle)

    if not oechem.OEParseCommandLine(itf, argv):
        return 1

    iname = itf.GetString("-in")
    oname = itf.GetString("-out")

    pagebypage = itf.GetBool("-pagebypage")

    # check input/output files

    ifs = oechem.oemolistream()
    if not ifs.open(iname):
        oechem.OEThrow.Fatal("Cannot open input file!")

    if ifs.GetFormat() not in [oechem.OEFormat_CSV, oechem.OEFormat_SDF]:
        oechem.OEThrow.Fatal("Input must be CSV or SDF file!")

    ext = oechem.OEGetFileExtension(oname)
    if not pagebypage and not oedepict.OEIsRegisteredMultiPageImageFile(ext):
        oechem.OEThrow.Warning("Report will be generated into separate pages!")
        pagebypage = True

    # import molecules

    mollist = []
    for mol in ifs.GetOEGraphMols():
        mollist.append(oechem.OEGraphMol(mol))

    # collect data tags

    tags = CollectDataTags(mollist)

    # initialize multi-page report

    rows, cols = 3, 2
    ropts = oedepict.OEReportOptions(rows, cols)
    ropts.SetHeaderHeight(25)
    ropts.SetFooterHeight(25)
    ropts.SetCellGap(2)
    ropts.SetPageMargins(10)
    report = oedepict.OEReport(ropts)

    # setup depiction options

    cellwidth, cellheight = report.GetCellWidth(), report.GetCellHeight()
    opts = oedepict.OE2DMolDisplayOptions(cellwidth, cellheight, oedepict.OEScale_AutoScale)
    oedepict.OESetup2DMolDisplayOptions(opts, itf)

    # generate report

    DepictMoleculesWithData(report, mollist, iname, tags, opts)

    if pagebypage:
        oedepict.OEWriteReportPageByPage(oname, report)
    else:
        oedepict.OEWriteReport(oname, report)

    return 0


def CollectDataTags(mollist):

    tags = []
    for mol in mollist:
        for dp in oechem.OEGetSDDataIter(mol):
            if not dp.GetTag() in tags:
                tags.append(dp.GetTag())

    return tags


def DepictMoleculesWithData(report, mollist, iname, tags, opts):

    for mol in mollist:

        # render molecule

        cell = report.NewCell()
        oedepict.OEPrepareDepiction(mol)
        disp = oedepict.OE2DMolDisplay(mol, opts)
        oedepict.OERenderMolecule(cell, disp)
        oedepict.OEDrawCurvedBorder(cell, oedepict.OELightGreyPen, 10.0)

        # render corresponding data

        cell = report.NewCell()
        RenderData(cell, mol, tags)

    # add input filnename to headers

    headerfont = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
                                 12, oedepict.OEAlignment_Center, oechem.OEBlack)
    headerpos = oedepict.OE2DPoint(report.GetHeaderWidth() / 2.0, report.GetHeaderHeight() / 2.0)

    for header in report.GetHeaders():
        header.DrawText(headerpos, iname, headerfont)

    # add page number to footers

    footerfont = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
                                 12, oedepict.OEAlignment_Center, oechem.OEBlack)
    footerpos = oedepict.OE2DPoint(report.GetFooterWidth() / 2.0, report.GetFooterHeight() / 2.0)

    for pageidx, footer in enumerate(report.GetFooters()):
        footer.DrawText(footerpos, "- %d -" % (pageidx + 1), footerfont)


def RenderData(image, mol, tags):

    data = []
    for tag in tags:
        value = "N/A"
        if oechem.OEHasSDData(mol, tag):
            value = oechem.OEGetSDData(mol, tag)
        data.append((tag, value))

    nrdata = len(data)

    tableopts = oedepict.OEImageTableOptions(nrdata, 2, oedepict.OEImageTableStyle_LightBlue)
    tableopts.SetColumnWidths([10, 20])
    tableopts.SetMargins(2.0)
    tableopts.SetHeader(False)
    tableopts.SetStubColumn(True)
    table = oedepict.OEImageTable(image, tableopts)

    for row, (tag, value) in enumerate(data):
        cell = table.GetCell(row + 1, 1)
        table.DrawText(cell, tag + ":")
        cell = table.GetBodyCell(row + 1, 1)
        table.DrawText(cell, value)


InterfaceData = '''
!CATEGORY "input/output options"

    !PARAMETER -in
      !ALIAS -i
      !TYPE string
      !REQUIRED true
      !KEYLESS 1
      !VISIBILITY simple
      !BRIEF Input filename(s)
    !END

    !PARAMETER -out
      !ALIAS -o
      !TYPE string
      !REQUIRED true
      !KEYLESS 2
      !VISIBILITY simple
      !BRIEF Output PDF filename
    !END

!END

!CATEGORY "report options"

    !PARAMETER -pagebypage
      !ALIAS -p
      !TYPE bool
      !REQUIRED false
      !DEFAULT false
      !VISIBILITY simple
      !BRIEF Write individual numbered separate pages
    !END

!END
'''

if __name__ == "__main__":
        sys.exit(main(sys.argv))
