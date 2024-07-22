# Author-puhitaku
# Description-Create a sketch on the YZ plane with axis lines that cross the origin point

import adsk.core, adsk.fusion, adsk.cam, traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Create a new sketch on the YZ plane
        sketch = rootComp.sketches.add(rootComp.yZConstructionPlane)

        # Create the Y axis line
        point1_1 = adsk.core.Point3D.create(-30, 0, 0)
        point2_1 = adsk.core.Point3D.create(30, 0, 0)
        line_1 = sketch.sketchCurves.sketchLines.addByTwoPoints(point1_1, point2_1)
        line_1.isConstruction = True

        # Create the Z axis line
        point1_2 = adsk.core.Point3D.create(0, -30, 0)
        point2_2 = adsk.core.Point3D.create(0, 30, 0)
        line_2 = sketch.sketchCurves.sketchLines.addByTwoPoints(point1_2, point2_2)
        line_2.isConstruction = True

        # Add constraints to bind the midpoints of the lines to the origin
        sketch.geometricConstraints.addMidPoint(sketch.originPoint, line_1)
        sketch.geometricConstraints.addMidPoint(sketch.originPoint, line_2)
        sketch.geometricConstraints.addHorizontal(line_1)
        sketch.geometricConstraints.addVertical(line_2)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
