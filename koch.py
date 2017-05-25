import rhinoscriptsyntax as rs

def koch(v1, v2):
    
    c1 = 1/3
    c2 = 1/2
    c3 = 2/3
    
    dist = rs.Distance(v1, v2)
    x1 = rs.VectorSubtract(v2, v1)
    x2 = x1
    x3 = x1
    cross = x1
    
    x1 = rs.VectorScale(x1, c1)
    x1 += v1
    
    x2 = rs.VectorScale(x2, c2)
    cross = rs.VectorRotate(cross, 90, [0, 0, 1])
    cross = rs.VectorScale(cross, c1)
    x2 += v1 + cross
    
    x3 = rs.VectorScale(x3, c3)
    x3 += v1
    
    return v1, x1, x2, x3, v2
    
fullLine = []
def recur(v1, v2, reps):
    
    ptList = koch(v1, v2)
    if reps > 0:
        recur(ptList[0], ptList[1], reps - 1)
        recur(ptList[1], ptList[2], reps - 1)
        recur(ptList[2], ptList[3], reps - 1)
        recur(ptList[3], ptList[4], reps - 1)
        
        if reps == 1:
            line = rs.AddPolyline([ptList[0], ptList[1], ptList[2], ptList[3],ptList[4] ])
            fullLine.append(line)
            
        return fullLine
    
#a = koch(pt1, pt2)
a = recur(pt1, pt2, reps)
